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

class CharWatsu(SvsdChar):
    def __init__(self, name='わつ', kana='watsu',
                 model='USL5OL1', head_type='USL', tail_type='USLOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USLOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLOLswl(cls, ta=None, **kwargs):
        pass

