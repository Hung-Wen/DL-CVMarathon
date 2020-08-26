# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time
img = cv2.imread(r'C:\Users\pi\Desktop\50day\DL-CVMarathon\lena.png')

#翻轉
img_vflip = img[::-1, :, :]
# 水平 + 垂直翻轉
img_hvflip = np.vstack((img, img_vflip))
new_img = img_hvflip[:,::-1, :]
# 組合 + 顯示圖片
hflip = np.hstack((img_hvflip, new_img))

# 縮放
img_test = cv2.resize(img, None, fx=0.2, fy=0.2)
fx, fy = 8, 8
start_time = time.time()
img_area_scale = cv2.resize(img_test, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
print('INTER_NEAREST zoom cost {}'.format(time.time() - start_time))
orig_img = cv2.resize(img, img_area_scale.shape[:2])
img_zoom = np.hstack((orig_img, img_area_scale))

#平移
M = np.array([[1, 0, 100], [0, 1, 50]], dtype=np.float32)
shift_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
img_shift = np.hstack((img, shift_img))

#翻轉
cv2.imshow('hflip', hflip)
#縮放
cv2.imshow('zoom image', img_zoom)
#平移
cv2.imshow('shift image', img_shift)


cv2.waitKey(0)
cv2.destroyAllWindows()
