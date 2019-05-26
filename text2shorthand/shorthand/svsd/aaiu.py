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

class CharAaiu(SvsdChar):
    def __init__(self, name='ああいう', kana='aaiu',
                 model='NE10SW5FP', head_type='NE', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NESWFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWFPswl(cls, ta=None, **kwargs):
        pass

