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

class CharToiu(SvsdChar):
    def __init__(self, name='という', kana='toiu',
                 model='SW5FP', head_type='SW', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWFPswl(cls, ta=None, **kwargs):
        pass

