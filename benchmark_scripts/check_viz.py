import io

import cv2
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from benchmark_utils import list_image_paths, list_bddl_files


def main() -> None:
    images = list_image_paths()
    if not images:
        raise RuntimeError("No images found")

    img = cv2.imread(str(images[0]))
    if img is None:
        raise RuntimeError(f"Failed to read image: {images[0]}")

    lengths = [len(p.name) for p in list_bddl_files()]
    if not lengths:
        raise RuntimeError("No BDDL files found")

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(lengths[:20], marker="o")
    ax.set_title("ROBOX BDDL name lengths")
    ax.set_xlabel("index")
    ax.set_ylabel("length")

    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)

    mean_bgr = img.mean(axis=(0, 1))
    print(
        "viz: png_bytes={} mean_bgr=({:.1f},{:.1f},{:.1f})".format(
            buf.tell(), mean_bgr[0], mean_bgr[1], mean_bgr[2]
        )
    )


if __name__ == "__main__":
    main()