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

class CharDeshou(SvsdChar):
    def __init__(self, name='でしょう', kana='deshou',
                 model='SEL5CNWL5', head_type='SEL', tail_type='NWL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELCNWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCNWLswl(cls, ta=None, **kwargs):
        pass

