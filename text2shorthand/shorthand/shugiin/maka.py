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


class CharMaka(ShugiinChar):
    def __init__(self, name='maka', kana='まか',
                 model='HER9', head_type='HER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.before.tail_type == 'S':
            self.head = self.before.tail + PP(1.7, -22)
        super().set_next_head(flick_len, dz)
    
    @classmethod
    def path_HER(self, ta=None, **kwwargs):
        #M 81.185274,260.85791 C 77.451224,261.16118 75.149816,259.82776 77.997579,257.16063 89.296435,246.57846 105.1772,252.15007 108.45317,258.86755

        z0 = P(0, -0)
        c0 = P(-1.31729, -0.106987)
        c1 = P(-2.12918, 0.363414)
        z1 = P(-1.12455, 1.30432)
        c2 = P(2.86144, 5.03747)
        c3 = P(8.46382, 3.07193)
        z2 = P(9.61951, 0.702155)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HERe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERswl(self, ta=None, **kwwargs):
        pass


