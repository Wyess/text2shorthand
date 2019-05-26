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

class CharHen(SvsdChar):
    def __init__(self, name='へん', kana='hen',
                 model='UWL5CL1', head_type='UWL', tail_type='UWLCL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UWLCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLswl(cls, ta=None, **kwargs):
        pass

