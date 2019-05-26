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

class Number2(SvsdChar):
    def __init__(self, name='2', kana='2',
                 model='2', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_2(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_2swl(cls, ta=None, **kwargs):
        pass

