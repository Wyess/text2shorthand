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

class Number4(SvsdChar):
    def __init__(self, name='4', kana='4',
                 model='4', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_4(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_4swl(cls, ta=None, **kwargs):
        pass

