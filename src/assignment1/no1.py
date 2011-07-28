# -*- coding: utf-8 -*-
'''
    assignment1.no1
    created by 25090335 Kohki Miki on 2011/07/19
'''
import sys
print sys.path
import itertools
from pattern import patterns

if __name__ == '__main__':
    if sys.version_info [0] >= 2 and sys.version_info[1] >= 6:
        #itertools.combinationsはPython2.6以上から実装されている
        #しかし、実験室上の環境ではバージョンが古く、利用できないため
        #分岐させている
        list = itertools.combinations(range(0, 9), 2)
    else:
        list = [(a, b) for a in xrange(0, 10) for b in xrange(a+1, 10)]
    distances = [patterns[i].hamming_distance(patterns[j]) for i,j in list]
    for i in xrange(0, 25):
        print i, distances.count(i)
