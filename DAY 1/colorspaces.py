import cv2

img = cv2.imread("img.jpeg")

img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("nnothing", img)
cv2.imshow("RGB", img_color)
cv2.waitKey(0)