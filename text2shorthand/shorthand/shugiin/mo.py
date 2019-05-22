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


class JoshiMo(ShugiinChar):
    def __init__(self, name='mo', kana='も',
                 model='UNER3', head_type='NER', tail_type='SWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature -= {'E'}

    
    @classmethod
    def path_UNER(cls, ta=None, **kwargs):
        #M 338.41114,393.61557 C 339.37031,392.38321 343.80672,385.93798 346.48166,387.87331 348.51403,389.34374 345.30412,394.28454 344.25578,395.06218

        z0 = P(0, -0)
        c0 = P(0.338374, 0.434749)
        c1 = P(1.90344, 2.70848)
        z1 = P(2.8471, 2.02574)
        c2 = P(3.56408, 1.50701)
        c3 = P(2.43169, -0.235998)
        z2 = P(2.06186, -0.510332)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_UNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNERswl(cls, ta=None, **kwargs):
        pass
