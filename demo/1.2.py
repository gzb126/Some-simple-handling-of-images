from PIL import Image

from pylab import *

#读取图像到数组中，并灰度化
im = array(Image.open('/demo/gzb/PycharmProjects/homework/data/a.png').convert('L'))

print(im.shape)
#绘制原始直方图

subplot(231)

hist(im.flatten(),5)

#计算图像直方图（每个bins数组的区间值对应一个imhist数组中的强度值）
#该函数返回值imhist表示每个区间的强度，bins表示坐标轴
imhist,bins = histogram(im.flatten(),5,normed=True)
print(imhist.shape)
print(imhist.sum())
print(bins.shape)
print("imhist：",imhist)
print("bins：",bins)


#计算累积分布函数
#概率分布的积分
cdf = imhist.cumsum()

print("cdf：",cdf[-1])

#累计函数归一化（由0～1变换至0~255）
cdf = cdf*255/cdf[-1]

#绘制累计分布函数
subplot(232)

plot(bins[1:6],cdf)
#依次对每一个灰度图像素值（强度值）使用cdf进行线性插值，计算其新的强度值

#interp（x，xp，yp） 输入原函数的一系列点（xp，yp），使用线性插值方法模拟函数并根据这个函数计算f（x）
im2 = interp(im.flatten(), bins[:5], cdf)

#将压平的图像数组重新变成二维数组
im2 = im2.reshape(im.shape)

# 显示均衡化之后的直方图图像
subplot(233)

hist(im2.flatten(),5)

#显示原始图像
gray()

subplot(234)

imshow(im)

#显示变换后图像
subplot(236)

imshow(im2)
show()