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

class CharIke(SvsdChar):
    def __init__(self, name='いけ', kana='ike',
                 model='BSL10', head_type='BSL', tail_type='SL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_BSL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BSLswl(cls, ta=None, **kwargs):
        pass

