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

class CharYu(SvsdChar):
    def __init__(self, name='ゆ', kana='yu',
                 model='SE20', head_type='SE', tail_type='SE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEswl(cls, ta=None, **kwargs):
        pass

