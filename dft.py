# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread('pout.tif', 0)
# 使用numpy中的函数进行傅里叶变换
f = np.fft.fft2(img1)
fshift = np.fft.fftshift(f)
# 之所以要进行对数转换是因为傅里叶变换后的结果对于在显示器显示来讲范围比较大，这样的话对于一些小的变化或者是高的变换值不能进行观察
magnitude_spectrum=20*np.log(np.abs(fshift))
# 使用numpy中的函数进行傅里叶逆变换
f1 = np.fft.ifft2(magnitude_spectrum)
f1shift = np.fft.ifftshift(f1)
f1images = 20*np.log(np.abs(f1shift))
plt.subplot(2,2,1),plt.imshow(img1)
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(magnitude_spectrum)
plt.title('Fourier transform'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(f1images)
plt.title('Inverse Fourier Transform'),plt.xticks([]),plt.yticks([])
plt.show()