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

class CharReh(SvsdChar):
    def __init__(self, name='れー', kana='reh',
                 model='SR5CR1FP', head_type='SR', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SRCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRFPswl(cls, ta=None, **kwargs):
        pass

