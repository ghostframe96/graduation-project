import cv2

img = cv2.imread("samples/corridor.jpg")

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
l = clahe.apply(l)

out = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)
cv2.imwrite("output/corridor_clahe.jpg", out)
