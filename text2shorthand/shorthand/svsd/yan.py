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

class CharYan(SvsdChar):
    def __init__(self, name='やん', kana='yan',
                 model='NE20CL1', head_type='NE', tail_type='NECL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NECL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLswl(cls, ta=None, **kwargs):
        pass

