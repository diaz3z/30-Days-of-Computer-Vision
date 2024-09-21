import cv2

img = cv2.imread("img.jpeg")

resized_img = cv2.resize(img, (640,480))

print(img.shape)
print(resized_img.shape)

cv2.imshow("Original Image", img)

cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)