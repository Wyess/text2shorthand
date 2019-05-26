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

class NumberRange1(SvsdChar):
    def __init__(self, name='若干数1', kana='range1',
                 model='P', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_P(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Per(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ps(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Psl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Psr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Psel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Psw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Pswl(cls, ta=None, **kwargs):
        pass

