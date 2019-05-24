from ..waseda.char import WasedaChar
from ..waseda.su import CharSu
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

class CharSun(CharSu):
    def __init__(self, name='sun', kana='すん',
                 model='NEL8CL4NE1F|SWR8CR4NE1F', head_type='NEL|SWR',
                 tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.model = 'SWR8CR4NE1F'
            self.head_type = 'SWR'
            self.tail_type = 'NEF'
            self.head_ligature = {'ER', 'NER'}
            self.tail_ligature = {}

            return super(WasedaChar, self).get_paths()
        else:
            self.model = 'NEL8CL4NE1F'
            self.head_type = 'NEL'
            self.tail_type = 'NEF'
            self.head_ligature = {'SEL', 'SL', 'SWL'}
            self.tail_ligature = {}

            return super(WasedaChar, self).get_paths()

    @classmethod
    def path_NELCLNEF(cls, ta=None, **kwargs):
        #M 257.495,106.89 C 263.225,103.714 274.65135,98.806744 273.896,91.5963 273.41282,86.983919 262.3878,93.979303 264.233,99.2493 264.89663,101.14466 268.16047,100.2385 269.685,99.2493 271.61164,97.999182 275.10102,95.118948 275.10102,95.118948

        #z0 = P(0, -0)
        #c0 = P(2.02142, 1.12042)
        #c1 = P(6.05238, 2.85159)
        #z1 = P(5.78591, 5.39528)
        #c2 = P(5.61545, 7.02242)
        #c3 = P(1.72607, 4.55461)
        #z2 = P(2.37702, 2.69547)
        #c4 = P(2.61113, 2.02683)
        #c5 = P(3.76254, 2.3465)
        #z3 = P(4.30036, 2.69547)
        #c6 = P(4.98004, 3.13648)
        #c7 = P(6.21101, 4.15257)
        z4 = P(6.21101, 4.15257)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.02142, 1.12042)
        #z1 = z0 + P(5.78591, 5.39528)
        #c1 = z1 + P(0.266471, -2.54368)
        #c2 = z1 + P(-0.170455, 1.62715)
        #z2 = z1 + P(-3.40889, -2.69981)
        #c3 = z2 + P(-0.650946, 1.85914)
        #c4 = z2 + P(0.234114, -0.668641)
        #z3 = z2 + P(1.92334, 0)
        #c5 = z3 + P(-0.53782, -0.348968)
        #c6 = z3 + P(0.679676, 0.441014)
        #z4 = z3 + P(1.91065, 1.4571)
        #c7 = z4 + P(0, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31116, 28)
        z1 = z0 + PP(7.91112, 42)
        c1 = z1 + PP(2.5576, -84)
        c2 = z1 + PP(1.63605, 95)
        z2 = z1 + PP(4.34851, -141)
        c3 = z2 + PP(1.9698, 109)
        c4 = z2 + PP(0.708442, -70)
        z3 = z2 + PP(1.92334, 0)
        #z3 = z4 - PP(2.40286, ta + 217)
        c5 = z3 + PP(0.641116, -147)
        c6 = z3 + PP(0.810217, 32)
        #z4 = z3 + PP(2.40286, 37)
        c7 = z4 + PP(0, 0)

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

    @classmethod
    def path_selNELCLNE(cls, ta=None, **kwargs):
        #M 63.614331,265.83723 C 70.165657,265.83723 76.155303,255.54649 75.399953,248.33605 74.916773,243.72367 63.891753,250.71905 65.736953,255.98905 66.400583,257.88441 69.537104,256.74674 71.188953,255.98905 73.234194,255.05091 74.971255,253.45614 76.604973,251.8587

        #z0 = P(0, -0)
        #c0 = P(2.31116, -0)
        #c1 = P(4.42418, 3.63034)
        #z1 = P(4.15771, 6.17403)
        #c2 = P(3.98725, 7.80117)
        #c3 = P(0.0978683, 5.33336)
        #z2 = P(0.748814, 3.47422)
        #c4 = P(0.982928, 2.80558)
        #c5 = P(2.08942, 3.20692)
        #z3 = P(2.67216, 3.47422)
        #c6 = P(3.39367, 3.80517)
        #c7 = P(4.00647, 4.36777)
        z4 = P(4.58281, 4.93131)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.31116, 0)
        #z1 = z0 + P(4.15771, 6.17403)
        #c1 = z1 + P(0.266471, -2.54368)
        #c2 = z1 + P(-0.170455, 1.62715)
        #z2 = z1 + P(-3.40889, -2.69981)
        #c3 = z2 + P(-0.650946, 1.85914)
        #c4 = z2 + P(0.234114, -0.668641)
        #z3 = z2 + P(1.92334, 0)
        #c5 = z3 + P(-0.582736, -0.267296)
        #c6 = z3 + P(0.721516, 0.330955)
        #z4 = z3 + P(1.91065, 1.4571)
        #c7 = z4 + P(-0.576339, -0.563541)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31116, 0)
        z1 = z0 + PP(7.44346, 56)
        c1 = z1 + PP(2.5576, -84)
        c2 = z1 + PP(1.63605, 95)
        z2 = z1 + PP(4.34851, -141)
        c3 = z2 + PP(1.9698, 109)
        c4 = z2 + PP(0.708442, -70)
        z3 = z2 + PP(1.92334, 0)
        #z3 = z4 - PP(2.40286, ta + 352)
        c5 = z3 + PP(0.641115, -155)
        c6 = z3 + PP(0.793798, 24)
        #z4 = z3 + PP(2.40286, 37)
        c7 = z4 + PP(0.806068, -135)

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

    @classmethod
    def path_SWRCRNEF(cls, ta=None, **kwargs):
        #M 409.622,307.442 C 410.592,315.335 406.83,327.443 402.483,326.91 396.778,326.209 403.17849,320.65665 409.443,316.192 410.64276,315.33694 411.32536,314.91087 412.69751,313.99864

        #z0 = P(0, -0)
        #c0 = P(0.342194, -2.78447)
        #c1 = P(-0.984956, -7.05591)
        #z1 = P(-2.51848, -6.86788)
        #c2 = P(-4.53108, -6.62058)
        #c3 = P(-2.27313, -4.66183)
        #z2 = P(-0.0631472, -3.08681)
        #c4 = P(0.360101, -2.78516)
        #c5 = P(0.600908, -2.63485)
        z3 = P(1.08497, -2.31304)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.342194, -2.78447)
        #z1 = z0 + P(-2.51848, -6.86788)
        #c1 = z1 + P(1.53352, -0.188031)
        #c2 = z1 + P(-2.0126, 0.247297)
        #z2 = z1 + P(2.45533, 3.78107)
        #c3 = z2 + P(-2.20998, -1.57503)
        #c4 = z2 + P(0.423249, 0.301646)
        #z3 = z2 + P(1.14812, 0.773769)
        #c5 = z3 + P(-0.484064, -0.321814)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80542, -82)
        z1 = z0 + PP(7.31509, -110)
        c1 = z1 + PP(1.54501, -6)
        c2 = z1 + PP(2.02773, 172)
        z2 = z1 + PP(4.50834, 57)
        #z2 = z3 - PP(1.38452, ta + 359)
        c3 = z2 + PP(2.7138, -144)
        c4 = z2 + PP(0.51974, 35)
        #z3 = z2 + PP(1.38452, 33)
        c5 = z3 + PP(0.581277, -146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])


