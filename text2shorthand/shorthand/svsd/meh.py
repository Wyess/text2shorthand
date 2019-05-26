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

class CharMeh(SvsdChar):
    def __init__(self, name='めー', kana='meh',
                 model='UER5CR1FP', head_type='UER', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UERCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRFPswl(cls, ta=None, **kwargs):
        pass

