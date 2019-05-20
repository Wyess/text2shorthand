from ..shugiin.char import ShugiinChar
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


class JoshiNo(ShugiinChar):
    def __init__(self, name='no', kana='の',
                 model='NE3F', head_type='NE', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {}

    @classmethod
    def path_NEF(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(3, 45))

    @classmethod
    def path_NEFWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEFWswl(cls, ta=None, **kwargs):
        pass
