from PIL import Image
from pylab import *
from numpy import *


def histeq(im,nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    #计算图像的直方图
    #在numpy中，也提供了一个计算直方图的函数histogram(),第一个返回的是直方图的统计量，第二个为每个bins的中间值
    imhist,bins = histogram(im.flatten(),nbr_bins,normed= True)
    cdf = imhist.cumsum()   #
    cdf = 255.0 * cdf / cdf[-1]               #累 计函数归一化（由0～1变换至0~255）
    #使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    #interp（x，xp，yp） 输入原函数的一系列点（xp，yp），使用线性插值方法模拟函数并根据这个函数计算f（x）
    return im2.reshape(im.shape),cdf


pil_im = Image.open('/home/gzb/PycharmProjects/homework/data/a.png')   #打开原图
pil_im_gray = pil_im.convert('L')     #转化为灰度图像
pil_im_gray.show()         #显示灰度图像

im = array(Image.open('/home/gzb/PycharmProjects/homework/data/a.png').convert('L'))
figure()
hist(im.flatten(),256)      # 原图

im2,cdf = histeq(im)
figure()
hist(im2.flatten(),256)
show()                 #增强后的

im2 = Image.fromarray(uint8(im2))
im2.show()
im2.save("/home/gzb/PycharmProjects/homework/res/1_res.png")  # 保存增强后的图