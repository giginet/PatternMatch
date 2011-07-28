# -*- coding: utf-8 -*-
'''
    pattern.model
    created by 25090335 Kohki Miki on 2011/07/19
'''
import random

class Pattern(object):
    def __init__(self, tuple, name=""):
        u"""
            コンストラクタ。二次元リストからPatternを生成します
            param:    tuple 数値から成る二次元リスト
            param:    name そのパターンの名前
        """
        self.matrix = tuple
        self.name = name
        
    @staticmethod
    def generate(w, h, p=1):
        u"""
            確率pで各数字を0としたw*hのPatternを生成します
            param     w
            param     h
            param     p
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
            パターンの特徴ベクトルを取り出すプロパティです
            return:    特徴ベクトル
        """
        return reduce(lambda a, b: a+b, self.matrix)
    
    def hamming_distance(self, other):
        u"""
            渡したPatternとのハミング距離を計算します
            param:    other 比較するPatternインスタンス
            return:　　そのインスタンスとのハミング距離
        """
        commons = [x for x, y in zip(self.vector, other.vector) if x == y]
        return max(len(self.vector), len(other.vector)) - len(commons)
    
    def nearest_pattern(self, patterns):
        u"""
            渡したPatternのタプルの中から、もっとも近いパターンを取り出します
            param:     patterns Patternインスタンスを含むタプル
            return:    最もハミング距離の短いインスタンス
                        　複数ある場合はタプル
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
        new = [[n(x) for x in col] for col in self.matrix]
        return Pattern(new)