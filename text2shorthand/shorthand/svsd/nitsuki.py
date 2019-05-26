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

class CharNitsuki(SvsdChar):
    def __init__(self, name='につき', kana='nitsuki',
                 model='CSEL5', head_type='CSEL', tail_type='CSEL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_CSEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CSELswl(cls, ta=None, **kwargs):
        pass

