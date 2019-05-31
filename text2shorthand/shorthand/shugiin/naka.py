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


class CharNaka(ShugiinChar):
    def __init__(self, name='naka', kana='なか',
                 model='HEL9', head_type='HEL', tail_type='EL',
                 flick_pos=None):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature -= {'ER', 'NER'}
    
    @classmethod
    def path_HEL(self, ta=None, **kwwargs):
        #M 94.748513,202.12374 C 92.584676,200.67192 88.441614,201.68923 89.381963,203.8718 92.219104,210.45688 106.16263,212.80428 114.62908,205.37623

        z0 = P(0, -0)
        c0 = P(-0.763354, 0.51217)
        c1 = P(-2.22493, 0.153285)
        z1 = P(-1.8932, -0.616677)
        c2 = P(-0.892319, -2.93975)
        c3 = P(4.02665, -3.76786)
        z2 = P(7.01342, -1.14741)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HELe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELswl(self, ta=None, **kwwargs):
        pass
