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

class Number3(SvsdChar):
    def __init__(self, name='3', kana='3',
                 model='3', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_3(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_3swl(cls, ta=None, **kwargs):
        pass

