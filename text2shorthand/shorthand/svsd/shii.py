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

class CharShii(SvsdChar):
    def __init__(self, name='しー', kana='shii',
                 model='SWL5CL1FP', head_type='SWL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLCLFPswl(cls, ta=None, **kwargs):
        pass

