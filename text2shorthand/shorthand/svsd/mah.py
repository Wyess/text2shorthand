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

class CharMah(SvsdChar):
    def __init__(self, name='まー', kana='mah',
                 model='NER20CR1FP', head_type='NER', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NERCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRFPswl(cls, ta=None, **kwargs):
        pass

