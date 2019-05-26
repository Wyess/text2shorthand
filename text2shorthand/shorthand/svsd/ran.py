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

class CharRan(SvsdChar):
    def __init__(self, name='らん', kana='ran',
                 model='NER5CR1', head_type='NER', tail_type='NERCR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NERCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERCRswl(cls, ta=None, **kwargs):
        pass

