# -*- coding: utf-8 -*-
#
#    assignment3.no1
#    Created by 25090335 Kohki Miki on 2011/07/20
#
import random
import math
from PIL import Image
N = 32

lena = Image.open("../../Resources/lena256.gif")
x = random.randint(0, 255-N)
y = random.randint(0, 255-N)
template = lena.crop((x, y, x+N, y+N))


#
template_sum = 0
for i in xrange(0, N):
    for j in xrange(0, N):
        template_sum += template.getpixel(i, j)
template_average = template_sum/(N**2)


def r(i, j):
    up = sum([[(lena.getpixel(i - N/2 + k, j - N/2 + l) - 0) * template.getpixel(k, l) - template_average for l in xrange(0, N)] for k in xrange(0, N)])