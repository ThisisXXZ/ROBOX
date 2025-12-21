import cloudpickle
import numpy as np
from einops import rearrange

from benchmark_utils import list_bddl_files


def main() -> None:
    files = list_bddl_files()
    if not files:
        raise RuntimeError("No BDDL files found")

    name_lengths = np.array([len(p.name) for p in files], dtype=np.int32)
    arr = np.arange(name_lengths.size * 2).reshape(name_lengths.size, 2)
    rearranged = rearrange(arr, "n c -> c n")
    payload = cloudpickle.dumps(rearranged)

    print(
        "data_stats: count={} min={} max={} mean={:.2f} pickle_bytes={}".format(
            name_lengths.size,
            int(name_lengths.min()),
            int(name_lengths.max()),
            float(name_lengths.mean()),
            len(payload),
        )
    )


if __name__ == "__main__":
    main()