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

class CharCho(SvsdChar):
    def __init__(self, name='ちょ', kana='cho',
                 model='BE5', head_type='BE', tail_type='E', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_BE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEswl(cls, ta=None, **kwargs):
        pass

