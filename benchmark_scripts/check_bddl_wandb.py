from dataclasses import dataclass
from importlib.metadata import version

import wandb
from transformers import HfArgumentParser

from benchmark_utils import count_bddl_files


@dataclass
class Args:
    task: str
    bddl_count: int


def main() -> None:
    bddl_count = count_bddl_files()

    parser = HfArgumentParser(Args)
    args = parser.parse_args_into_dataclasses(
        ["--task", "robox", "--bddl_count", str(bddl_count)]
    )[0]

    run = wandb.init(project="robox_benchmark", mode="disabled")
    run.log({"bddl_file_count": bddl_count})
    run.summary["bddl_version"] = version("bddl")
    run.finish()

    print(
        "bddl_transformers_wandb: task={} bddl_count={} bddl_version={}".format(
            args.task, args.bddl_count, version("bddl")
        )
    )


if __name__ == "__main__":
    main()
