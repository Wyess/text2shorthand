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


class CharA(SvsdChar):
    def __init__(self, name='a', kana='あ',
                 model='NE10', head_type='NE', tail_type='NE'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {'NE'}
    
    @classmethod
    def path_NE(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(10, 30))

    @classmethod
    def path_NEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEne(cls, ta=None, **kwargs):
        return cls.jog(cls.path_NE())

    @classmethod
    def path_NEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEswl(cls, ta=None, **kwargs):
        pass
