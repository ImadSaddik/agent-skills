#!/usr/bin/env python3
import sys
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"

TARGET_AGENT_DIRS = [
    Path.home() / ".gemini" / "antigravity-cli" / "skills",
    Path.home() / ".claude" / "skills",
    Path.home() / ".agents" / "skills",
    Path.home() / ".cursor" / "skills",
]

GREEN = "\033[32m"
CYAN = "\033[36m"
DIM = "\033[2m"
RESET = "\033[0m"
BOLD = "\033[1m"


class LinkResult(NamedTuple):
    skill: str
    path: Path
    status: str


def link_skills() -> list[LinkResult]:
    if not SKILLS_DIR.exists():
        print(f"Skills directory not found at: {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)

    results: list[LinkResult] = []

    for skill_path in sorted(SKILLS_DIR.iterdir()):
        if not skill_path.is_dir() or not (skill_path / "SKILL.md").exists():
            continue

        for target_parent in TARGET_AGENT_DIRS:
            target_parent.mkdir(parents=True, exist_ok=True)
            link_destination = target_parent / skill_path.name

            if link_destination.is_symlink() or link_destination.exists():
                link_destination.unlink()

            link_destination.symlink_to(skill_path, target_is_directory=True)
            results.append(
                LinkResult(
                    skill=skill_path.name,
                    path=link_destination,
                    status="Linked",
                )
            )

    return results


def display_results(results: list[LinkResult]) -> None:
    print(f"\n{BOLD}{CYAN}Agent skills symlink status{RESET}\n")
    print(f"{BOLD}{'Skill':<16} {'Status':<10} {'Agent path'}{RESET}")
    print("-" * 75)

    for item in results:
        print(
            f"{BOLD}{item.skill:<16}{RESET} {GREEN}{item.status:<10}{RESET} {DIM}{item.path}{RESET}"
        )

    print()


if __name__ == "__main__":
    links = link_skills()
    display_results(links)
