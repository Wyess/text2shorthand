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

class CharGozaimashita(SvsdChar):
    def __init__(self, name='ございました', kana='gozaimashita',
                 model='EL10NWL5', head_type='EL', tail_type='NWL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELNWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELNWLswl(cls, ta=None, **kwargs):
        pass

