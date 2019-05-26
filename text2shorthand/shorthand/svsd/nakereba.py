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

class CharNakereba(SvsdChar):
    def __init__(self, name='なければ', kana='nakereba',
                 model='XNEL20', head_type='X', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_XNEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNELswl(cls, ta=None, **kwargs):
        pass

