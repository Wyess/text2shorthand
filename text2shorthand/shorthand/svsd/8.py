from ..svsd.char import SvsdChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)

class Number8(SvsdChar):
    def __init__(self, name='8', kana='8',
                 model='8', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_8(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_8swl(cls, ta=None, **kwargs):
        pass

