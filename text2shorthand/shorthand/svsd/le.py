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

class CharLe(SvsdChar):
    def __init__(self, name='ぇ', kana='le',
                 model='UNR1S', head_type='NER', tail_type='S', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRSswl(cls, ta=None, **kwargs):
        pass

