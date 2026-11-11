# Documentation policy

Docs are part of the change, not a follow-up. `scripts/check_docs_changes.py`
runs in CI (`.github/workflows/docs-check.yml`) on every pull request and
fails the build if a change touches code without touching the doc that
describes it. See `docs/CHANGE_IMPACT_MATRIX.md` for exactly which code
path requires which doc.

If a change is genuinely non-behavioral (a comment, a formatting pass, a
dependency bump with no observable effect), label the PR
`docs-not-required` and say why in the PR description -- the gate does not
currently read PR labels itself, so this is a human override recorded for
reviewers, not a bypass the script honors automatically.

## A repo's first commit is exempt

`scripts/check_docs_changes.py` diffs against `HEAD^`, which does not exist
on a repository's root commit -- the gate correctly fails closed (exit 2,
"could not compare") rather than silently passing. This is a one-time
bootstrap gap, not a bypass: every commit after the first has a `HEAD^` to
diff against, and the gate applies normally from the second commit onward.

## Why centralized, not per-module

`docs/MODULE_CATALOG.md` holds every module's section in one file, not a
`README.md` per `src/pages/<area>/` folder. A per-module README was tried
in an earlier sibling project and reverted once it became clear nothing
about Selenium/behave's layer-first structure actually needs it --
`core-pw-e2e-tests`' own convention is one catalog, and this repo matches
it for the same reason: one file to search, one file to keep current, no
risk of a module's README silently drifting out of sync with its code
while nobody notices because nobody opens that folder.
