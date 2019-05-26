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

class CharHutsu(SvsdChar):
    def __init__(self, name='ふつ', kana='hutsu',
                 model='SEL20OL1', head_type='SEL', tail_type='SELOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELOLswl(cls, ta=None, **kwargs):
        pass

