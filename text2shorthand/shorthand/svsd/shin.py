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

class CharShin(SvsdChar):
    def __init__(self, name='しん', kana='shin',
                 model='SWL5CL1', head_type='SWL', tail_type='SWLCL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLswl(cls, ta=None, **kwargs):
        pass

