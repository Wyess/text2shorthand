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

class CharGozaimashite(SvsdChar):
    def __init__(self, name='ございまして', kana='gozaimashite',
                 model='EL10S5', head_type='EL', tail_type='S', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSswl(cls, ta=None, **kwargs):
        pass

