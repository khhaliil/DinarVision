import cv2
import numpy as np

################################
tolerance_th = 0.85 #tolerance mtaa el matching
################################

img= cv2.imread(r"C:\Users\MSI\Desktop\20.png")
img2 = cv2.imread(r"C:\Users\MSI\Desktop\22.jpg")

orb =cv2.ORB_create(nfeatures=1000) #fast and free

kp1,des1=orb.detectAndCompute(img,None)
kp2,des2=orb.detectAndCompute(img2,None)
#print(kp1)

imgkp = cv2.drawKeypoints(img,kp1,None,color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
imgkp2 = cv2.drawKeypoints(img2,kp2,None,color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []

for m,n in matches:
    if m.distance < tolerance_th*n.distance :
        good.append([m])

img3= cv2.drawMatchesKnn(img,kp1,img2,kp2,good,None,flags=2)

cv2.imshow("detect",imgkp)
cv2.imshow("detect2",imgkp2)
cv2.imshow("res",img3)

cv2.waitKey(0)

