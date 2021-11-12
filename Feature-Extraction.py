import cv2
import matplotlib.pyplot as plt
img = cv2.imread('/home/rjoker/DeepLearning/face_image.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)
cv2.imshow("Img",gray)
Rgray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
cv2.imshow("Img222",Rgray)
cv2.waitKey(0)