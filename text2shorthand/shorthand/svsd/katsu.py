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

class CharKatsu(SvsdChar):
    def __init__(self, name='かつ', kana='katsu',
                 model='NEL10OL1', head_type='NEL', tail_type='NELOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NELOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELOLswl(cls, ta=None, **kwargs):
        pass

