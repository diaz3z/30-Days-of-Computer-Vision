import  cv2

img = cv2.imread("public.jpg")
img = cv2.resize(img, (1080,720))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
img_thresh = cv2.blur(img_thresh, (7,7))
ret, img_thresh = cv2.threshold(img_thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("image", img)
cv2.imshow("Threshold Image", img_thresh)
cv2.waitKey(0)