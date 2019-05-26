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

class Number9(SvsdChar):
    def __init__(self, name='9', kana='9',
                 model='9', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_9(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_9swl(cls, ta=None, **kwargs):
        pass

