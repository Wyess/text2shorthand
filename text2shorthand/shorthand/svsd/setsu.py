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

class CharSetsu(SvsdChar):
    def __init__(self, name='せつ', kana='setsu',
                 model='SL5OL1', head_type='SL', tail_type='SLOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SLOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLOLswl(cls, ta=None, **kwargs):
        pass

