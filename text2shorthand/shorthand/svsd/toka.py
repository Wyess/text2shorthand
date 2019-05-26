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

class CharToka(SvsdChar):
    def __init__(self, name='とか', kana='toka',
                 model='E5NW4', head_type='E', tail_type='NW', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ENW(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ENWswl(cls, ta=None, **kwargs):
        pass

