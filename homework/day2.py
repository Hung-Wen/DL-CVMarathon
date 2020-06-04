import cv2

img = cv2.imread(r"C:\Users\pi\Desktop\50day\DL-CVMarathon\lena.png", cv2.IMREAD_COLOR)

hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow('img', img)
cv2.imshow('hsv', hsv)
cv2.imshow('hls', hls)
cv2.imshow('lab', lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
