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

class Number6(SvsdChar):
    def __init__(self, name='6', kana='6',
                 model='6', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_6(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_6swl(cls, ta=None, **kwargs):
        pass

