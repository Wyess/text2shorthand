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

class CharNakuteha(SvsdChar):
    def __init__(self, name='なくては', kana='nakuteha',
                 model='XNER20', head_type='X', tail_type='NER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_XNER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_XNERswl(cls, ta=None, **kwargs):
        pass

