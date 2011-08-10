# -*- coding: utf-8 -*-
#    
#    assignment5.no1
#    created by 25090335 Kohki Miki on 2011/08/10
#
import math
import numpy
from PIL import Image
from matplotlib import pyplot
from scipy.optimize import leastsq

from assignment4.no1 import DensityDistribution

class GaussianFitting(object):
    def gaussian(self, params, x):
        a, m1, m2, s1, s2 = params
        p = a/numpy.sqrt(2*numpy.pi*s1**2)*numpy.exp(-(x-m1)**2/(2*s1**2)) + (1-a)/numpy.sqrt(2*numpy.pi*s2**2)*numpy.exp(-(x-m2)**2/(2*s2**2))
        return p
    def residuals(self, params, x, y):
        err = self.gaussian(params, x)-y
        return err
    def fitting(self, x, y, initial=None):
        if not initial: initial = [-100] * 5
        result = leastsq(self.residuals, initial, args=(x, y), full_output=True)
        return result
    
lena = DensityDistribution(Image.open(r"../../Resources/lena256.gif"))
y = numpy.array(lena.density_distribution())
x = numpy.array([lena.xmax*k/256.0 for k in xrange(256)])
gf = GaussianFitting()
p1, success = gf.fitting(x, y)
    