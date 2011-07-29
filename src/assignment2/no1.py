# -*- coding: utf-8 -*-
#
#    assignment2.no1
#    Created by 25090335 Kohki Miki on 2011/07/20
#
import numpy
import random
import math

N = 2000

class Perceptron(object):
    def __init__(self, x):
        self.x = x
        n = N
        self.j_star = numpy.matrix([1/math.sqrt(n)] * n)
        self.y = self._sgn(self.j_star * x.T)
    
    @staticmethod
    def _sgn(x):
        return 1 if x > 0 else -1
    
    def j(self, n):
        if self.js[n] is None:
            self.js[n] = self.j(n - 1) + self.y * self.x
        self.js[n] = self.js[n] / numpy.linalg.norm(self.js[n])
        return self.js[n]
    
    def epsilon(self, n):
        self.js = [None] * (n + 1)
        self.js[0] = self.j_star
        jn = self.j(0)
        for i in xrange(0, n):
            jn = self.j(i)
        # 100回食い違いを測定する
        e = 0
        for i in xrange(0, 100):
            x = numpy.matrix([random.random() * 2 - 1 for i in xrange(N)])
            x /= numpy.linalg.norm(x)
            a = self._sgn(jn * x.T)
            b = self._sgn(self.j_star * x.T)
            if a != b: e += 1
        return e

x = numpy.matrix([random.random() * 2 - 1 for i in xrange(N)])
x /= numpy.linalg.norm(x)
test = Perceptron(x)
for n in xrange(0, 100):
    sum = 0.0
    for i in xrange(0, 10):
        sum += test.epsilon(n)
    print n, sum/10.0