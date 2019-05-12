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
                 model='SR9', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SR(cls, ta=None, **kwargs):
        #M 387.73031,172.99871 C 392.51531,175.98971 395.024,193.291 387.777,197.474

        z0 = P(0, -0)
        c0 = P(1.68804, -1.05516)
        c1 = P(2.57305, -7.15867)
        z1 = P(0.0164712, -8.63434)

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
