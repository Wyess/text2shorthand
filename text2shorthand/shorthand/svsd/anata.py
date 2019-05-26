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

class CharAnata(SvsdChar):
    def __init__(self, name='あなた', kana='anata',
                 model='NE10SW2NE5', head_type='NE', tail_type='NE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NESWNE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWNEswl(cls, ta=None, **kwargs):
        pass

