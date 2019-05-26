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

class CharToh(SvsdChar):
    def __init__(self, name='とー', kana='toh',
                 model='E5CL1FP', head_type='E', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ECLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ECLFPswl(cls, ta=None, **kwargs):
        pass

