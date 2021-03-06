import cv2
import numpy

image = cv2.imread("/home/gzb/PycharmProjects/homework/data/girl.jpg",cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))   ##膨胀压缩的像素范围
dilate_img = cv2.dilate(image, kernel)
erode_img = cv2.erode(image, kernel)
"""
我选了一张较好的图片，有的图片要去噪（高斯模糊）
将两幅图像相减获得边；cv2.absdiff参数：(膨胀后的图像，腐蚀后的图像)
上面得到的结果是灰度图，将其二值化以便观察结果
反色，对二值图每个像素取反
"""
absdiff_img = cv2.absdiff(dilate_img,erode_img);
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY);
result = cv2.bitwise_not(threshold_img);

cv2.imshow("yuantu",image)
cv2.imshow("dilate_img",dilate_img)
cv2.imshow("erode_img",erode_img)
cv2.imshow("absdiff_img",absdiff_img)
cv2.imshow("threshold_img",threshold_img)
cv2.imshow("result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
