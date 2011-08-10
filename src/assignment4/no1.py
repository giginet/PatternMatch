# -*- coding: utf-8 -*-
#    
#    assignment4.no1
#    created by 25090335 Kohki Miki on 2011/07/30
#
import numpy
from PIL import Image
from matplotlib import pyplot

class DensityDistribution(object):
    def __init__(self, image):
        u"""
            コンストラクタ
            @param このパターンのイメージ
        """
        self.image = image
        self.width, self.height = self.image.size
        self.xmax = 5
        
    def histogram(self):
        u"""
            イメージのヒストグラムを返します
            @return k
            @return C[k]
        """
        return range(256), self.image.histogram()
    
    def plot_histogram(self, label=None):
        u"""
            ヒストグラムをプロットします
            @param label グラフ描画時のラベル
        """
        x, y = self.histogram()
        pyplot.plot(x, y)
        pyplot.xlabel('k')
        pyplot.ylabel('C[k]')
        if label: pyplot.title(label)
        pyplot.show()
        
    def density_distribution(self):
        u"""
            濃度分布を返します
            @return x
            @return P(x)
        """
        return [self.xmax*k/256.0 for k in xrange(256)], [self.p(k) for k in self.image.histogram()]
    
    def plot_density_distribution(self, label=None):
        u"""
            濃度分布をプロットします
            @param label グラフ描画時のラベル
        """
        x, y = self.density_distribution()
        pyplot.plot(x, y)
        pyplot.xlabel('x')
        pyplot.ylabel('P(x)')
        if label: pyplot.title(label)
        pyplot.show()
        
    def h(self, k):
        u"""
            渡した濃度の数を割合にして返します
            @param k 濃度の数
            @return 割合 
        """
        return float(k/(float(self.width*self.height)))
    
    def p(self, k):
        u"""
            kの濃度分布を返します
            @param k 
            @return 濃度分布P(x)
        """
        return (256.0/self.xmax)*self.h(k)
    
    def divergence(self, other):
        u"""
            他のイメージとのクルバックーライブラ・ダイバージェンスを計算します
            @param  other 比較するパターン
            @return クルバックーライブラ・ダイバージェンス
        """
        return sum([p*numpy.log(p/q if p and q else 1) for p, q in zip([self.p(k) for k in self.image.histogram()], [other.p(k) for k in other.image.histogram()])])

if __name__ == '__main__':
    lena = DensityDistribution(Image.open(r"../../Resources/lena256.gif"))
    lena.plot_histogram('lena256')
    lena.plot_density_distribution('lena256')
    p = DensityDistribution(Image.open(r"../../Resources/CIMG0209.gif"))
    p.plot_histogram('P')
    p.plot_density_distribution('P')
    q = DensityDistribution(Image.open(r"../../Resources/CIMG0210.gif"))
    q.plot_histogram('Q')
    q.plot_density_distribution('Q')
    r = DensityDistribution(Image.open(r"../../Resources/CIMG0211.gif"))
    r.plot_histogram('R')
    r.plot_density_distribution('R')
    
    print "D(P||Q) = %f" % p.divergence(q)
    print "D(P||R) = %f" % p.divergence(r)
