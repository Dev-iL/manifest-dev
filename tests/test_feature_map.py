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
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MAP = REPO_ROOT / "docs" / "features"
INDEX = MAP / "README.md"
DRIVE = REPO_ROOT / "scripts" / "features" / "drive.sh"
SURFACE_REFERENCE = (
    REPO_ROOT
    / "claude-plugins"
    / "manifest-dev"
    / "skills"
    / "setup-project"
    / "references"
    / "VERIFICATION_SURFACE.md"
)
# Map entries that are not skills, by file name. `drive.sh` skips its skill-loaded check for
# the same names.
NON_SKILL_FEATURES = {"design-instruments"}

INVOCABLE_FALSE = re.compile(r"^user-invocable:\s*false\s*$", re.MULTILINE)
STATUS = re.compile(
    r"^Status: (unverified"
    r"|verified \(\d{4}-\d{2}-\d{2}\)(?:; not driven: .+)?"
    r"|stale \(\d{4}-\d{2}-\d{2}\): .+"
    r"|unreachable \(\d{4}-\d{2}-\d{2}\): .+)$",
    re.MULTILINE,
)
INDEX_LINK = re.compile(r"\]\(\./([\w.-]+\.md)\)")
CODE_SPAN = re.compile(r"`([^`\n]+)`")
REPO_ROOTS = ("claude-plugins/", "tests/", "scripts/", "docs/", "dist/")


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


def repo_paths(text: str) -> list[str]:
    """Every repository path named in a code span, including inside a command."""
    paths = []
    for span in CODE_SPAN.findall(text):
        for token in span.split():
            token = token.strip("\"'()<>,;.")
            if token.startswith(REPO_ROOTS) and not re.search(r"[<>*|{}$]", token):
                paths.append(token.rstrip("/"))
    return paths


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


# Holds the decision in docs/adr/20261014-the-feature-map-is-a-navigation-contract-over-what-users-invoke.md.
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
    statuses = list(STATUS.finditer(text))
    assert len(statuses) == 1, (
        f"{entry.name}: needs exactly one `Status:` line — unverified, verified (date), "
        "stale (date): what differs, or unreachable (date): prerequisite; a verified line names "
        "any entry point the drive did not use after `; not driven:`"
    )
    first_section = text.index("\n## ")
    assert (
        statuses[0].start() < first_section
    ), f"{entry.name}: the `Status:` line belongs before the first section"


# Holds the decision in docs/adr/20261014-the-feature-map-is-a-navigation-contract-over-what-users-invoke.md.
@pytest.mark.parametrize("page", [INDEX, *feature_files()], ids=lambda p: p.stem)
def test_page_points_only_at_paths_that_exist(page: Path) -> None:
    missing = [
        path
        for path in repo_paths(page.read_text(encoding="utf-8"))
        if not (REPO_ROOT / path).exists()
    ]
    assert not missing, f"{page.name} names paths that do not exist: {missing}"


def test_path_check_sees_paths_inside_commands() -> None:
    found = repo_paths(
        "Run `scripts/features/drive.sh x <p> --scaffold docs/missing-case`."
    )
    assert found == ["scripts/features/drive.sh", "docs/missing-case"]


def test_drive_harness_parses() -> None:
    # The harness's own checks: a broken drive.sh fails here, not in the first run that needs it.
    result = subprocess.run(["bash", "-n", str(DRIVE)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_drive_harness_dry_run_starts_nothing() -> None:
    result = subprocess.run(
        [str(DRIVE), "figure-out", str(INDEX), "--dry-run"],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin", "HOME": "/nonexistent-home"},
    )
    assert result.returncode == 0, result.stderr
    assert "docs/features/evidence/figure-out/" in result.stdout


def test_drive_harness_refuses_a_feature_with_no_entry() -> None:
    result = subprocess.run(
        [str(DRIVE), "no-such-feature", str(INDEX), "--dry-run"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0 and "no entry" in result.stderr


def test_drive_harness_never_reuses_an_evidence_directory(tmp_path: Path) -> None:
    # Two drives of one feature started in the same second once shared a directory and
    # interleaved their transcripts. Start two at once with the stamp pinned and a stub `docker`
    # that does nothing, and require two distinct evidence directories.
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    stub = bin_dir / "docker"
    stub.write_text("#!/bin/sh\nexit 0\n")
    stub.chmod(0o755)
    store = tmp_path / "store"
    env = {
        "PATH": f"{bin_dir}:/usr/bin:/bin",
        "HOME": str(tmp_path),
        "ANTHROPIC_API_KEY": "test-key",
        "MANIFEST_DEV_FEATURES_EVIDENCE": str(store),
        "DRIVE_STAMP": "20990101T000000Z",
    }
    drives = [
        subprocess.Popen(
            [str(DRIVE), "figure-out", str(INDEX)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(2)
    ]
    for drive in drives:
        try:
            drive.communicate(timeout=60)
        finally:
            drive.kill()
    made = sorted(p.name for p in (store / "figure-out").iterdir())
    assert made == ["20990101T000000Z", "20990101T000000Z-2"], made


def test_drive_harness_fails_fast_when_it_cannot_create_evidence(
    tmp_path: Path,
) -> None:
    # Only "another drive holds this directory" may be retried; any other failure stops loudly.
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    stub = bin_dir / "docker"
    stub.write_text("#!/bin/sh\nexit 0\n")
    stub.chmod(0o755)
    store = tmp_path / "store"
    (store / "figure-out").mkdir(parents=True)
    (store / "figure-out").chmod(0o555)
    try:
        result = subprocess.run(
            [str(DRIVE), "figure-out", str(INDEX)],
            env={
                "PATH": f"{bin_dir}:/usr/bin:/bin",
                "HOME": str(tmp_path),
                "ANTHROPIC_API_KEY": "test-key",
                "MANIFEST_DEV_FEATURES_EVIDENCE": str(store),
                "DRIVE_STAMP": "20990101T000000Z",
            },
            capture_output=True,
            text=True,
            timeout=30,
        )
    finally:
        (store / "figure-out").chmod(0o755)
    assert result.returncode != 0 and "cannot create" in result.stderr, result.stderr
