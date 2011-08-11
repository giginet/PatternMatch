# -*- coding: utf-8 -*-
#
#    assignment1.no3
#    created by 25090335 Kohki Miki on 2011/08/10
#

from matplotlib import pyplot
from pattern import patterns
from pattern.model import Pattern

THRESHOLD = 9

n = int(raw_input("n:"))
type = int(raw_input("0 for (A) or 1 for (B):"))

p = (25, 100)[type]

if __name__ == '__main__':
    pattern = patterns[n]
    sum = 0
    result = []
    for p in xrange(0, p):
        if type == 1: p *= 0.01
        sum = 0.0
        available = 0.0
        for c in xrange(10):
            count = 0
            for i in xrange(100):
                if not type:
                    handmade = pattern.generate_handmade(p/25.0)
                else:
                    handmade = Pattern.generate(5, 5, p)
                if handmade.hamming_distance(pattern) < THRESHOLD: 
                    available += 1
                    if pattern in handmade.nearest_pattern(patterns):
                        count += 1
            sum += count
        if available:
            result.append((sum/available))
        else:
            result.append(0)
    pyplot.plot(result)
    pyplot.title("n = %d Type %s Threshold = %d" % (n, 'A' if not type else 'B', THRESHOLD))
    pyplot.ylabel('frequency')
    pyplot.xlabel('p' if not type else 'q')
    pyplot.show()