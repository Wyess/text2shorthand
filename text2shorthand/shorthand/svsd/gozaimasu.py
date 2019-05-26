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

class CharGozaimasu(SvsdChar):
    def __init__(self, name='ございます', kana='gozaimasu',
                 model='EL10', head_type='EL', tail_type='EL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_EL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELswl(cls, ta=None, **kwargs):
        pass

