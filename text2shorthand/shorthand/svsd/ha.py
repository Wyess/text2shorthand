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

class CharHa(SvsdChar):
    def __init__(self, name='は', kana='ha',
                 model='NEL20', head_type='NEL', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswl(cls, ta=None, **kwargs):
        pass

