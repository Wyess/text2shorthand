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

class CharNii(SvsdChar):
    def __init__(self, name='にー', kana='nii',
                 model='SWR10CR1FP', head_type='SWR', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWRCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRFPswl(cls, ta=None, **kwargs):
        pass

