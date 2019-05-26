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

class CharHah(SvsdChar):
    def __init__(self, name='はー', kana='hah',
                 model='NEL20CL1FP', head_type='NEL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NELCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLFPswl(cls, ta=None, **kwargs):
        pass

