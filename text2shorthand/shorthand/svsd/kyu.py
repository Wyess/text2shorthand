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

class CharKyu(SvsdChar):
    def __init__(self, name='きゅ', kana='kyu',
                 model='HSEL10', head_type='HSEL', tail_type='SEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HSEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSELswl(cls, ta=None, **kwargs):
        pass

