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

class CharNa(SvsdChar):
    def __init__(self, name='な', kana='na',
                 model='NER10', head_type='NER', tail_type='NER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERswl(cls, ta=None, **kwargs):
        pass

