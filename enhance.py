import cv2
import numpy as np


def auto_gamma(image, target_mean=0.5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = float(np.clip(gray.mean() / 255.0, 0.01, 0.99))
    gamma = np.log(target_mean) / np.log(mean)
    return float(np.clip(gamma, 0.3, 3.0))


def apply_gamma(image, gamma):
    table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)])
    return cv2.LUT(image, table.astype("uint8"))


img = cv2.imread("samples/corridor.jpg")

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
l = clahe.apply(l)
out = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

out = apply_gamma(out, auto_gamma(out))
cv2.imwrite("output/corridor_enhanced.jpg", out)
