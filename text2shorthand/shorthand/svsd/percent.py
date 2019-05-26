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

class NumberPercent(SvsdChar):
    def __init__(self, name='％', kana='percent',
                 model='BNE10', head_type='BNE', tail_type='NE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_BNE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BNEswl(cls, ta=None, **kwargs):
        pass

