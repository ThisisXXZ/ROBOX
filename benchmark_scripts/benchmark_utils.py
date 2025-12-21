from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent] + list(here.parents):
        if (parent / "requirements.txt").is_file() and (parent / "robox").is_dir():
            return parent
    raise RuntimeError("Could not find repo root from " + str(here))


def list_bddl_files():
    root = repo_root()
    bddl_root = root / "robox" / "robox" / "bddl_files"
    return sorted(bddl_root.rglob("*.bddl"))


def count_bddl_files() -> int:
    return len(list_bddl_files())


def list_image_paths():
    root = repo_root()
    image_dir = root / "images"
    return sorted([p for p in image_dir.iterdir() if p.is_file()])


def robox_config_path() -> Path:
    root = repo_root()
    return root / "robox" / "configs" / "config.yaml"