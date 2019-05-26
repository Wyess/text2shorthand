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

class EraHeisei(SvsdChar):
    def __init__(self, name='平成', kana='heisei',
                 model='h', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_h(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_he(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_her(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_hswl(cls, ta=None, **kwargs):
        pass

