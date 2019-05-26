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

class CharLa(SvsdChar):
    def __init__(self, name='ぁ', kana='la',
                 model='UNR1NE', head_type='NER', tail_type='NE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRNE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRNEswl(cls, ta=None, **kwargs):
        pass

