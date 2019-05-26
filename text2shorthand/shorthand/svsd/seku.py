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

class CharSeku(SvsdChar):
    def __init__(self, name='せく', kana='seku',
                 model='SL5CL5', head_type='SL', tail_type='SL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SLCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLswl(cls, ta=None, **kwargs):
        pass

