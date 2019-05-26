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

class CharSore(SvsdChar):
    def __init__(self, name='それ', kana='sore',
                 model='USL1', head_type='SEL', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLswl(cls, ta=None, **kwargs):
        pass

