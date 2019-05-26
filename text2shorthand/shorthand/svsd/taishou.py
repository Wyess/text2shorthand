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

class EraTaishou(SvsdChar):
    def __init__(self, name='大正', kana='taishou',
                 model='T', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_T(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Te(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ter(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ts(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Tswl(cls, ta=None, **kwargs):
        pass

