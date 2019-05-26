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

class CharSeh(SvsdChar):
    def __init__(self, name='せー', kana='seh',
                 model='SL5CL1FP', head_type='SL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SLCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLCLFPswl(cls, ta=None, **kwargs):
        pass

