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

class CharHeh(SvsdChar):
    def __init__(self, name='へー', kana='heh',
                 model='UWL5CL1FP', head_type='UWL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UWLCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLCLFPswl(cls, ta=None, **kwargs):
        pass

