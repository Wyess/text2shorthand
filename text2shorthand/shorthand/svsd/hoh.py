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

class CharHoh(SvsdChar):
    def __init__(self, name='ほー', kana='hoh',
                 model='EL20CL1FP', head_type='EL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELCLFPswl(cls, ta=None, **kwargs):
        pass

