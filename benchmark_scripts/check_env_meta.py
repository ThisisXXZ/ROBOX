from importlib.metadata import version

import gym
from gym import spaces

from benchmark_utils import repo_root


def main() -> None:
    env_dir = repo_root() / "robox" / "robox" / "envs"
    env_count = len([p for p in env_dir.iterdir() if p.is_dir()])
    space = spaces.Dict(
        {
            "task_id": spaces.Discrete(max(1, env_count)),
            "stage": spaces.Discrete(3),
        }
    )
    sample = space.sample()

    print(
        "env_meta: robosuite={} robomimic={} thop={} gym_task_id={}".format(
            version("robosuite"),
            version("robomimic"),
            version("thop"),
            sample["task_id"],
        )
    )


if __name__ == "__main__":
    main()