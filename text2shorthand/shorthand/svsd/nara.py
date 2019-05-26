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

class CharNara(SvsdChar):
    def __init__(self, name='なら', kana='nara',
                 model='UNER10', head_type='NER', tail_type='SWR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERswl(cls, ta=None, **kwargs):
        pass

