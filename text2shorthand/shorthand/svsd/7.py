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

class Number7(SvsdChar):
    def __init__(self, name='7', kana='7',
                 model='7', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_7(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_7swl(cls, ta=None, **kwargs):
        pass

