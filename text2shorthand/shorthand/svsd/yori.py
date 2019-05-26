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

class CharYori(SvsdChar):
    def __init__(self, name='より', kana='yori',
                 model='HSWR5', head_type='HSWR', tail_type='SWR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HSWR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSWRswl(cls, ta=None, **kwargs):
        pass

