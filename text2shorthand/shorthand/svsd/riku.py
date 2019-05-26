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

class CharRiku(SvsdChar):
    def __init__(self, name='りく', kana='riku',
                 model='SWR5CR5', head_type='SWR', tail_type='SWRCR5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWRCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRswl(cls, ta=None, **kwargs):
        pass

