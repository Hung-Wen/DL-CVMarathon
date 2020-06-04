import cv2

img = cv2.imread(r"C:\Users\pi\Desktop\50day\lena.png", cv2.IMREAD_COLOR)

img_GRAY = cv2.imread(r"C:\Users\pi\Desktop\50day\lena.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)
cv2.imshow('img_GRAY', img_GRAY)

cv2.waitKey(0)
cv2.destroyAllWindows()
