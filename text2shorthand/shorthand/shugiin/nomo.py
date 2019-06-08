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
        #M 143.01116,600.44405 C 143.01116,600.44405 148.84859,600.34232 150.56441,596.41465 152.51376,591.95241 148.54483,589.78613 147.02359,594.4432
        z0 = P(0, -0)
        c0 = P(0, -0)
        c1 = P(2.05932, 0.0358881)
        z1 = P(2.66462, 1.42148)
        c2 = P(3.35231, 2.99566)
        c3 = P(1.95216, 3.75988)
        z2 = P(1.4155, 2.11697)

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


