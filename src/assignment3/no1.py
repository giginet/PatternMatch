# -*- coding: utf-8 -*-
#
#    assignment3.no1
#    Created by 25090335 Kohki Miki on 2011/07/20
#
import random
import math
import numpy
from PIL import Image
M = 25
N = 256

class Match(object):
    cache_g = [[None for i in xrange(0, N)] for i in xrange(0, N)]
    rs = [[None for i in xrange(0, N)] for i in xrange(0, N)]
    
    def __init__(self, filename):
        self.lena = Image.open(filename)
    
    def _g(self, i, j):
        m2 = int(M/2)
        if not self.cache_g[i][j]:
            self.cache_g[i][j] = numpy.mean([[self.lena.getpixel((x, y)) for x in xrange(max(0, i - m2), min(i + m2 + 1, N))] for y in xrange(max(0, j - m2), min(j + m2 + 1, N))])
        return self.cache_g[i][j]

    def _r(self, i, j):
        a = numpy.sum([[(self.lena.getpixel((i - int(M/2) + k, j - int(M/2) + l)) - self._g(i, j)) * (self.template.getpixel((k, l)) - self.template_average) for l in xrange(0, M)] for k in xrange(0, M)])
        b = numpy.sum([[(self.lena.getpixel((i - int(M/2) + k, j - int(M/2) + l)) - self._g(i, j))**2 for l in xrange(0, M)] for k in xrange(0, M)])
        c = numpy.sum([[(self.template.getpixel((k, l)) - self.template_average)**2 for l in xrange(0, M)] for k in xrange(0, M)])
        return a/math.sqrt(b*c)
    
    def search(self, template):
        self.template = template
        self.template_average = numpy.mean([[self.template.getpixel((x, y)) for x in xrange(0, M)] for y in xrange(0, M)])
        max = -1000000
        max_point = (0, 0)
        for x in xrange(12, N-12):
            for y in xrange(12, N-12):
                r = self._r(x, y)
                if r > max:
                    max = r
                    max_point = (x, y)
        return max_point

# Lena画像を読み込む
match = Match("../../Resources/lena256.gif")
# テンプレート画像を生成
tx = random.randint(0, N-M)
ty = random.randint(0, N-M)
template = match.lena.crop((tx, ty, tx+M, ty+M))
# テンプレート画像が元画像のどこの部分かを判定
print match.search(template)