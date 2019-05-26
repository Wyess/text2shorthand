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

class CharRoku(SvsdChar):
    def __init__(self, name='ろく', kana='roku',
                 model='ER5CR5', head_type='ER', tail_type='ERCR5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ERCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERCRswl(cls, ta=None, **kwargs):
        pass

