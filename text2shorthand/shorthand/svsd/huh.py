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

class CharHuh(SvsdChar):
    def __init__(self, name='ふー', kana='huh',
                 model='SEL20CL1FP', head_type='SEL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELCLFPswl(cls, ta=None, **kwargs):
        pass

