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

class CharHe(SvsdChar):
    def __init__(self, name='へ', kana='he',
                 model='UWL5', head_type='SWL', tail_type='SEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswl(cls, ta=None, **kwargs):
        pass

