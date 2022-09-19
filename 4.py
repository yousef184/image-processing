import cv2
import numpy as np
import matplotlib.pyplot as plt
image = np.array([[255,170],[10,50]])
image[image<127] = 0
print(image)