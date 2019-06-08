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

class CharNo(ShugiinChar):
    def __init__(self, name='no', kana='の',
                 model='NEL3', head_type='NEL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_NEL(cls, ta=None, **kwargs):
        #M 180.61974,496.94587 C 183.80206,495.77859 185.53002,494.07229 186.85375,491.16801
        z0 = P(0, -0)
        c0 = P(1.12265, 0.41179)
        c1 = P(1.73224, 1.01374)
        z1 = P(2.19922, 2.0383)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswl(cls, ta=None, **kwargs):
        pass
