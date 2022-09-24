from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bear1.jpeg",0)
window_name = 'image'
cv2.imshow(window_name, img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 