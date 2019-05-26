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

class CharMya(SvsdChar):
    def __init__(self, name='みゃ', kana='mya',
                 model='HNER20', head_type='HNER', tail_type='NER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HNER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HNERswl(cls, ta=None, **kwargs):
        pass

