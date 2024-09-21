import cv2

img = cv2.imread("img.jpeg")

cropped_img = img[60:320, 40:240]
cv2.imshow("nothing", img)
cv2.imshow("jdlf", cropped_img)
cv2.waitKey(0)