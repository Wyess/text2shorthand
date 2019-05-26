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

class CharTotsu(SvsdChar):
    def __init__(self, name='とつ', kana='totsu',
                 model='E5OL1', head_type='E', tail_type='EOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_EOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_EOLswl(cls, ta=None, **kwargs):
        pass

