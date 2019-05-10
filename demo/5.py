import cv2
import numpy as np

#############

# 绿色
lower_green = np.array([35, 43, 46])
upper_green = np.array([77, 255, 255])

###################
img = cv2.imread('/home/gzb/PycharmProjects/homework/data/b.png')

# get a frame and show

frame = img

cv2.imshow('Capture', frame)        ######显示原图

# change to hsv model
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow('Mask', mask)       ######提取目的颜色图的黑白轮廓
# detect green
res = cv2.bitwise_and(frame, frame, mask=mask)
cv2.imshow('Result', res)       ####显示提取的绿色图片


cv2.waitKey(0)
cv2.destroyAllWindows()