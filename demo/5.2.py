# --coding: utf-8--
import cv2 as cv
import numpy as np


def color_seperate(image):
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)   #对目标图像进行色彩空间转换
        lower_hsv = np.array([50, 100, 150])          #设定蓝色下限
        upper_hsv = np.array([124, 255, 255])        #设定蓝色上限
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  #依据设定的上下限对目标图像进行二值化转换
        dst = cv.bitwise_and(src, src, mask=mask)    #将二值化图像与原图进行“与”操作；实际是提取前两个frame 的“与”结果，然后输出mask 为1的部分
                                                     #注意：括号中要写mask=xxx
        cv.imshow('result', dst)                     #输出


src = cv.imread('/home/gzb/PycharmProjects/homework/data/b.png')   #导入目标图像，获取图像信息
color_seperate(src)
cv.imshow('image', src)
cv.waitKey(0)

cv.destroyAllWindows()
