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

class CharHuku(SvsdChar):
    def __init__(self, name='ふく', kana='huku',
                 model='SEL20CL5', head_type='SEL', tail_type='SEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLswl(cls, ta=None, **kwargs):
        pass

