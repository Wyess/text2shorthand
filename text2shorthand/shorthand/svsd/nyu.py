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

class CharNyu(SvsdChar):
    def __init__(self, name='にゅ', kana='nyu',
                 model='HSER10', head_type='HSER', tail_type='SER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HSER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSERswl(cls, ta=None, **kwargs):
        pass

