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

class CharKotsu(SvsdChar):
    def __init__(self, name='こつ', kana='kotsu',
                 model='EL10OL1', head_type='EL', tail_type='ELOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELOLswl(cls, ta=None, **kwargs):
        pass

