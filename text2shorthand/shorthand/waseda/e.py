from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    endknot,
    knot,
    smoothknot,
    tensioncurve, 
    controlcurve,
    curve,
    path as mpath)

class CharE(WasedaChar):
    def __init__(self, name='e', kana='え', model='SE4', head_type='SE', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 2

    @classmethod
    def path_SE(cls, ta=-60):
        ta= -45
        return pyx.path.line(0, 0, *PP(4, ta))

    @classmethod
    def path_SENE(cls, ta=-60):
        return pyx.path.path(
            *cls.path_SE(),
            pyx.path.rlineto(*PP(1, 45)))

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') == 'SE':
            if self.tail_type.endswith('NEF'):
                return [self.path_SENE(self.before.tail_angle+170)]
            else:
                path = self.path_SE(self.before.tail_angle+170)
        else:
            if self.tail_type.endswith('NEF'):
                return [self.path_SENE()]
            else:
                path = self.path_SE()

        if self.tail_type == 'SEF':
            return [path]

        if getattr(self.after, 'head_type', '') in {'SR', 'SE'}:
            return self.jog([path])
        elif getattr(self.after, 'head_type', '') == 'EL':
            return self.jog([path], length = 0.3) 
        else:
            return [path]

class CharKangae(CharE):
    def __init__(self):
        super().__init__(name='kangae', kana='え')

class CharEn(CharE):
    def __init__(self):
        super().__init__(name='en', kana='えん', tail_type='NEF')

class CharEku(CharE):
    def __init__(self):
        super().__init__(name='en', kana='えく', head_type='BSE')

    def draw(self, canvas, linewidth=0.3, color=None):
        self.paths = self.barb(self.paths)
        super().draw(canvas, linewidth)

class CharEtsu(CharE):
    def __init__(self, name='etsu', kana='えつ', model='CR1SE4', head_type='CR1', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 2

    @classmethod
    def path_CRSE(cls, ta=None, **kwargs):
        #M 48.648192,55.649308 C 47.132035,56.220999 45.609894,55.835104 45.405607,54.730411 45.258329,53.933999 46.43975,51.62983 47.351786,53.275743 49.204743,56.619697 51.003251,59.745855 52.732687,62.595723

        #z0 = P(0, -0)
        #c0 = P(-0.534866, -0.20168)
        #c1 = P(-1.07184, -0.0655447)
        #z1 = P(-1.14391, 0.324166)
        #c2 = P(-1.19587, 0.605123)
        #c3 = P(-0.779089, 1.41798)
        #z2 = P(-0.457343, 0.837341)
        #c4 = P(0.196339, -0.342332)
        #c5 = P(0.830812, -1.44517)
        z3 = P(1.44092, -2.45054)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.534866, -0.20168)
        #z1 = z0 + P(-1.14391, 0.324166)
        #c1 = z1 + P(0.0720679, -0.389711)
        #c2 = z1 + P(-0.0519564, 0.280956)
        #z2 = z1 + P(0.686569, 0.513175)
        #c3 = z2 + P(-0.321746, 0.580642)
        #c4 = z2 + P(0.653682, -1.17967)
        #z3 = z2 + P(1.89826, -3.28788)
        #c5 = z3 + P(-0.610107, 1.00537)

        z0 = P(0, -0)
        c0 = z0 + PP(0.571627, -159)
        z1 = z0 + PP(1.18896, 164)
        c1 = z1 + PP(0.396319, -79)
        c2 = z1 + PP(0.28572, 100)
        z2 = z1 + PP(0.857161, 36)
        #z2 = z3 - PP(3.79652, ta + 0)
        c3 = z2 + PP(0.663826, 118)
        c4 = z2 + PP(1.34868, -61)
        z3 = z2 + PP(3.79652, -59)
        c5 = z3 + PP(1.17601, 121)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_XCRSE(cls, ta=None, **kwargs):
        #M 50.046618,54.467581 C 49.671996,55.151631 48.37988,55.634402 47.422897,55.633104 46.686215,55.632105 45.641412,55.498912 45.405607,54.730411 45.168027,53.956125 46.43975,51.62983 47.351786,53.275743 49.204743,56.619697 51.003251,59.745855 52.732687,62.595723

        #z0 = P(0, -0)
        #c0 = P(-0.132158, -0.241318)
        #c1 = P(-0.587988, -0.411629)
        #z1 = P(-0.92559, -0.411171)
        #c2 = P(-1.18548, -0.410818)
        #c3 = P(-1.55406, -0.363831)
        #z2 = P(-1.63725, -0.0927206)
        #c4 = P(-1.72106, 0.18043)
        #c5 = P(-1.27242, 1.0011)
        #z3 = P(-0.950677, 0.420454)
        #c6 = P(-0.296995, -0.759219)
        #c7 = P(0.337479, -1.86206)
        z4 = P(0.947585, -2.86743)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.132158, -0.241318)
        #z1 = z0 + P(-0.92559, -0.411171)
        #c1 = z1 + P(0.337602, -0.000457906)
        #c2 = z1 + P(-0.259885, 0.000352425)
        #z2 = z1 + P(-0.711655, 0.31845)
        #c3 = z2 + P(0.0831868, -0.27111)
        #c4 = z2 + P(-0.0838129, 0.273151)
        #z3 = z2 + P(0.686569, 0.513175)
        #c5 = z3 + P(-0.321746, 0.580642)
        #c6 = z3 + P(0.653682, -1.17967)
        #z4 = z3 + P(1.89826, -3.28788)
        #c7 = z4 + P(-0.610107, 1.00537)

        z0 = P(0, -0)
        c0 = z0 + PP(0.275136, -118)
        z1 = z0 + PP(1.01281, -156)
        c1 = z1 + PP(0.337603, 0)
        c2 = z1 + PP(0.259885, 179)
        z2 = z1 + PP(0.779656, 155)
        c3 = z2 + PP(0.283585, -72)
        c4 = z2 + PP(0.28572, 107)
        z3 = z2 + PP(0.857161, 36)
        #z3 = z4 - PP(3.79652, ta + 0)
        c5 = z3 + PP(0.663826, 118)
        c6 = z3 + PP(1.34868, -61)
        z4 = z3 + PP(3.79652, -59)
        c7 = z4 + PP(1.17601, 121)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {'', 'P'}:
            if self.name in {'echi', 'mochi'}:
                path = self.path_XCRSE()
            else:
                path = self.path_CRSE()
        else:
            path = self.path_SE()

        if getattr(self.after, 'head_type', '') in {'SR', 'SE'}:
            return self.jog([path])
        elif getattr(self.after, 'head_type', '') == 'EL':
            return self.jog([path], 0.3)
        else:
            return [path]

    def set_next_head(self):
        if getattr(self.before, 'tail_type', 'P') != 'P':
            self.head = self.before.head + self.before.get_pos_tsux() - self.get_pos_xtsu()

        super().set_next_head()

