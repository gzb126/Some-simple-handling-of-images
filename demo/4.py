
import cv2
import numpy as np
original_img = cv2.imread('/home/gzb/PycharmProjects/homework/data/4.1.jpeg')
res = cv2.resize(original_img,None,fx=0.6, fy=0.6,
                 interpolation = cv2.INTER_CUBIC) #图形太大了缩小一点
B, G, R = cv2.split(res)                    #获取红色通道
img = R
_,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
#OpenCV定义的结构矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
eroded = cv2.erode(RedThresh,kernel)        #腐蚀图像
dilated = cv2.dilate(RedThresh,kernel)      #膨胀图像

cv2.imshow("original_img", res)             #原图像
cv2.imshow("Eroded Image",eroded)           #显示腐蚀后的图像
cv2.imshow("Dilated Image",dilated)         #显示膨胀后的图像

# #NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(RedThresh,NpKernel)       #腐蚀图像
#   cv2.imshow("Eroded by NumPy kernel",Nperoded)  #显示腐蚀后的图像
cv2.waitKey(0)
cv2.destroyAllWindows()
