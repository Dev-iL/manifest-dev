"""Every check a harness project keeps is a recipe, the checks it runs across the whole tree
included, and every path that builds or audits a harness adopts them.

Holds the decision in docs/adr/20261015-every-check-a-harness-project-keeps-is-a-recipe.md. The
upgrade path used to move an older surface's user-reachable entries one for one and stop, so a
project's lint, types, tests and gate runner stayed outside its harness.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REFERENCES = (
    Path(__file__).resolve().parent.parent
    / "claude-plugins/manifest-dev/skills/setup-project/references"
)
SETUP = REFERENCES.parent / "SKILL.md"
GUIDES = sorted((REFERENCES / "upgrades").glob("v*-to-current.md"))

# Per file: the clause that has a run adopt the checks run across the whole tree.
ADOPTION = {
    REFERENCES
    / "VERIFICATION_HARNESS.md": (
        "adopted on every path that builds or audits a harness"
    ),
    SETUP: "a recipe for the checks the project runs across the whole tree",
    REFERENCES
    / "upgrades/MOVE_TO_HARNESS.md": (
        "The checks the project runs across the whole tree get a recipe too"
    ),
    **dict.fromkeys(GUIDES, "across the whole tree"),
}


def _text(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    ("path", "clause"), ADOPTION.items(), ids=[p.name for p in ADOPTION]
)
def test_every_path_that_builds_or_audits_a_harness_adopts_whole_tree_checks(
    path: Path, clause: str
) -> None:
    assert clause in _text(path), (
        f"{path.name} no longer has a run adopt the checks run across the whole tree "
        f"(expected: {clause!r})"
    )


def test_the_audit_counts_a_second_way_in_as_a_gap() -> None:
    assert (
        "each verification command the context file names that no recipe runs"
        in _text(SETUP)
    )


def test_an_example_recipe_shows_the_whole_tree_checks() -> None:
    recipe = REFERENCES / "harness/recipes/project-checks.md"
    assert recipe.exists(), "the shipped example of a whole-tree check recipe is gone"
    front = recipe.read_text(encoding="utf-8").split("---")[1]
    assert re.search(r"^kind: suite$", front, re.MULTILINE)
    assert re.search(r"^covers: \.$", front, re.MULTILINE)
    assert "ask-first" not in front
