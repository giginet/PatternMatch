# -*- coding: utf-8 -*-
#
#    assignment1.no1
#    created by 25090335 Kohki Miki on 2011/07/19
#
import itertools
from matplotlib import pyplot

from pattern import patterns

if __name__ == '__main__':
    list = itertools.combinations(range(0, 10), 2)
    distances = [patterns[i].hamming_distance(patterns[j]) for i,j in list]
    hist = [distances.count(i) for i in xrange(0, 25)]
    pyplot.bar(range(25), hist)
    pyplot.xlim((0, 25))
    pyplot.xticks(xrange(0, 25))
    pyplot.show()