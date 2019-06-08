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


class CharNomo(ShugiinChar):
    def __init__(self, name='nomo', kana='～のも',
                 model='NEL3UNEL3', head_type='NEL', tail_type='SWL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_NELUNEL(self, ta=None, **kwwargs):
        #M 122.62247,628.78087 C 122.62247,628.78087 128.4599,628.67914 130.17572,624.75147 131.33585,622.09582 128.98777,620.18924 126.92192,624.66477
        z0 = P(0, -0)
        c0 = P(0, -0)
        c1 = P(2.05932, 0.0358881)
        z1 = P(2.66462, 1.42148)
        c2 = P(3.07389, 2.35834)
        c3 = P(2.24554, 3.03094)
        z2 = P(1.51675, 1.45207)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_NELUNELe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NELUNELswl(self, ta=None, **kwwargs):
        pass


