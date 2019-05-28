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


class CharNaga(ShugiinChar):
    def __init__(self, name='naga', kana='なが',
                 model='HNEL9', head_type='HNEL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HNEL(self, ta=None, **kwwargs):
        #M 99.442075,246.205 C 95.8644,247.42358 97.217037,249.58495 98.617275,249.95646 104.14616,251.42337 115.45388,248.56312 117.46516,236.00543

        z0 = P(0, -0)
        c0 = P(-1.26212, -0.429888)
        c1 = P(-0.784944, -1.19237)
        z1 = P(-0.290971, -1.32343)
        c2 = P(1.6595, -1.84092)
        c3 = P(5.64861, -0.831892)
        z2 = P(6.35814, 3.59818)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HNELe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELswl(self, ta=None, **kwwargs):
        pass


