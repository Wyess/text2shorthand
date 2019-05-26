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

class CharHetsu(SvsdChar):
    def __init__(self, name='へつ', kana='hetsu',
                 model='UWL5OL1', head_type='UWL', tail_type='UWLOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UWLOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLOLswl(cls, ta=None, **kwargs):
        pass

