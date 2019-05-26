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

class CharLo(SvsdChar):
    def __init__(self, name='ぉ', kana='lo',
                 model='UNR1E', head_type='NER', tail_type='E', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNREswl(cls, ta=None, **kwargs):
        pass

