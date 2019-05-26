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

class CharChin(SvsdChar):
    def __init__(self, name='ちん', kana='chin',
                 model='SW5CR1', head_type='SW', tail_type='SWCR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCRswl(cls, ta=None, **kwargs):
        pass

