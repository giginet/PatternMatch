# -*- coding: utf-8 -*-
#
#    assignment3.no1
#    Created by 25090335 Kohki Miki on 2011/07/20
#
import random
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
        return a/numpy.sqrt(b*c)
    
    def search(self, template):
        self.template = template
        self.template_average = numpy.mean(list(self.template.getdata()))
        rs = [self._r(12+i%(N-M), 12+i/(N-M)) for i in xrange((((N-M)**2)))]
        m = max(rs)
        max_point = rs.index(m)
        return max_point%(N-M)+12, max_point/(N-M)+12

if __name__ == '__main__':
    # Lena画像を読み込む
    match = Match("../../Resources/lena256.gif")
    # テンプレート画像を生成
    #　左端の点を選ぶ
    tx = random.randint(0, N-M)
    ty = random.randint(0, N-M)
    # ランダムに選んだ点の中央点を出力
    print tx + M/2, ty + M/2 
    template = match.lena.crop((tx, ty, tx+M, ty+M))
    template.show()
    # テンプレート画像が元画像のどこの部分かを判定
    print match.search(template)
