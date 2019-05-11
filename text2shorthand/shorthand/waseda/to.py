from ..waseda.char import WasedaChar
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

class CharTo(WasedaChar):
    def __init__(self, name='to', kana='と', model='SW16|NE16', head_type='SW|NE', tail_type='NE|SW', to_reverse=None):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = -7

    def to_reverse(self):
        if getattr(self.before, 'tail_type', '').endswith('F'):
            return False
        else:
            return not getattr(self.before, 'tail_type') in {
                'SWR', 'SW', 'SR', 'S', 'SER', '', 'SRCR1', 'P'}

    def get_paths(self):
        if self.to_reverse():
            self.head_type = 'SW'
            self.tail_type = 'SW'
            self.model = 'SW16'
        else:
            self.head_type = 'NE'
            self.tail_type = 'NE'
            self.model = 'NE16'

        return super(WasedaChar, self).get_paths()

    @classmethod
    def path_NE(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(16, 40))

    @classmethod
    def path_NENE(cls, ta=None, **kwargs):
        #M 345.067,86.2169 C 356.40642,76.257585 367.99108,66.543511 379.81,57.0637 380.2046,56.311876 380.29038,55.296055 381.18768,54.207776

        #z0 = P(0, -0)
        #c0 = P(4.0003, 3.51343)
        #c1 = P(8.08711, 6.94033)
        #z1 = P(12.2566, 10.2846)
        #c2 = P(12.3958, 10.5498)
        #c3 = P(12.426, 10.9082)
        z2 = P(12.7426, 11.2921)

        #z0 = P(0, -0)
        #c0 = z0 + P(4.0003, 3.51343)
        #z1 = z0 + P(12.2566, 10.2846)
        #c1 = z1 + P(-4.16945, -3.34427)
        #c2 = z1 + P(0.139206, 0.265227)
        #z2 = z1 + P(0.486015, 1.00751)
        #c3 = z2 + P(-0.316547, -0.383921)

        z0 = P(0, -0)
        c0 = z0 + PP(5.32414, 41)
        z1 = z0 + PP(15.9999, 40)
        #z1 = z2 - PP(1.11861, ta + 373)
        c1 = z1 + PP(5.34495, -141)
        c2 = z1 + PP(0.299539, 62)
        z2 = z1 + PP(1.11861, 64)
        c3 = z2 + PP(0.497592, -129)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_SW(cls, ta=-115, **kwargs):
        return pyx.path.line(0, 0, *PP(16, -115))

    @classmethod
    def path_SWNE(cls, ta=None, **kwargs):
        #M 70.0186,221.374 C 64.101355,235.54762 57.710318,249.24745 50.851,262.479 51.764401,261.75619 52.657481,261.04354 53.893874,260.15923

        #z0 = P(0, -0)
        #c0 = P(-2.08747, -5.00014)
        #c1 = P(-4.34209, -9.83313)
        #z1 = P(-6.7619, -14.5009)
        #c2 = P(-6.43968, -14.2459)
        #c3 = P(-6.12462, -13.9945)
        #z2 = P(-5.68845, -13.6826)

        #z0 = P(0, -0)
        #c0 = z0 + P(-2.08747, -5.00014)
        #z1 = z0 + P(-6.7619, -14.5009)
        #c1 = z1 + P(2.41981, 4.6678)
        #c2 = z1 + P(0.322228, 0.254991)
        #z2 = z1 + P(1.07346, 0.818363)
        #c3 = z2 + P(-0.436172, -0.311965)

        z0 = P(0, -0)
        c0 = z0 + PP(5.41839, -112)
        z1 = z0 + PP(16, -115)
        #z1 = z2 - PP(1.34983, ta + 361)
        c1 = z1 + PP(5.25774, 62)
        c2 = z1 + PP(0.410915, 38)
        z2 = z1 + PP(1.34983, 37)
        c3 = z2 + PP(0.536254, -144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

class CharTon(CharTo):
    def __init__(self, name='ton', kana='とん', 
            model='SW16NE1F|NE16NE1F', head_type='SW|NE', tail_type='NEF', to_reverse=None):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_type = 'SW'
            self.tail_type = 'NEF'
            self.model = 'SW16NE1F'
            return [self.path_SWNE()]
        else:
            self.head_type = 'NE'
            self.tail_type = 'NEF'
            self.model = 'NE16NE1F'
            return [self.path_NENE()]

class CharTora(CharTo):
    def __init__(self, name='tora', kana='とら', model='SW16F|NE16F',
    head_type='SW|NE', tail_type='NEF|SWF', to_reverse=None):
        super().__init__(name, kana, model, head_type, tail_type)
        self.to_flick = True

