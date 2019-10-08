import cv2
import numpy as np
# 读入一个图像文件
img = cv2.imread('11.png')
# 把两个图像相加
img2 = cv2.add(img, img)
# 显示图片
cv2.imshow('img', img)
cv2.imshow('img2', img2)
# 当按下键盘是关闭所有的图像
cv2.waitKey(0)
cv2.destroyAllWindows()


