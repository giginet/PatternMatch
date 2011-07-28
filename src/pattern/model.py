# -*- coding: utf-8 -*-
#
#  pattern.model
#  Created by 25090335 Kohki Miki on 2011/07/20
#
'''
    pattern.model
    created by 25090335 Kohki Miki on 2011/07/19
'''
import random
import numpy

class Pattern(object):
    def __init__(self, tuple, name=""):
        u"""
            コンストラクタ。二次元リストからPatternを生成します
            param:    tuple 数値から成る二次元リスト
            param:    name そのパターンの名前
        """
        self._matrix = tuple
        self.name = name
        
    @staticmethod
    def generate(w, h, p=1):
        u"""
            確率pで各数字を0としたw*hのPatternを生成します
            param     w パターンの幅
            param     h パターンの高さ
            param     p 0にする確率
            return    ランダムで生成されたPattern
        """
        def n():
            if random.random() < p:
                return 0
            else:
                return 1
        new = [[n() for a in xrange(w)] for b in xrange(h)] 
        return Pattern(new)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
        
    def __eq__(self, other):
        if not isinstance(other, Pattern): return False
        return self.hamming_distance(other) == 0

    @property
    def vector(self):
        u"""
            パターンの特徴ベクトルを取り出すプロパティです。<br>
            numpy.Matrix形式で取り出します
            return:    特徴ベクトル
        """
        return numpy.matrix(reduce(lambda a, b: a+b, self._matrix))
    
    @property
    def matrix(self):
        u"""
            パターンの行列を取り出すプロパティです。<br>
            numpy.Matrix形式で取り出します
            return:    行列
        """
        return numpy.matrix(self._matrix)
    
    def linear_discriminant_function(self, x):
        u"""
            渡されたパターンとこのパターンに線形判別関数g(X)を適応した値を返します
            param:     x 比較するパターン
            return:    線形判別関数(numpy.Matrix)の戻り値
        """
        return (self.vector * x.vector.T - 0.5 * numpy.power(x.vector, 2).sum()).sum()
    
    def hamming_distance(self, other):
        u"""
            渡したPatternとのハミング距離を計算します
            param:    other 比較するPatternインスタンス
            return:　　そのインスタンスとのハミング距離
        """
        return numpy.power(self.vector - other.vector, 2).sum()
    
    def nearest_pattern(self, patterns):
        u"""
            渡したPatternのタプルの中から、もっとも近いパターンを取り出します。<br>
            最小値のハミング距離をとるパターンが2つ以上見つかったときは、それらを含むタプルを返します
            param:     patterns Patternインスタンスを含むタプル
            return:    最もハミング距離の短いインスタンス。複数ある場合はタプル
         """
        hammings = [(pattern, self.hamming_distance(pattern)) for pattern in patterns]
        m = min([d[1] for d in hammings])
        return tuple([p for p, d in hammings if d == m])
    
    def generate_handmade(self, p=0):
        u"""
            特徴ベクトルの各成分を確率pで反転させたPatternを生成して返します
            param:     p　反転させる確率
            return:    生成されたPattern
         """
        def n(x):
            if random.random() < p:
                return (x+1)%2
            else:
                return x
        new = [[n(x) for x in col] for col in self._matrix]
        return Pattern(new)