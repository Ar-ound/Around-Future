import cv2

im = cv2.imread("..\001.jpeg",1)

print(type(im))


cv2.waitKey()

cv2.destroyAllWindows()
