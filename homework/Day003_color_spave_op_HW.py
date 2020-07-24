import cv2
import numpy as np

#1 改變飽和度
#2 直方圖均衡
#3 調整對比/明亮

img = cv2.imread(r'C:\Users\pi\Desktop\50day\DL-CVMarathon\lena.png')
#1
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
change_percentage = 0.2
#2
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#3 調整對比
add_contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=0)
add_lighness = cv2.convertScaleAbs(img, alpha=1.0, beta=50)
# 改變飽和度
img_hsv_down = img_hsv.astype('float32')
img_hsv_down[..., -1] = img_hsv_down[..., -1]/255 - change_percentage
img_hsv_down[img_hsv_down[..., -1] < 0] = 0
img_hsv_down[..., -1] = img_hsv_down[..., -1]*255
img_hsv_down = img_hsv_down.astype('uint8')

img_hsv_up = img_hsv.astype('float32')
img_hsv_up[..., -1] = img_hsv_up[..., -1]/255 + change_percentage
img_hsv_up[img_hsv_up[..., -1] > 1] = 1
img_hsv_up[..., -1] = img_hsv_up[..., -1]*255
img_hsv_up = img_hsv_up.astype('uint8')
# 直方圖
img_gray_equal = cv2.equalizeHist(img_gray)
img_gray_equalHist = np.hstack((img_gray, img_gray_equal))

# 組合(對比)
img_contrast_light = np.hstack((img, add_contrast, add_lighness))

img_hsv_down = cv2.cvtColor(img_hsv_down, cv2.COLOR_HSV2BGR)
img_hsv_up = cv2.cvtColor(img_hsv_up, cv2.COLOR_HSV2BGR)

img_hsv_change = np.hstack((img, img_hsv_down, img_hsv_up))
# 飽和度
cv2.imshow('change saturation', img_hsv_change)
# 直方圖
cv2.imshow('gray equal histogram', img_gray_equalHist)
# 調整對比
cv2.imshow('adjust contrast and brighness', img_contrast_light)

cv2.waitKey(0)
cv2.destroyAllWindows()