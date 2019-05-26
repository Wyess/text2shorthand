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

class CharTah(SvsdChar):
    def __init__(self, name='たー', kana='tah',
                 model='NE5CL1FP', head_type='NE', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NECLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLFPswl(cls, ta=None, **kwargs):
        pass

