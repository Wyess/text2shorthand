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

class CharMen(SvsdChar):
    def __init__(self, name='めん', kana='men',
                 model='UER5CR1', head_type='SER', tail_type='SWRCR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UERCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERCRswl(cls, ta=None, **kwargs):
        pass

