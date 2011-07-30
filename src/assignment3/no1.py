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
        tx = random.randint(0, N-M)
        ty = random.randint(0, N-M)
        self.template = self.lena.crop((tx, ty, tx+M, ty+M))
        self.template_average = numpy.mean([[self.template.getpixel((x, y)) for x in xrange(0, M)] for y in xrange(0, M)])
    
    def g(self, i, j):
        m2 = int(M/2)
        if not self.cache_g[i][j]:
            self.cache_g[i][j] = numpy.mean([[self.lena.getpixel((x, y)) for x in xrange(max(0, i - m2), min(i + m2 + 1, N))] for y in xrange(max(0, j - m2), min(j + m2 + 1, N))])
        return self.cache_g[i][j]

    def r(self, i, j):
        a = numpy.sum([[(self.lena.getpixel((i - int(M/2) + k, j - int(M/2) + l)) - self.g(i, j)) * (self.template.getpixel((k, l)) - self.template_average) for l in xrange(0, M)] for k in xrange(0, M)])
        b = numpy.sum([[(self.lena.getpixel((i - int(M/2) + k, j - int(M/2) + l)) - self.g(i, j))**2 for l in xrange(0, M)] for k in xrange(0, M)])
        c = numpy.sum([[(self.template.getpixel((k, l)) - self.template_average)**2 for l in xrange(0, M)] for k in xrange(0, M)])
        return a/math.sqrt(b*c)
    
    def search(self):
        max = -1000000
        max_point = (0, 0)
        for x in xrange(12, N-12):
            for y in xrange(12, N-12):
                r = self.r(x, y)
                if r > max:
                    max = r
                    max_point = (x, y)
        print max_point

match = Match("../../Resources/lena256.gif")
match.search()