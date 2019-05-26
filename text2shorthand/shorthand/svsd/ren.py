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

class CharRen(SvsdChar):
    def __init__(self, name='れん', kana='ren',
                 model='SR5CR1', head_type='SR', tail_type='SRCR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SRCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRCRswl(cls, ta=None, **kwargs):
        pass

