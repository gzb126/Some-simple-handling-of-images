
# Referrence Link:https://pywavelets.readthedocs.io/en/latest/regression/wp2d.html
# can expanded to other type of wavelet.
# you can use in cmd line with: python wavelets_transfer.py --image image.jpg
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import argparse
import imutils
import cv2
from datetime import datetime
import numpy as np
import pywt


def wavelete_packet2D(img_name):
    img = np.array(Image.open(img_name).convert('L'))
    rows, cols = img.shape
    plt.figure(img_name)
    plt.imshow(img, cmap='gray')
    # plt.axis('off')
    plt.show()  # show the original image

    # use 2D wavelete db1 mode='symmetric'
    wp = pywt.WaveletPacket2D(data=img, wavelet='db2', mode='symmetric')

    # show a - LL, low-low coefficients
    plt.imshow((wp['a'].data), cmap='gray')
    plt.show()

    # show h - LH, low-high coefficients
    plt.imshow((wp['h'].data), cmap='gray')
    plt.show()

    # show v - HL, high-low coefficients
    plt.imshow((wp['v'].data), cmap='gray')
    plt.show()

    # show d - HH, high-high coefficients
    plt.imshow((wp['d'].data), cmap='gray')
    plt.show()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    args = vars(ap.parse_args())
    # image = cv2.imread(args["image"])
    t1 = datetime.now()
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    wavelete_packet2D(args["image"])
    print(datetime.now() - t1)



####   https://blog.csdn.net/leemboy/article/details/84669369