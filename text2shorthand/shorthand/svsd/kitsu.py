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

class CharKitsu(SvsdChar):
    def __init__(self, name='きつ', kana='kitsu',
                 model='SWL10OL1', head_type='SWL', tail_type='SWLOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLOLswl(cls, ta=None, **kwargs):
        pass

