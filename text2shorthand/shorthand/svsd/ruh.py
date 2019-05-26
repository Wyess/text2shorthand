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

class CharRuh(SvsdChar):
    def __init__(self, name='るー', kana='ruh',
                 model='SER5CR1FP', head_type='SER', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SERCRFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRFPswl(cls, ta=None, **kwargs):
        pass

