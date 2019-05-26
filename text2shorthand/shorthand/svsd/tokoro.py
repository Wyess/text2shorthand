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

class CharTokoro(SvsdChar):
    def __init__(self, name='ところ', kana='tokoro',
                 model='SER10', head_type='SER', tail_type='SER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERswl(cls, ta=None, **kwargs):
        pass

