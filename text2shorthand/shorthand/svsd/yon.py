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

class CharYon(SvsdChar):
    def __init__(self, name='よん', kana='yon',
                 model='E20CL1', head_type='E', tail_type='ECL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ECL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLswl(cls, ta=None, **kwargs):
        pass

