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

class CharDeshita(SvsdChar):
    def __init__(self, name='でした', kana='deshita',
                 model='USEL5', head_type='SEL', tail_type='NWL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USELswl(cls, ta=None, **kwargs):
        pass

