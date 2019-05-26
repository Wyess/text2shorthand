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

class CharLi(SvsdChar):
    def __init__(self, name='ぃ', kana='li',
                 model='UNR1SW', head_type='NER', tail_type='SW', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRSW(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSWswl(cls, ta=None, **kwargs):
        pass

