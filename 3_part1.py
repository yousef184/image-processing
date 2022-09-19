import cv2
import numpy as np
import matplotlib.pyplot as plt
img3 = cv2.imread("cat1.jpeg",0)
img3 = cv2.resize(img3, (183, 276)) 
img4 = cv2.imread("cat2.jpeg",0)
img4 = cv2.resize(img4, (183, 276)) 
img1 = cv2.imread("ball.jpeg",0)
img1 = cv2.resize(img1, (183, 276)) 
img2 = cv2.imread("boat1.jpeg",0)
img2 = cv2.resize(img2, (183, 276))
img12 = cv2.hconcat([img1,img2])
img34 = cv2.hconcat([img3,img4])
imgT = cv2.vconcat([img12,img34])
imgT = cv2.resize(imgT, (200, 200)) 
plt.imshow(imgT, cmap='gray')
plt.show()