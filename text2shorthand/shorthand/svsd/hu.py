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

class CharHu(SvsdChar):
    def __init__(self, name='ふ', kana='hu',
                 model='SEL20', head_type='SEL', tail_type='SEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELswl(cls, ta=None, **kwargs):
        pass

