import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("cat1.jpeg",0)
img2 = cv2.imread("cat2.jpeg",0)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3)
plt.show()
#1- FLANN based Matcher gets the best results
#2- flann take the most time brute force with sift takes less and brute force with orb takes lesser time
#3- no matching appears