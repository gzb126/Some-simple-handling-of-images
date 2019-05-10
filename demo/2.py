#coding=utf-8

from PIL import Image

#灰度化
infile = '/home/gzb/PycharmProjects/homework/data/3.jpeg' #原始图像路径
outfile= '/home/gzb/PycharmProjects/homework/res/girl.jpg' #灰度化后的图像路径

im = Image.open(infile).convert('L') #灰度化
out = im.resize((400,400),Image.ANTIALIAS) #重新定义图片尺寸大小

out.save(outfile) #存储图片
