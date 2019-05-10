#encoding：utf-8
import numpy as np
import cv2
#   读 取 图 片
img = cv2.imread('/home/gzb/PycharmProjects/homework/data/b.png')  # 直接读为灰度图像
#   缩小图像10倍(因为我的图片太大，所以要缩小10倍方便看看效果)
height, width = img.shape[:2]
size = (int(width * 0.1), int(height * 0.1))  # bgr
img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
#BGR转化为HSV
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("imageHSV",HSV)
cv2.imshow('image',img)
color = [
    ([0, 80,0], [255, 100, 255])  ]
# 蓝色范围~这个是我自己试验的范围，可根据实际情况自行调整~注意：数值按[b,g,r]排布
# 如果color中定义了几种颜色区间，都可以分割出来
for (lower, upper) in color:
    # 创建NumPy数组
    lower = np.array(lower, dtype="uint8")  # 颜色下限
    upper = np.array(upper, dtype="uint8")  # 颜色上限
    # 根据阈值找到对应颜色
    mask = cv2.inRange(HSV, lower, upper)    #查找处于范围区间的
    mask = 255-mask                          #留下铝材区域
    output = cv2.bitwise_and(img, img, mask=mask)    #获取铝材区域
    #bgroutput = cv2.cvtColor(output,cv2.COLOR_HSV2BGR)
    # 展示图片
    cv2.imshow("images", np.hstack([img, output]))
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(mask.shape)
    #print(mask[0])
    print(len(contours))
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    for i in contours:
        print(cv2.contourArea(i))  # 计算缺陷区域面积
        x, y, w, h = cv2.boundingRect(i)  # 画矩形框
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
    #cv.imwrite(show_result_path, match_img_color)
    cv2.imshow("detect",img)
    cv2.imshow("chanle", img)
    cv2.waitKey(0)
cv2.waitKey(0)
