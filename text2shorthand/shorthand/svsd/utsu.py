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

class CharUtsu(SvsdChar):
    def __init__(self, name='うつ', kana='utsu',
                 model='SE10OL1', head_type='SE', tail_type='SEOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SEOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEOLswl(cls, ta=None, **kwargs):
        pass

