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

class Number1(SvsdChar):
    def __init__(self, name='1', kana='1',
                 model='1', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_1(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1e(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1er(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1el(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1ne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1ner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1nel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1s(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1sl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1sr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1sw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1swr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_1swl(cls, ta=None, **kwargs):
        pass

