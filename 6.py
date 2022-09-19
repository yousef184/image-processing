import cv2
import numpy as np
import matplotlib.pyplot as plt
#lower hystersis threshold
tlower = 50
#upper hystersis threshold
tupper = 100
img1 = cv2.imread("ball.jpeg",0)
img1 = cv2.Canny(img1,tlower,tupper)
plt.imshow(img1, cmap='gray')
plt.show()
#The hysteresis mode uses a hysteresis loop to provide a more connected result
# . Any pixel above the upper threshold is turned white. The surround pixels are then searched recursively. 
# If the values are greater than the lower threshold they are also turned white. 
# The result is that there are many fewer specks of white in the resulting image.