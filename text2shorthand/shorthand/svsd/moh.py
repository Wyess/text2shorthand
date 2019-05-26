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

class CharMoh(SvsdChar):
    def __init__(self, name='もー', kana='moh',
                 model='ER20CR1FP', head_type='ER', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ERCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRFPswl(cls, ta=None, **kwargs):
        pass

