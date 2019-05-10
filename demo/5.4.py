
# coding=utf-8
# import Image ,ImageDraw
import  numpy as np
from PIL import Image
from PIL import ImageDraw
ret = {}
def twoValue(image ,G):
    for y in range(0 ,image.size[1]):
        for x in range(0 ,image.size[0]):
            g = image.getpixel((x ,y))
            if g > G:
                ret[(x ,y)] = 1
            else:
                ret[(x ,y)] = 0
def OtsuGray(image):
    hist = image.histogram()
    totalH = 0
    for h in range(0 ,256):
        v =hist[h]
        if v == 0: continue
        totalH += v * h
    width = image.size[0]
    height = image.size[1]
    total = width * height
    v = 0
    gMax = 0.0
    tIndex = 0
    total0 = 0.0
    total1 = 0.0
    n0H = 0.0
    n1H = 0.0
    for t in range(1, 255):
        v = hist[t - 1]
        if v == 0: continue
        total0 += v
        total1 = total - total0
        n0H += (t - 1) * v
        n1H = totalH - n0H
        if total0 > 0 and total1 > 0:
            u0 = n0H / total0
            u1 = n1H / total1
            w0 = total0 / total
            w1 = 1.0 - w0
            uD = u0 - u1
            g = w0 * w1 * uD * uD
            if gMax < g:
                gMax = g
                tIndex = t
    return tIndex


def saveImage(filename, size):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point((x, y), ret[(x, y)])
    image.save(filename)


def handle(filename, outputname):
    im = Image.open(filename)
    im = im.convert('L')
    otsu = OtsuGray(im)
    twoValue(im, otsu)
    saveImage(outputname, im.size)


if __name__ == '__main__':
    handle('/home/gzb/PycharmProjects/homework/data/b.png', '/home/gzb/PycharmProjects/homework/res/temp.jpg')

