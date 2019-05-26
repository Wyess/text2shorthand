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

class CharItsu(SvsdChar):
    def __init__(self, name='いつ', kana='itsu',
                 model='SW10OR1', head_type='SW', tail_type='SWOR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWOR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWORswl(cls, ta=None, **kwargs):
        pass

