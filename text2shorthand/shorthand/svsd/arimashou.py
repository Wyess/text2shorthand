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

class CharArimashou(SvsdChar):
    def __init__(self, name='ありましょう', kana='arimashou',
                 model='NE10CNWL5', head_type='NE', tail_type='NECNWL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NECNWL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECNWLswl(cls, ta=None, **kwargs):
        pass

