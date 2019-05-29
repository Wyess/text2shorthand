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


class CharHana(ShugiinChar):
    def __init__(self, name='hana', kana='はな',
                 model='HSEL9', head_type='HSEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature -= {'NER', 'S''}
    
    @classmethod
    def path_HSEL(self, ta=None, **kwwargs):
        #M 116.29164,247.55576 C 116.70923,244.53978 112.17045,244.09995 111.65994,246.84319 110.40121,253.60693 116.2253,263.89669 128.64282,264.18236

        z0 = P(0, -0)
        c0 = P(0.147316, 1.06397)
        c1 = P(-1.45386, 1.21913)
        z1 = P(-1.63396, 0.251379)
        c2 = P(-2.07801, -2.13472)
        c3 = P(-0.0234033, -5.76472)
        z2 = P(4.35722, -5.8655)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HSELe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELswl(self, ta=None, **kwwargs):
        pass


