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

class CharSe(SvsdChar):
    def __init__(self, name='せ', kana='se',
                 model='SL5', head_type='SL', tail_type='SL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLswl(cls, ta=None, **kwargs):
        pass

