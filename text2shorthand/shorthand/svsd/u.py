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


class CharU(SvsdChar):
    def __init__(self, name='u', kana='う',
                 model='SE10', head_type='SE', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {'SE'}
    
    @classmethod
    def path_SE(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(10, -30))

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
        return cls.jog(cls.path_SE())

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
