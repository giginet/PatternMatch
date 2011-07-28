# -*- coding: utf-8 -*-
#
#     assignment3.no1
#    Created by 25090335 Kohki Miki on 2011/07/20
#
import random
from PIL import Image
N = 32

lena = Image.open("../../Resources/lena256.gif")
print lena.getpixel((0, 0))
x = random.randint(0, 255-N)
y = random.randint(0, 255-N)
part = lena.crop((x, y, x+N, y+N))
