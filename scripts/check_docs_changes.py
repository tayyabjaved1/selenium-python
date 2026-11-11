#!/usr/bin/env python3
import os
import re
import subprocess
import sys

base = os.environ.get("GITHUB_BASE_REF")
base = f"origin/{base}" if base else os.environ.get("DOCS_BASE_REF", "HEAD^")

try:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    changed = [line for line in result.stdout.splitlines() if line]
except subprocess.CalledProcessError:
    print(f"Could not compare changes against '{base}'. Fetch the base branch or set DOCS_BASE_REF.", file=sys.stderr)
    sys.exit(2)

if not changed:
    print("Documentation check: no changed files detected.")
    sys.exit(0)

changed_set = set(changed)


def has_any(*paths):
    return any(path in changed_set for path in paths)


requirements = []


def add(condition, message):
    if condition:
        requirements.append(message)


features_changed = any(re.match(r"^features/.*\.feature$", p) for p in changed)
steps_changed = any(re.match(r"^features/steps/", p) or p == "features/environment.py" for p in changed)
factories_changed = any(re.match(r"^src/data/(factories|generators|builders)/", p) for p in changed)
module_code_changed = any(re.match(r"^src/pages/", p) for p in changed)
api_changed = any(re.match(r"^src/api/", p) for p in changed)
core_changed = any(re.match(r"^src/core/", p) for p in changed)
config_changed = any(
    p in ("behave.ini", "pytest.ini", "requirements.txt", ".env.example") or p.startswith(".github/workflows/")
    for p in changed
)

add(features_changed and not has_any("docs/TEST_CATALOG.md"), "Feature file changes require docs/TEST_CATALOG.md.")
add(features_changed and not has_any("docs/TRACEABILITY.md"), "Feature file changes require docs/TRACEABILITY.md.")
add(steps_changed and not has_any("docs/TEST_AUTHORING_GUIDE.md"), "Step definition/hook changes require docs/TEST_AUTHORING_GUIDE.md.")
add(factories_changed and not has_any("docs/DATA_FACTORY_GUIDE.md"), "Factory/generator/builder changes require docs/DATA_FACTORY_GUIDE.md.")
add(factories_changed and not has_any("docs/FACTORY_CATALOG.md"), "Factory/generator/builder changes require docs/FACTORY_CATALOG.md.")
add(module_code_changed and not has_any("docs/MODULE_CATALOG.md"), "Module (page object) changes require docs/MODULE_CATALOG.md.")
add(api_changed and not has_any("docs/API_GUIDE.md"), "API client changes require docs/API_GUIDE.md.")
add(core_changed and not has_any("docs/ARCHITECTURE.md"), "Core architecture changes require docs/ARCHITECTURE.md.")
add(config_changed and not has_any("README.md"), "Configuration/CI/dependency changes require README.md.")
add(config_changed and not has_any("docs/CONFIGURATION.md"), "Configuration/CI/dependency changes require docs/CONFIGURATION.md.")

if requirements:
    print("\nDocumentation check failed. Update the required docs in this same change:\n", file=sys.stderr)
    for item in requirements:
        print(f"  - {item}", file=sys.stderr)
    print(
        "\nIf this is a genuinely non-behavioral change, use the docs-not-required PR label and document the reason in the PR.",
        file=sys.stderr,
    )
    sys.exit(1)

missing_files = [
    path
    for path in (
        "docs/DOCUMENTATION_POLICY.md",
        "docs/CHANGE_IMPACT_MATRIX.md",
        "docs/TEST_CATALOG.md",
        "docs/TRACEABILITY.md",
    )
    if not os.path.exists(path)
]
if missing_files:
    print(f"Documentation governance files are missing: {', '.join(missing_files)}", file=sys.stderr)
    sys.exit(1)

print("Documentation check passed for changed source files.")
