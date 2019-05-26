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

class CharHi(SvsdChar):
    def __init__(self, name='ひ', kana='hi',
                 model='SWL20', head_type='SWL', tail_type='SWL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLswl(cls, ta=None, **kwargs):
        pass

