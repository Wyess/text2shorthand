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

class CharWatakushi(SvsdChar):
    def __init__(self, name='私', kana='watakushi',
                 model='UNR5', head_type='NER', tail_type='SER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRswl(cls, ta=None, **kwargs):
        pass

