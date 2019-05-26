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

class CharMashou(SvsdChar):
    def __init__(self, name='ましょう', kana='mashou',
                 model='EL5CNWL5', head_type='EL', tail_type='ELNWL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELCNWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCNWLswl(cls, ta=None, **kwargs):
        pass

