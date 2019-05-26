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

class CharDouiu(SvsdChar):
    def __init__(self, name='どういう', kana='douiu',
                 model='E5SW5FP', head_type='E', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ESWFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWFPswl(cls, ta=None, **kwargs):
        pass

