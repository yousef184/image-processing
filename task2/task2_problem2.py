#import opencv and numpy
import cv2  
import numpy as np

def display_img(img):
    window_name = 'image'
    cv2.imshow(window_name, img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

def extract_color(min_value:np.ndarray, max_value:np.ndarray, img, display=True):
    hsv_img= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv_img,min_value,max_value) ## 2D matrix
    if display:
        display_img(mask)
    extracted_img= cv2.bitwise_and(img,img,mask=mask)
    return extracted_img

#trackbar callback fucntion to update HSV value
def callback(x):
	global H_low,H_high,S_low,S_high,V_low,V_high
	#assign trackbar position value to H,S,V High and low variable
	H_low = cv2.getTrackbarPos('low H','controls')
	H_high = cv2.getTrackbarPos('high H','controls')
	S_low = cv2.getTrackbarPos('low S','controls')
	S_high = cv2.getTrackbarPos('high S','controls')
	V_low = cv2.getTrackbarPos('low V','controls')
	V_high = cv2.getTrackbarPos('high V','controls')


#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10)


#global variable
H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

#create trackbars for high,low H,S,V 
cv2.createTrackbar('low H','controls',0,179,callback)
cv2.createTrackbar('high H','controls',179,179,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)

cap= cv2.VideoCapture("timer.mp4")
while True:
    ret,img= cap.read()
#     img= cv2.resize(img, (360,360))
    hsv_low = np.array([H_low, S_low, V_low], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)
    cv2.imshow('Original',img)
    cv2.imshow('Green Extracted',extract_color(hsv_low,hsv_high,img, False))
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()    