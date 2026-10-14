"""The repository's feature map covers every feature it ships and points only at things that exist.

`docs/features/` tells an agent how a user reaches each feature and how to drive and check
it: one file per user-invocable skill, plus the design instruments. A map that misses a skill
cannot place a report about it, and an entry naming a file that moved sends the next run to
nothing. The file shape is the one setup-project's verification-surface reference defines, so
the section names are read from there rather than restated here.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MAP = REPO_ROOT / "docs" / "features"
INDEX = MAP / "README.md"
SURFACE_REFERENCE = (
    REPO_ROOT
    / "claude-plugins"
    / "manifest-dev"
    / "skills"
    / "setup-project"
    / "references"
    / "VERIFICATION_SURFACE.md"
)
# Features that are not skills: the map file name, and the paths that must exist for it.
NON_SKILL_FEATURES = {"design-instruments"}

INVOCABLE_FALSE = re.compile(r"^user-invocable:\s*false\s*$", re.MULTILINE)
STATUS = re.compile(
    r"^Status: (unverified"
    r"|verified \(\d{4}-\d{2}-\d{2}\)"
    r"|stale \(\d{4}-\d{2}-\d{2}\): .+"
    r"|unreachable \(\d{4}-\d{2}-\d{2}\): .+)$",
    re.MULTILINE,
)
INDEX_LINK = re.compile(r"\]\(\./([\w.-]+\.md)\)")
REPO_PATH = re.compile(r"`((?:claude-plugins|tests|scripts|docs|dist)/[^`\s<>*|]+)`")


def shipped_plugins() -> list[Path]:
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    return [REPO_ROOT / plugin["source"] for plugin in marketplace["plugins"]]


def user_invocable_skills() -> set[str]:
    found = set()
    for plugin in shipped_plugins():
        for skill in (plugin / "skills").glob("*/SKILL.md"):
            frontmatter = skill.read_text(encoding="utf-8").split("---", 2)[1]
            if not INVOCABLE_FALSE.search(frontmatter):
                found.add(skill.parent.name)
    return found


def required_sections() -> list[str]:
    """The feature-file sections, in order, as the verification-surface reference lists them."""
    text = SURFACE_REFERENCE.read_text(encoding="utf-8")
    block = text.split("**Each feature file**", 1)[1].split("\n\n", 2)[1]
    sections = re.findall(r"^\d+\. `([^`]+)`", block, re.MULTILINE)
    assert sections, f"{SURFACE_REFERENCE} lists no feature-file sections"
    return sections


def feature_files() -> list[Path]:
    return sorted(p for p in MAP.glob("*.md") if p != INDEX)


# Holds the decision in docs/adr/20261014-the-feature-map-is-a-navigation-contract-over-what-users-invoke.md.
def test_every_user_invocable_skill_has_an_entry() -> None:
    entries = {p.stem for p in feature_files()}
    missing = user_invocable_skills() - entries
    assert not missing, (
        f"{sorted(missing)} can be invoked but have no entry in {MAP.relative_to(REPO_ROOT)}; "
        "add one per the shape in the verification-surface reference"
    )
    unknown = entries - user_invocable_skills() - NON_SKILL_FEATURES
    assert not unknown, (
        f"{sorted(unknown)} in {MAP.relative_to(REPO_ROOT)} name no user-invocable skill; "
        "remove them, or list a deliberate non-skill feature in NON_SKILL_FEATURES"
    )


def test_index_lists_exactly_the_feature_files() -> None:
    linked = set(INDEX_LINK.findall(INDEX.read_text(encoding="utf-8")))
    on_disk = {p.name for p in feature_files()}
    assert linked == on_disk, (
        f"index and files disagree — linked only: {sorted(linked - on_disk)}; "
        f"on disk only: {sorted(on_disk - linked)}"
    )


# Holds the decision in docs/adr/20261014-the-feature-map-is-a-navigation-contract-over-what-users-invoke.md.
@pytest.mark.parametrize("entry", feature_files(), ids=lambda p: p.stem)
def test_entry_has_the_shape_and_a_status(entry: Path) -> None:
    text = entry.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+?)\s*$", text, re.MULTILINE)
    assert (
        headings == required_sections()
    ), f"{entry.name}: sections {headings}, expected {required_sections()} in that order"
    assert len(STATUS.findall(text)) == 1, (
        f"{entry.name}: needs exactly one `Status:` line — unverified, verified (date), "
        "stale (date): what differs, or unreachable (date): prerequisite"
    )


@pytest.mark.parametrize("entry", feature_files(), ids=lambda p: p.stem)
def test_entry_points_only_at_paths_that_exist(entry: Path) -> None:
    missing = [
        path
        for path in REPO_PATH.findall(entry.read_text(encoding="utf-8"))
        if not (REPO_ROOT / path.rstrip("/.,;")).exists()
    ]
    assert not missing, f"{entry.name} names paths that do not exist: {missing}"
