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

class CharRo(SvsdChar):
    def __init__(self, name='ろ', kana='ro',
                 model='ER5', head_type='ER', tail_type='ER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ER(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERswl(cls, ta=None, **kwargs):
        pass

