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

class CharTatsu(SvsdChar):
    def __init__(self, name='たつ', kana='tatsu',
                 model='NE5OL1', head_type='NE', tail_type='NEOL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NEOL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEOLswl(cls, ta=None, **kwargs):
        pass

