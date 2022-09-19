import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("ball.jpeg",0)
kernel= np.array([
    [0, -0.25, 0],
    [-0.25, 2, -0.25],
    [0, -0.25, 0]
])
# filtered_img1= np.zeros_like(noisy_image)
filtered_img1= cv2.filter2D(img1,-1, kernel)
plt.imshow(filtered_img1, cmap='gray')
plt.show()