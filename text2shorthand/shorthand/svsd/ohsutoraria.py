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

class CharOhsutoraria(SvsdChar):
    def __init__(self, name='オーストラリア', kana='ohsutoraria',
                 model='E5_X5_GSW10', head_type='E', tail_type='SW', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_E_X_GSW(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_X_GSWswl(cls, ta=None, **kwargs):
        pass

