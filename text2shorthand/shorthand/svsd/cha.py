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

class CharCha(SvsdChar):
    def __init__(self, name='ちゃ', kana='cha',
                 model='HNE5', head_type='HNE', tail_type='NE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HNE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNEswl(cls, ta=None, **kwargs):
        pass

