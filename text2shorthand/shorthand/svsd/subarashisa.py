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

class CharSubarashisa(SvsdChar):
    def __init__(self, name='すばらしさ', kana='subarashisa',
                 model='SEL5SWL5NEL5', head_type='SEL', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELSWLNEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLNELswl(cls, ta=None, **kwargs):
        pass

