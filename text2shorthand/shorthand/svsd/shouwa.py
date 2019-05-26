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

class EraShouwa(SvsdChar):
    def __init__(self, name='昭和', kana='shouwa',
                 model='S', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_S(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Snel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ss(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswl(cls, ta=None, **kwargs):
        pass

