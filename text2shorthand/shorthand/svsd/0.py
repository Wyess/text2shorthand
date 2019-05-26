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

class Number0(SvsdChar):
    def __init__(self, name='0', kana='0',
                 model='0', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_0(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_0swl(cls, ta=None, **kwargs):
        pass

