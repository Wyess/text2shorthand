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


class CharSa(ShugiinChar):
    def __init__(self, name='sa', kana='さ',
                 model='SR7', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SR(cls, ta=None, **kwargs):
        #M 317.143,76.022512 C 321.92827,79.013084 323.5357,96.258183 316.28953,100.44144
        z0 = P(0, -0)
        c0 = P(1.68814, -1.05501)
        c1 = P(2.2552, -7.1387)
        z1 = P(-0.301085, -8.61446)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswl(cls, ta=None, **kwargs):
        pass

class CharZa(CharSa):
    def __init__(self, name='za', kana='ざ',
                 model='SR7', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)
