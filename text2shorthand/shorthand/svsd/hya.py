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

class CharHya(SvsdChar):
    def __init__(self, name='ひゃ', kana='hya',
                 model='HNEL20', head_type='HNEL', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HNEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNELswl(cls, ta=None, **kwargs):
        pass

