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

class CharNe(SvsdChar):
    def __init__(self, name='ね', kana='ne',
                 model='SR10', head_type='SR', tail_type='SR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswl(cls, ta=None, **kwargs):
        pass

