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

class CharSon(SvsdChar):
    def __init__(self, name='そん', kana='son',
                 model='EL5CL1', head_type='EL', tail_type='ELCL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLswl(cls, ta=None, **kwargs):
        pass

