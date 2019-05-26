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

class CharChi(SvsdChar):
    def __init__(self, name='ち', kana='chi',
                 model='SW5', head_type='SW', tail_type='SW', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SW(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWswl(cls, ta=None, **kwargs):
        pass

