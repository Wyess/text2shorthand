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

class CharKyo(SvsdChar):
    def __init__(self, name='きょ', kana='kyo',
                 model='HEL10', head_type='HEL', tail_type='EL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_HEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HELswl(cls, ta=None, **kwargs):
        pass

