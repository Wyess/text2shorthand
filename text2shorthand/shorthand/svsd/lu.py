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

class CharLu(SvsdChar):
    def __init__(self, name='ぅ', kana='lu',
                 model='UNR1SE', head_type='NER', tail_type='SE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRSE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSEswl(cls, ta=None, **kwargs):
        pass

