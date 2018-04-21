"""
Low-light photo enhancement using CLAHE + automatic gamma correction.
Graduation Project - B.Sc. Computer Science (2018)
"""
import argparse

import cv2
import numpy as np


def auto_gamma(image, target_mean=0.5):
    """Pick a gamma value that pushes the mean brightness toward target_mean."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = float(np.clip(gray.mean() / 255.0, 0.01, 0.99))
    gamma = np.log(target_mean) / np.log(mean)
    return float(np.clip(gamma, 0.3, 3.0))


def apply_gamma(image, gamma):
    """Apply gamma correction with a lookup table (fast, 256 values)."""
    table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)])
    return cv2.LUT(image, table.astype("uint8"))


def enhance(image, clip_limit=2.0, grid_size=8):
    """CLAHE on the L channel only (keeps colors stable), then auto gamma."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(grid_size, grid_size))
    l = clahe.apply(l)
    merged = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)
    return apply_gamma(merged, auto_gamma(merged))


def main():
    parser = argparse.ArgumentParser(description="Brighten underexposed photos.")
    parser.add_argument("input", help="path to the dark photo")
    parser.add_argument("output", help="where to save the enhanced photo")
    parser.add_argument("--clip", type=float, default=2.0, help="CLAHE clip limit")
    parser.add_argument("--grid", type=int, default=8, help="CLAHE tile grid size")
    args = parser.parse_args()

    image = cv2.imread(args.input)
    if image is None:
        raise SystemExit(f"Could not read {args.input}")

    result = enhance(image, args.clip, args.grid)
    cv2.imwrite(args.output, result)
    print(f"Saved enhanced image to {args.output}")


if __name__ == "__main__":
    main()
