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

class CharWah(SvsdChar):
    def __init__(self, name='わー', kana='wah',
                 model='USL5CL1FP', head_type='USL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USLCLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLFPswl(cls, ta=None, **kwargs):
        pass

