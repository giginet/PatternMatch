# -*- coding: utf-8 -*-
#    
#    assignment5.output
#    created by 25090335 Kohki Miki on 2011/08/11
#
from PIL import Image
from assignment4.no1 import DensityDistribution
from matplotlib import pyplot

image = DensityDistribution(Image.open(r"../../Resources/CIMG0211.gif"))
xs, ys = image.density_distribution()
for x, y in zip(xs, ys):
    print x, y