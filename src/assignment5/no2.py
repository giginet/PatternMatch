# -*- coding: utf-8 -*-
#    
#    assignment5.no2
#    created by 25090335 Kohki Miki on 2011/08/12
#

from PIL import Image

from assignment4.no1 import DensityDistribution

class BinaryImage(object):
    XMAX = 5.
    def __init__(self, image):
        self.image = image
        
    @classmethod
    def to_xc(cls, kc):
        return cls.XMAX * kc/256.0
    
    @classmethod
    def to_kc(cls, xc):
        return 256.0 * xc/cls.XMAX
    
    def binarization(self, xc):
        kc = self.to_kc(xc)
        binarization = Image.new('L', self.image.size)
        binarization.putdata([0 if p < kc else 255 for p in self.image.getdata()])
        return binarization
        
    def diff(self, other):
        diff = Image.new('L', self.image.size)
        diff.putdata([abs(b1 - b2) for b1, b2 in zip(self.image.getdata(), other.getdata())])
        return diff
    
    def get_change_point(self, other):
        seq = range(256)
        seq.reverse()
        max = -1
        max_x = 0
        for kc in seq:
            xc = BinaryImage.to_xc(kc)
            pb = self.binarization(xc)
            qb = other.binarization(xc)
            
            d = BinaryImage(pb).diff(qb)
            dd = DensityDistribution(d)
            black = DensityDistribution(Image.new('L', self.image.size, 0))
            divergence = dd.divergence(black)
            
            if abs(divergence) > max:
                max = abs(divergence)
                max_x = xc
        return max_x
if __name__ == '__main__':
    p = BinaryImage(Image.open(r"../../Resources/CIMG0209.gif"))
    q = BinaryImage(Image.open(r"../../Resources/CIMG0210.gif"))
    r = BinaryImage(Image.open(r"../../Resources/CIMG0211.gif"))
    pb = p.binarization(3.73)
    qb = q.binarization(3.73)
    rb = r.binarization(3.06)
    pqd = BinaryImage(pb).diff(qb)
    prd = BinaryImage(pb).diff(rb)
    map(lambda i: i.show(), (pb, qb, rb, pqd, prd))