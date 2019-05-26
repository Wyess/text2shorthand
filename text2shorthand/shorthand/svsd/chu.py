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

class CharChu(SvsdChar):
    def __init__(self, name='ちゅ', kana='chu',
                 model='BSE5', head_type='BSE', tail_type='SE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_BSE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSEswl(cls, ta=None, **kwargs):
        pass

