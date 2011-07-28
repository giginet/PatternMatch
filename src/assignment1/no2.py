# -*- coding: utf-8 -*-
'''
    assignment1.no2
    created by 25090335 Kohki Miki on 2011/07/19
'''
from pattern import patterns
from pattern.model import Pattern

n = int(raw_input("n:"))
type = int(raw_input("0 for (A) or 1 for (B):"))
threshold = int(raw_input("threshold:"))

p = (25, 100)[type]

if __name__ == '__main__':
    pattern = patterns[n]
    sum = 0
    for p in xrange(0, p):
        if type == 1: p *= 0.01
        sum = 0
        for c in xrange(10):
            count = 0
            for i in xrange(100):
                if not type:
                    handmade = pattern.generate_handmade(p/25.0)
                else:
                    handmade = Pattern.generate(5, 5, p)
                if handmade.hamming_distance(pattern) > threshold:
                    continue
                if pattern in handmade.nearest_pattern(patterns):
                    count += 1
            sum += count
        print p, sum/10.0