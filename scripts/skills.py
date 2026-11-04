"""Scaffold and structurally validate portable Agent Skills (Python 3.10+)."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("Install development dependencies: python -m pip install -r requirements-dev.txt")


WORKSPACE = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate metadata keys instead of silently accepting the last value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise ValueError("frontmatter mapping keys must be strings")
        if key in result:
            raise ValueError(f"duplicate frontmatter key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def valid_name(name):
    return isinstance(name, str) and len(name) <= 64 and NAME.fullmatch(name) is not None


def scaffold(name, description, root):
    if not valid_name(name):
        raise ValueError("name must be 1-64 lowercase letters/digits with single separating hyphens")
    if not description.strip() or len(description) > 1024:
        raise ValueError("description must be 1-1024 characters and not blank")
    template = (WORKSPACE / "templates/skill/SKILL.md").read_text(encoding="utf-8")
    # Serialize the description as a scalar so punctuation cannot inject YAML fields.
    scalar = yaml.safe_dump(description, default_style='"', allow_unicode=True).strip()
    content = template.replace("{{SKILL_NAME}}", name).replace("{{SKILL_DESCRIPTION}}", scalar)
    target = root / name
    target.mkdir(parents=True, exist_ok=False)
    (target / "SKILL.md").write_text(content, encoding="utf-8")
    return target



def validate_resource_links(skill):
    """Reject broken/escaping local Markdown links in a standalone skill bundle."""
    errors = []
    root = skill.resolve()
    for markdown in sorted(skill.rglob("*.md")):
        try:
            lines = markdown.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read linked Markdown {markdown}: {exc}")
            continue
        fenced = False
        for line_number, line in enumerate(lines, start=1):
            if re.match(r"^\\s*(?:```|~~~)", line):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in re.finditer(r"!?\\[[^\\]\\n]+\\]\\(([^)\\n]+)\\)", line):
                destination = match.group(1).strip()
                if destination.startswith("<") and destination.endswith(">"):
                    destination = destination[1:-1]
                # Optional Markdown title: [label](path "title")
                destination = destination.split(' "', 1)[0]
                parts = urlsplit(destination)
                if parts.scheme or destination.startswith("//") or not parts.path:
                    continue
                target = (markdown.parent / unquote(parts.path)).resolve()
                label = f"{markdown.relative_to(skill)}:{line_number} -> {destination}"
                if not target.is_relative_to(root):
                    errors.append(f"resource link escapes skill directory: {label}")
                elif not target.is_file():
                    errors.append(f"missing linked resource: {label}")
    return errors

def validate(skill):
    errors = []
    try:
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read SKILL.md: {exc}"]
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return ["SKILL.md must start with YAML frontmatter (---)"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return ["frontmatter must end with ---"]
    try:
        metadata = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError, RecursionError) as exc:
        return [f"invalid YAML frontmatter: {exc}"]
    if not isinstance(metadata, dict):
        return ["frontmatter must be a mapping"]
    for field in sorted(set(metadata) - FIELDS):
        errors.append(f"unsupported frontmatter field: {field}; use metadata for custom fields")
    name = metadata.get("name")
    if not valid_name(name):
        errors.append("name must be 1-64 lowercase letters/digits with single separating hyphens")
    elif name != skill.name:
        errors.append(f"name {name!r} must match directory {skill.name!r}")
    for field, maximum in (("description", 1024), ("compatibility", 500)):
        if field == "compatibility" and field not in metadata:
            continue
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > maximum:
            errors.append(f"{field} must be a nonblank string of at most {maximum} characters")
    for field in ("license", "allowed-tools"):
        if field in metadata and (not isinstance(metadata[field], str) or not metadata[field].strip()):
            errors.append(f"{field} must be a nonblank string")
    if "metadata" in metadata:
        values = metadata["metadata"]
        if not isinstance(values, dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in values.items()
        ):
            errors.append("metadata must map string keys to string values")
    if not "\n".join(lines[end + 1:]).strip():
        errors.append("instructions must not be empty")
    if re.search(r"\bTODO\b|\{\{SKILL_(?:NAME|DESCRIPTION)\}\}", text):
        errors.append("replace draft TODO markers and template placeholders before release")
    if len(lines) >= 500:
        errors.append("keep SKILL.md below 500 lines; move detail into references/")
    errors.extend(validate_resource_links(skill))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    new = commands.add_parser("new", help="create a draft skill without overwriting existing content")
    new.add_argument("name")
    new.add_argument("--description", required=True)
    new.add_argument("--root", type=Path, default=WORKSPACE / "skills")
    check = commands.add_parser("validate", help="validate a skill or each immediate skill directory")
    check.add_argument("skill", nargs="?", type=Path)
    check.add_argument("--root", type=Path, default=WORKSPACE / "skills")
    args = parser.parse_args(argv)
    try:
        if args.command == "new":
            target = scaffold(args.name, args.description, args.root)
            print(f"Created {target}. Replace TODO markers before validation.")
            return 0
        if args.skill is not None:
            skills = [args.skill]
        elif not args.root.is_dir():
            print(f"No skill collection at {args.root}; create a skill with the new command.", file=sys.stderr)
            return 1
        else:
            skills = sorted(path for path in args.root.iterdir() if path.is_dir() and not path.name.startswith("."))
        if not skills:
            print("No skills found; create a skill with the new command.", file=sys.stderr)
            return 1
        failed = False
        for skill in skills:
            errors = validate(skill)
            failed |= bool(errors)
            if errors:
                for error in errors:
                    print(f"FAIL {skill}: {error}", file=sys.stderr)
            else:
                print(f"PASS {skill}")
        return int(failed)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
