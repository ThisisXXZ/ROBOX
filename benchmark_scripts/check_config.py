from __future__ import annotations

from hydra import compose, initialize_config_dir
from easydict import EasyDict
from future.utils import iteritems

from benchmark_utils import robox_config_path, count_bddl_files


def main() -> None:
    config_path = robox_config_path()
    config_dir = config_path.parent
    with initialize_config_dir(version_base=None, config_dir=str(config_dir)):
        cfg = compose(config_name=config_path.stem)

    summary = EasyDict()
    summary.bddl_files = count_bddl_files()
    summary.cfg_keys = len(cfg.keys())
    summary.bddl_folder = cfg.get("bddl_folder", None)

    parts = [f"{k}={v}" for k, v in iteritems(summary)]
    print("config_tooling: " + ", ".join(parts))


if __name__ == "__main__":
    main()