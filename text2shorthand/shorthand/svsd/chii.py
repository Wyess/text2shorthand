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

class CharChii(SvsdChar):
    def __init__(self, name='ちー', kana='chii',
                 model='SW5CR1FP', head_type='SW', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRFPswl(cls, ta=None, **kwargs):
        pass

