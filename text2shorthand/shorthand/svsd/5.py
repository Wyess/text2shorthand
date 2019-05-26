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

class Number5(SvsdChar):
    def __init__(self, name='5', kana='5',
                 model='5', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_5(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_5swl(cls, ta=None, **kwargs):
        pass

