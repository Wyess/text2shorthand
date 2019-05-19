import math
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


class CharWa(WasedaChar):
    def __init__(self, name='wa', kana='わ',
                 model='UWL4', head_type='SWL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'ECL1', 'NEL8CL1', 'NEL8CL4', 'SWRCR4'}

    @classmethod
    def path_UWL(cls, ta=None, **kwargs):
        #M 47.3414,58.6772 C 44.5656,59.468982 42.1255,61.8061 42.1255,64.6774 42.1255,67.5206 45.5236,69.1216 48.5106,67.7917

        #z0 = P(0, -0)
        #c0 = P(-0.975582, -0.27828)
        #c1 = P(-1.83318, -1.09968)
        #z1 = P(-1.83318, -2.10883)
        #c2 = P(-1.83318, -3.1081)
        #c3 = P(-0.638884, -3.67079)
        #z2 = P(0.410927, -3.20338)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.975582, -0.27828)
        #z1 = z0 + P(-1.83318, -2.10883)
        #c1 = z1 + P(0, 1.00915)
        #c2 = z1 + P(0, -0.999271)
        #z2 = z1 + P(2.24411, -1.09455)
        #c3 = z2 + P(-1.04981, -0.467406)

        z0 = P(0, -0)
        c0 = z0 + PP(1.0145, -164)
        z1 = z0 + PP(2.79423, -131)
        #z1 = z2 - PP(2.49681, ta + 309)
        c1 = z1 + PP(1.00915, 90)
        c2 = z1 + PP(0.999271, -90)
        z2 = z1 + PP(2.49681, -26)
        c3 = z2 + PP(1.14916, -155)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_UWL_up(cls, ta=24, da=0, **kwargs):
        #M47.3414 58.6772C44.5656 59.7427 42.1255 61.8061 42.1255 64.6774C42.1255 67.5206 45.5236 69.1216 48.5106 67.7917

        #z0 = P(0, -0)
        #c0 = P(-0.975582, -0.37448)
        #c1 = P(-1.83318, -1.09968)
        #z1 = P(-1.83318, -2.10883)
        #c2 = P(-1.83318, -3.1081)
        #c3 = P(-0.638884, -3.67079)
        #z2 = P(0.410927, -3.20338)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.975582, -0.37448)
        #z1 = z0 + P(-1.83318, -2.10883)
        #c1 = z1 + P(0, 1.00915)
        #c2 = z1 + P(0, -0.999271)
        #z2 = z1 + P(2.24411, -1.09455)
        #c3 = z2 + P(-1.04981, -0.467406)

        z0 = P(0, -0)
        c0 = z0 + PP(1.04499, -159)
        z1 = z0 + PP(2.79423, -131)
        #z1 = z2 - PP(2.49681, ta + 309)
        c1 = z1 + PP(1.00915, 90)
        #c2 = z1 + PP(0.999271, -90)
        z2 = z1 + PP(2.49681, -26) + P(0.5, 0)
        #c3 = z2 + PP(1.14916, -155)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            tensioncurve(1.2),
            endknot(*z2, angle=ta+90+da)])

    @classmethod
    def path_UWL_smooth(cls, ta=24, **kwargs):
        #M 140.394,124.485 C 137.618,125.55 134.64966,127.88811 135.178,130.485 135.65009,132.80543 138.64443,134.72371 141.563,133.599

        #z0 = P(0, -0)
        #c0 = P(-0.975653, -0.374305)
        #c1 = P(-2.01891, -1.19606)
        #z1 = P(-1.83321, -2.10876)
        #c2 = P(-1.66729, -2.9243)
        #c3 = P(-0.614904, -3.5985)
        z2 = P(0.410857, -3.20321)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.975653, -0.374305)
        #z1 = z0 + P(-1.83321, -2.10876)
        #c1 = z1 + P(-0.18569, 0.912703)
        #c2 = z1 + P(0.165921, -0.815538)
        #z2 = z1 + P(2.24407, -1.09445)
        #c3 = z2 + P(-1.02576, -0.39529)

        z0 = P(0, -0)
        c0 = z0 + PP(1.04499, -159)
        z1 = z0 + PP(2.7942, -131)
        #z1 = z2 - PP(2.49673, ta + 313)
        c1 = z1 + PP(0.931401, 101)
        #c2 = z1 + PP(0.832245, -78)
        #z2 = z1 + PP(2.49673, -25)
        #c3 = z2 + PP(1.09929, -158)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_UWL_upright(cls, ta=None, **kwargs):
        #M 532.653,710.481 C 531.53312,712.70883 530.66646,714.83279 530.66646,717.69279 530.66646,720.52579 534.07546,722.17279 537.02846,720.79579

        #z0 = P(0, -0)
        #c0 = P(-0.395069, -0.785929)
        #c1 = P(-0.700807, -1.53521)
        #z1 = P(-0.700807, -2.54416)
        #c2 = P(-0.700807, -3.54358)
        #c3 = P(0.501812, -4.1246)
        z2 = P(1.54357, -3.63883)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.395069, -0.785929)
        #z1 = z0 + P(-0.700807, -2.54416)
        #c1 = z1 + P(0, 1.00894)
        #c2 = z1 + P(0, -0.999419)
        #z2 = z1 + P(2.24437, -1.09467)
        #c3 = z2 + P(-1.04175, -0.485775)

        z0 = P(0, -0)
        c0 = z0 + PP(0.879638, -116)
        z1 = z0 + PP(2.63892, -105)
        #z1 = z2 - PP(2.4971, ta + 309)
        c1 = z1 + PP(1.00894, 90)
        c2 = z1 + PP(0.999419, -90)
        z2 = z1 + PP(2.4971, -26)
        c3 = z2 + PP(1.14945, -155)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_UWL_upright_up(cls, ta=None, **kwargs):
        #M 532.653,710.481 C 531.53312,712.70883 530.66646,714.83279 530.66646,717.69279 530.66646,720.52579 534.07546,722.17279 537.02846,720.79579

        #z0 = P(0, -0)
        #c0 = P(-0.395069, -0.785929)
        #c1 = P(-0.700807, -1.53521)
        #z1 = P(-0.700807, -2.54416)
        #c2 = P(-0.700807, -3.54358)
        #c3 = P(0.501812, -4.1246)
        z2 = P(1.54357, -3.63883)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.395069, -0.785929)
        #z1 = z0 + P(-0.700807, -2.54416)
        #c1 = z1 + P(0, 1.00894)
        #c2 = z1 + P(0, -0.999419)
        #z2 = z1 + P(2.24437, -1.09467)
        #c3 = z2 + P(-1.04175, -0.485775)

        z0 = P(0, -0)
        c0 = z0 + PP(0.879638, -116)
        z1 = z0 + PP(2.63892, -105)
        #z1 = z2 - PP(2.4971, ta + 309)
        c1 = z1 + PP(1.00894, 90)
        c2 = z1 + PP(0.999419, -90)
        z2 = z1 + PP(2.4971, -26)
        #c3 = z2 + PP(1.14945, -155)
        c3 = z2 + PP(1.14945, -120)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_UWLe(cls, ta=None, **kwargs):
        #M 47.3414,124.485 C 44.5656,125.55 41.597148,127.88814 42.1255,130.485 42.597614,132.80545 44.153501,133.599 48.5106,133.599

        #z0 = P(0, -0)
        #c0 = P(-0.975582, -0.374305)
        #c1 = P(-2.01887, -1.19607)
        #z1 = P(-1.83318, -2.10876)
        #c2 = P(-1.66725, -2.9243)
        #c3 = P(-1.12042, -3.20321)
        z2 = P(0.410927, -3.20321)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.975582, -0.374305)
        #z1 = z0 + P(-1.83318, -2.10876)
        #c1 = z1 + P(-0.185695, 0.912692)
        #c2 = z1 + P(0.165929, -0.815545)
        #z2 = z1 + P(2.24411, -1.09445)
        #c3 = z2 + P(-1.53135, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(1.04492, -159)
        #z1 = z0 + PP(2.79417, -131)
        z1 = z2 - PP(2.49676, ta + -25)
        c1 = z1 + PP(0.931391, 101)
        #c2 = z1 + PP(0.832254, -78)
        #z2 = z1 + PP(2.49676, -25)
        #c3 = z2 + PP(1.53135, 180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_UWLer(cls, ta=30, **kwargs):
        return cls.path_UWL_smooth(ta=ta)

    @classmethod
    def path_UWLel(cls, ta=None, **kwargs):
        return cls.path_UWL_up(ta=ta) 

    @classmethod
    def path_UWLne(cls, ta=None, **kwargs):
        #M 47.3414,190.223 C 43.854505,191.64387 39.459656,198.27509 44.662924,199.67149 46.540136,200.13108 48.727579,199.09861 50.203729,197.96392

        #z0 = P(0, -0)
        #c0 = P(-1.2255, -0.499379)
        #c1 = P(-2.77012, -2.82999)
        #z1 = P(-0.941377, -3.32077)
        #c2 = P(-0.281612, -3.48229)
        #c3 = P(0.487186, -3.11942)
        z2 = P(1.00599, -2.72062)

        #z0 = P(0, -0)
        #c0 = z0 + P(-1.2255, -0.499379)
        #z1 = z0 + P(-0.941377, -3.32077)
        #c1 = z1 + P(-1.82874, 0.490779)
        #c2 = z1 + P(0.659765, -0.161527)
        #z2 = z1 + P(1.94737, 0.600142)
        #c3 = z2 + P(-0.518807, -0.398798)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32334, -157)
        z1 = z0 + PP(3.45162, -105)
        #z1 = z2 - PP(2.03775, ta + 339)
        c1 = z1 + PP(1.89345, 164)
        #c2 = z1 + PP(0.67925, -13)
        #z2 = z1 + PP(2.03775, 17)
        #c3 = z2 + PP(0.654371, -142)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_UWLner(cls, ta=None, **kwargs):
        #M 124.215,190.223 C 121.451,191.016 119.12678,193.56302 119.019,196.201 118.91743,198.68695 120.59165,199.54968 122.14222,199.66589 123.68863,199.78179 124.71184,199.06234 125.73735,196.71319

        #z0 = P(0, -0)
        #c0 = P(-0.971435, -0.278708)
        #c1 = P(-1.78831, -1.17388)
        #z1 = P(-1.82619, -2.10103)
        #c2 = P(-1.86188, -2.97474)
        #c3 = P(-1.27346, -3.27795)
        #z2 = P(-0.728499, -3.3188)
        #c4 = P(-0.184998, -3.35953)
        #c5 = P(0.174619, -3.10667)
        z3 = P(0.535045, -2.28104)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.971435, -0.278708)
        #z1 = z0 + P(-1.82619, -2.10103)
        #c1 = z1 + P(0.0378803, 0.927144)
        #c2 = z1 + P(-0.0356978, -0.873712)
        #z2 = z1 + P(1.09769, -1.21777)
        #c3 = z2 + P(-0.544963, 0.0408432)
        #c4 = z2 + P(0.543501, -0.0407342)
        #z3 = z2 + P(1.26354, 1.03776)
        #c5 = z3 + P(-0.360426, -0.825632)

        z0 = P(0, -0)
        c0 = z0 + PP(1.01063, -163)
        z1 = z0 + PP(2.78375, -130)
        c1 = z1 + PP(0.927918, 87)
        c2 = z1 + PP(0.874441, -92)
        #z2 = z1 + PP(1.63948, -47)
        z2 = z3 - PP(1.63508, ta + 332)
        c3 = z2 + PP(0.546492, 175)
        #c4 = z2 + PP(0.545025, -4)
        #z3 = z2 + PP(1.63508, 39)
        #c5 = z3 + PP(0.900874, -113)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_UWLnel(cls, ta=None, **kwargs):
        return cls.path_UWL_smooth(ta=ta)

    @classmethod
    def path_UWLs(cls, ta=None, **kwargs):
        return cls.path_UWL_up(ta=ta,da=40)

    @classmethod
    def path_UWLsl(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def path_UWLsr(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def path_UWLse(cls, ta=None, **kwargs):
        return cls.path_UWL_up(ta=ta)

    @classmethod
    def path_UWLser(cls, ta=None, **kwargs):
        #M 82.5249,329.871 C 79.7605,330.663 77.3284,332.988 77.3284,335.848 77.3284,338.681 81.092813,339.63669 83.779038,340.91644

        #z0 = P(0, -0)
        #c0 = P(-0.971576, -0.278356)
        #c1 = P(-1.82636, -1.0955)
        #z1 = P(-1.82636, -2.10068)
        #c2 = P(-1.82636, -3.09636)
        #c3 = P(-0.503321, -3.43225)
        z2 = P(0.440779, -3.88203)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.971576, -0.278356)
        #z1 = z0 + P(-1.82636, -2.10068)
        #c1 = z1 + P(0, 1.00518)
        #c2 = z1 + P(0, -0.995686)
        #z2 = z1 + P(2.26714, -1.78135)
        #c3 = z2 + P(-0.9441, 0.449781)

        z0 = P(0, -0)
        c0 = z0 + PP(1.01066, -164)
        #z1 = z0 + PP(2.7836, -131)
        z1 = z2 - PP(2.88325, ta + -12)
        c1 = z1 + PP(1.00518, 90)
        #c2 = z1 + PP(0.995686, -90)
        #z2 = z1 + PP(2.88325, -38)
        #c3 = z2 + PP(1.04577, 154)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_UWLsel(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def path_UWLsw(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def path_UWLswr(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def path_UWLswl(cls, ta=None, **kwargs):
        return cls.path_UWL()

    @classmethod
    def _path_UWL_upright(cls, ta=26, **kwargs):
        #M 394.96332,388.27664 C 393.15736,389.81556 392.05736,392.033 392.05736,394.894 392.05736,397.726 395.46636,399.373 398.41836,397.996

        #z0 = P(0, -0)
        #c0 = P(-0.637103, -0.542897)
        #c1 = P(-1.02516, -1.32516)
        #z1 = P(-1.02516, -2.33446)
        #c2 = P(-1.02516, -3.33352)
        #c3 = P(0.177461, -3.91455)
        z2 = P(1.21886, -3.42877)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.637103, -0.542897)
        #z1 = z0 + P(-1.02516, -2.33446)
        #c1 = z1 + P(0, 1.0093)
        #c2 = z1 + P(0, -0.999067)
        #z2 = z1 + P(2.24402, -1.09432)
        #c3 = z2 + P(-1.0414, -0.485775)

        z0 = P(0, -0)
        c0 = z0 + PP(0.83704, -139)
        z1 = z0 + PP(2.54964, -113)
        #z1 = z2 - PP(2.49663, ta + 309)
        c1 = z1 + PP(1.0093, 90)
        c2 = z1 + PP(0.999067, -90)
        #z2 = z1 + PP(2.49663, -25)
        #c3 = z2 + PP(1.14913, -154)
        c3 = z2 + PP(1.14913, ta-180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_ecl1UWL(cls, ta=26, **kwargs):
        return cls.path_UWL_upright(ta=ta)

    @classmethod
    def path_ecl1UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLsw(cls, ta=None, **kwargs):
        return cls.path_ecl1UWL()

    @classmethod
    def path_ecl1UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ecl1UWLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWL(cls, ta=None, **kwargs):
        return cls.path_UWL_upright()

    @classmethod
    def path_nel8cl1UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLsw(cls, ta=None, **kwargs):
        return cls.path_UWL_upright()

    @classmethod
    def path_nel8cl1UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl1UWLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWL(cls, ta=None, **kwargs):
        return cls.path_UWL_upright()
        
    @classmethod
    def path_nel8cl4UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLsw(cls, ta=None, **kwargs):
        return cls.path_UWL_upright()

    @classmethod
    def path_nel8cl4UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nel8cl4UWLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWL(cls, ta=None, **kwargs):
        return cls.path_UWL_upright()

    @classmethod
    def path_swrcr4UWLe(cls, ta=None, **kwargs):
        #M 17520.5,17.3937 C 17519.4,19.6348 17518.203,22.287313 17518.5,24.6192 17518.856,27.416918 17522.197,30.100121 17524.9,27.7221

        #z0 = P(0, -0)
        #c0 = P(-0.388056, -0.79061)
        #c1 = P(-0.810331, -1.72636)
        #z1 = P(-0.705556, -2.549)
        #c2 = P(-0.579967, -3.53597)
        #c3 = P(0.598664, -4.48254)
        z2 = P(1.55222, -3.64363)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.388056, -0.79061)
        #z1 = z0 + P(-0.705556, -2.549)
        #c1 = z1 + P(-0.104775, 0.822638)
        #c2 = z1 + P(0.125589, -0.986973)
        #z2 = z1 + P(2.25778, -1.09463)
        #c3 = z2 + P(-0.953558, -0.838913)

        z0 = P(0, -0)
        c0 = z0 + PP(0.880711, -116)
        z1 = z0 + PP(2.64484, -105)
        #z1 = z2 - PP(2.50914, ta + 293)
        c1 = z1 + PP(0.829283, 97)
        c2 = z1 + PP(0.994931, -82)
        z2 = z1 + PP(2.50914, -25)
        c3 = z2 + PP(1.27006, -138)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_swrcrUWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swrcrUWLswl(cls, ta=None, **kwargs):
        pass

