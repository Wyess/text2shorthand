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

class CharMi(SvsdChar):
    def __init__(self, name='み', kana='mi',
                 model='SWR20', head_type='SWR', tail_type='SWR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRswl(cls, ta=None, **kwargs):
        pass

