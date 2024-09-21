import cv2

img = cv2.imread("public.jpg")
img = cv2.resize(img, (1080,720))

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian = cv2.GaussianBlur(img, (k_size,k_size),5)
img_median = cv2.medianBlur(img, (k_size))
cv2.imshow("norhing", img)
cv2.imshow("blur", img_blur)
cv2.imshow("Gaussian blur", img_gaussian)
cv2.imshow("Median blur", img_median)
cv2.waitKey(0)