class CharWan(CharWa):
    def __init__(self, name='wan', kana='わん',
                 model='UWL4F', head_type='SWL', tail_type='SELF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') == 'ECL1':
            return [self.path_UWL_upright()]
        else:
            return [self.path_UWL_up(-45, 0)]

class CharWaku(CharWa):
    def __init__(self, name='waku', kana='わく',
                 model='BUWL4', head_type='BSWL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharWatsu(CharWa):
    def __init__(self, name='watsu', kana='わつ',
                 model='CL1UWL4', head_type='CL1SWL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharRare(CharWa):
    def __init__(self, name='rare', kana='られ',
                 model='PUWL4', head_type='P', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}

    def get_paths(self):
        return super(WasedaChar, self).get_paths(me='UWL')

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        self.head = self.before.head + self.before.get_pos_rare()
        super().set_next_head()

class CharRareru(CharRare):
    def __init__(self, name='rareru', kana='られる',
                 model='PUWL4S1F', head_type='P', tail_type='SF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_UWLSF()]

    @classmethod
    def path_UWLSF(cls, ta=None, **kwargs):
        #M 52.827226,64.384752 C 49.932313,65.307965 47.630826,67.501952 47.630826,70.362452 47.630826,73.195052 51.039826,74.841752 53.992126,73.465152 53.992126,74.410034 53.992126,75.354916 53.992126,76.299798

        #z0 = P(0, -0)
        #c0 = P(-1.02126, -0.325689)
        #c1 = P(-1.83317, -1.09968)
        #z1 = P(-1.83317, -2.1088)
        #c2 = P(-1.83317, -3.10808)
        #c3 = P(-0.630555, -3.689)
        #z2 = P(0.410951, -3.20336)
        #c4 = P(0.410951, -3.5367)
        #c5 = P(0.410951, -3.87003)
        z3 = P(0.410951, -4.20336)

        #z0 = P(0, -0)
        #c0 = z0 + P(-1.02126, -0.325689)
        #z1 = z0 + P(-1.83317, -2.1088)
        #c1 = z1 + P(0, 1.00912)
        #c2 = z1 + P(0, -0.999278)
        #z2 = z1 + P(2.24413, -1.09456)
        #c3 = z2 + P(-1.04151, -0.485634)
        #c4 = z2 + P(0, -0.333333)
        #z3 = z2 + P(0, -1)
        #c5 = z3 + P(0, 0.333333)

        z0 = P(0, -0)
        c0 = z0 + PP(1.07194, -162)
        z1 = z0 + PP(2.7942, -131)
        c1 = z1 + PP(1.00912, 90)
        c2 = z1 + PP(0.999278, -90)
        z2 = z1 + PP(2.49683, -26)
        #z2 = z3 - PP(1, ta + 0)
        c3 = z2 + PP(1.14916, -155)
        c4 = z2 + PP(0.333333, -90)
        z3 = z2 + PP(1, -90)
        c5 = z3 + PP(0.333333, 90)

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
    def path_UWLSFe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLSFswl(cls, ta=None, **kwargs):
        pass

