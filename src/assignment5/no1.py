# -*- coding: utf-8 -*-
#    
#    assignment5.no1
#    created by 25090335 Kohki Miki on 2011/08/10
#
import numpy
from PIL import Image
from scipy.optimize import leastsq
from matplotlib import pyplot

from assignment4.no1 import DensityDistribution

class GaussianFitting(object):
    def gaussian(self, params, x):
        a, m1, m2, s1, s2 = params
        p = a/numpy.sqrt(2*numpy.pi*s1**2)*numpy.exp(-(x-m1)**2/(2*s1**2)) + (1-a)/numpy.sqrt(2*numpy.pi*s2**2)*numpy.exp(-(x-m2)**2/(2*s2**2))
        return p
    def residuals(self, params, x, y):
        err = self.gaussian(params, x) - y
        return err
    def fitting(self, x, y, initial=None):
        if not initial: initial = [0.] * 5
        result = leastsq(self.residuals, initial, args=(x, y), full_output=False)
        return result

if __name__ == '__main__':
    p1 = DensityDistribution(Image.open(r"../../Resources/CIMG0209.gif"))
    x, y = p1.density_distribution()
    gf = GaussianFitting()
    initial = (0.63583867, 3.22051539, 1.26030523, 0.64014307, 0.52168001)
    params = gf.fitting(x, y, initial)
    time = numpy.linspace(x[0], x[-1], 100)
    print params[0]
    pyplot.plot(x, y, x, [gf.gaussian(params[0], t) for t in x], "r-")
    pyplot.title(r"CIMG0209.gif")
    pyplot.xlabel("x")
    pyplot.ylabel("P(x)")
    pyplot.show()
    
    p2 = DensityDistribution(Image.open(r"../../Resources/CIMG0210.gif"))
    x, y = p2.density_distribution()
    gf = GaussianFitting()
    initial = (0.63583867, 3.22051539, 1.26030523, 0.64014307, 0.52168001)
    params = gf.fitting(x, y, initial)
    time = numpy.linspace(x[0], x[-1], 100)
    print params[0]
    pyplot.plot(x, y, x, [gf.gaussian(params[0], t) for t in x], "r-")
    pyplot.title(r"CIMG0210.gif")
    pyplot.xlabel("x")
    pyplot.ylabel("Q(x)")
    pyplot.show()
    
    p3 = DensityDistribution(Image.open(r"../../Resources/CIMG0211.gif"))
    x, y = p3.density_distribution()
    gf = GaussianFitting()
    initial = (0.63583867, 3.22051539, 1.26030523, 0.64014307, 0.52168001)
    params = gf.fitting(x, y, initial)
    time = numpy.linspace(x[0], x[-1], 100)
    print params[0]
    pyplot.plot(x, y, x, [gf.gaussian(params[0], t) for t in x], "r-")
    pyplot.title(r"CIMG0211.gif")
    pyplot.xlabel("x")
    pyplot.ylabel("R(x)")
    pyplot.show()