class CharEchi(CharEtsu):
    def __init__(self, name='echi', kana='えち', model='XCR1SE4', head_type='XCR1', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharMotsu(CharEtsu):
    def __init__(self, name='motsu', kana='もつ', model='CR1SE4', head_type='CR1', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharMochi(CharMotsu):
    def __init__(self, name='mochi', kana='もち', model='XCR1SE4', head_type='XCR1', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharEru(WasedaChar):
    def __init__(self, name='eru', kana='える', model='CSEL4', head_type='SE',
    tail_type='NWL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'ELCL1', 'EL16CL1', 'NECL1', 'NEL8CL1',
        'NEL16CL1', 'NELCL1', 'NEL8CL4', 'NECWL4', 'CNEL4', 'NEL', 'NER', 'OL',
        'NERCR1', 'NEROR4'}
        self.tail_ligature = {}

    @classmethod
    def path_CSEL(cls, ta=None, **kwargs):
        #M 40.670877,58.870121 C 40.670877,60.879404 42.333669,63.011502 43.801655,64.630416 44.768079,65.696201 46.990649,67.642971 47.374699,67.051621 47.943699,65.831421 42.286235,59.249753 40.657435,58.873753

        #z0 = P(0, -0)
        #c0 = P(0, -0.70883)
        #c1 = P(0.586596, -1.46099)
        #z1 = P(1.10447, -2.0321)
        #c2 = P(1.4454, -2.40809)
        #c3 = P(2.22948, -3.09487)
        #z2 = P(2.36496, -2.88625)
        #c4 = P(2.56569, -2.45579)
        #c5 = P(0.569862, -0.133926)
        z3 = P(-0.00474204, -0.00128129)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.70883)
        #z1 = z0 + P(1.10447, -2.0321)
        #c1 = z1 + P(-0.517873, 0.571117)
        #c2 = z1 + P(0.340933, -0.375985)
        #z2 = z1 + P(1.26049, -0.854147)
        #c3 = z2 + P(-0.135484, -0.208615)
        #c4 = z2 + P(0.200731, 0.430459)
        #z3 = z2 + P(-2.3697, 2.88497)
        #c5 = z3 + P(0.574604, -0.132644)

        z0 = P(0, -0)
        c0 = z0 + PP(0.70883, -90)
        z1 = z0 + PP(2.31286, -61)
        c1 = z1 + PP(0.770952, 132)
        c2 = z1 + PP(0.507543, -47)
        z2 = z1 + PP(1.52263, -34)
        #z2 = z3 - PP(3.73344, ta + 321)
        c3 = z2 + PP(0.248749, -123)
        c4 = z2 + PP(0.474961, 64)
        z3 = z2 + PP(3.73344, 129)
        c5 = z3 + PP(0.589716, -12)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_elcl1CSEL(cls, ta=None, **kwargs):
        #M 40.670877,58.870121 C 41.838342,60.379062 43.247769,62.355728 44.635559,64.018887 45.508296,65.064795 47.245322,67.744767 47.374699,67.051621 47.989938,63.755431 43.319633,58.216355 40.657435,58.873753

        #z0 = P(0, -0)
        #c0 = P(0.411856, -0.532321)
        #c1 = P(0.90907, -1.22964)
        #z1 = P(1.39865, -1.81637)
        #c2 = P(1.70653, -2.18534)
        #c3 = P(2.31932, -3.13078)
        #z2 = P(2.36496, -2.88625)
        #c4 = P(2.582, -1.72343)
        #c5 = P(0.934422, 0.230634)
        z3 = P(-0.00474204, -0.00128129)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.411856, -0.532321)
        #z1 = z0 + P(1.39865, -1.81637)
        #c1 = z1 + P(-0.489581, 0.586726)
        #c2 = z1 + P(0.307882, -0.368973)
        #z2 = z1 + P(0.966308, -1.06988)
        #c3 = z2 + P(-0.0456413, -0.244527)
        #c4 = z2 + P(0.217043, 1.16282)
        #z3 = z2 + P(-2.3697, 2.88497)
        #c5 = z3 + P(0.939164, 0.231915)

        z0 = P(0, -0)
        c0 = z0 + PP(0.673046, -52)
        z1 = z0 + PP(2.29247, -52)
        c1 = z1 + PP(0.764158, 129)
        c2 = z1 + PP(0.480554, -50)
        z2 = z1 + PP(1.44166, -47)
        #z2 = z3 - PP(3.73344, ta + 296)
        c3 = z2 + PP(0.24875, -100)
        c4 = z2 + PP(1.1829, 79)
        z3 = z2 + PP(3.73344, 129)
        c5 = z3 + PP(0.967375, 13)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_nel8cl1CSEL(cls, ta=None, **kwargs):
        return cls.path_elcl1CSEL()

class CharSeki(CharEru):
    def __init__(self, name='seki', kana='せき', model='CSEL4', head_type='SE',
    tail_type='NWL'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharZeki(CharEru):
    def __init__(self, name='zeki', kana='ぜき', model='CSEL4', head_type='SE',
    tail_type='NWL'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSeme(CharEru):
    def __init__(self, name='seme', kana='せめ', model='CSEL4', head_type='SE',
    tail_type='NWL'):
        super().__init__(name, kana, model, head_type, tail_type)
