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

class CharNioite(SvsdChar):
    def __init__(self, name='において', kana='nioite',
                 model='SWR10NER5', head_type='SWR', tail_type='NER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWRNER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNERswl(cls, ta=None, **kwargs):
        pass

