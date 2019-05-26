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

class CharEku(SvsdChar):
    def __init__(self, name='えく', kana='eku',
                 model='S10CR5', head_type='S', tail_type='S', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SCRswl(cls, ta=None, **kwargs):
        pass

