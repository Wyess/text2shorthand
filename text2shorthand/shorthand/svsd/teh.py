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

class CharTeh(SvsdChar):
    def __init__(self, name='てー', kana='teh',
                 model='S5CR1FP', head_type='S', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRFPswl(cls, ta=None, **kwargs):
        pass

