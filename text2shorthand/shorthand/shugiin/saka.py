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


class CharSaka(ShugiinChar):
    def __init__(self, name='saka', kana='さか',
                 model='HSR9', head_type='NER', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature -= {'SR', 'EL', 'SW'}

    @classmethod
    def path_HSR(cls, ta=None, **kwargs):
        #M 134.74093,780.4697 C 133.02975,777.58594 134.39659,774.0219 136.14803,774.37228 143.65678,775.87442 143.65958,794.88669 136.22987,799.8803

        z0 = P(0, -0)
        c0 = P(-0.603666, 1.01733)
        c1 = P(-0.121475, 2.27464)
        z1 = P(0.496394, 2.15103)
        c2 = P(3.14531, 1.62111)
        c3 = P(3.1463, -5.08599)
        z2 = P(0.525265, -6.84763)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HSRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRner(cls, ta=None, **kwargs):
        #M 124.281,78.6614 C 122.57,75.7776 123.937,72.2136 125.688,72.564 133.197,74.0661 130.12079,90.248223 125.77,98.072
        z0 = P(0, -0)
        c0 = P(-0.603603, 1.01734)
        c1 = P(-0.121356, 2.27464)
        z1 = P(0.496358, 2.15103)
        c2 = P(3.14537, 1.62112)
        c3 = P(2.06015, -4.08757)
        z2 = P(0.525286, -6.84763)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HSRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_HSRswl(cls, ta=None, **kwargs):
        pass
