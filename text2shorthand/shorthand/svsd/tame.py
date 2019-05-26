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

class CharTame(SvsdChar):
    def __init__(self, name='ため', kana='tame',
                 model='UER5', head_type='SER', tail_type='SWR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERswl(cls, ta=None, **kwargs):
        pass

