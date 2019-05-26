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

class CharMyo(SvsdChar):
    def __init__(self, name='みょ', kana='myo',
                 model='HER20', head_type='HER', tail_type='ER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HERswl(cls, ta=None, **kwargs):
        pass

