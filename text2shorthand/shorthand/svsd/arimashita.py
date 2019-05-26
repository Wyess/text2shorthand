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

class CharArimashita(SvsdChar):
    def __init__(self, name='ありました', kana='arimashita',
                 model='NE10NW5', head_type='NE', tail_type='NW', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NENW(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NENWswl(cls, ta=None, **kwargs):
        pass

