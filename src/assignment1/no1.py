# -*- coding: utf-8 -*-
#
#    assignment1.no1
#    created by 25090335 Kohki Miki on 2011/07/19
#
import sys
print sys.path
import itertools
from pattern import patterns

if __name__ == '__main__':
    list = itertools.combinations(range(0, 9), 2)
    distances = [patterns[i].hamming_distance(patterns[j]) for i,j in list]
    for i in xrange(0, 25):
        print i, distances.count(i)