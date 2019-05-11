import math
import re
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

class CharHa(WasedaChar):
    def __init__(self, name='ha', kana='は',
                 model='SEL8', head_type='SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SEL(cls, ha=-90, tn=0.8, ta=0, d=-55,
                 sellen=7.3, dz=P(0, 0)):
        return mpath([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(*(PP(sellen, d) + dz), angle=ta)])

    @classmethod
    def path_SEL_smooth(cls, ta=0):
        return cls.path_SEL(ta=ta)

    @classmethod
    def path_SEL_up(cls, ta=60, dz=P(0, 1.4)):
        return cls.path_SEL(ta=ta, dz=dz)

    @classmethod
    def path_SELf(cls, ta=30, dz=P(0, 0.4)):
        return cls.path_SEL(ta=ta, dz=dz)

    @classmethod
    def path_SELnw(cls, ta=0):
        return cls.path_SEL(ta=ta)

    @classmethod
    def path_SELnel(cls, ha=-90, tn=1.5, ta=0):
        return mpath([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(*P(4.5, -math.sqrt(7.6**2 - 4.5**2)), angle=ta)])
        
    def get_paths(self):
        if self.after is None:
            return [self.path_SEL()]
        
        if self.tail_type.endswith('F'):
            return [self.path_SELf()]

        if self.after.head_type in {'E','EL', 'NE', 'NL', 'SW', 'SR', 'SE', 'SEL'}:
            return [self.path_SEL_up()]

        if self.after.head_type == 'NEL':
            return [self.path_SELnel()]

        if self.after.head_type == 'SER':
            return [self.path_SEL_smooth(self.after.head_angle)]
        
        return [self.path_SEL()]


class CharHan(CharHa):
    def __init__(self, name='han', kana='はん',
                 model='SEL8F', head_type='SEL', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharHaku(CharHa):
    def __init__(self, name='haku', kana='はく',
                 model='SEL8F', head_type='BSEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self, **kwargs):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharHatsu(CharHa):
    def __init__(self, name='hatsu', kana='はつ',
                 model='CL1SEL8', head_type='CL1SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'EL', 'E', 'SW', 'NEL', 'NE', 'SE'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()

    @classmethod
    def path_CLSEL_fusion(cls, ta=None, **kwargs):
        #M 47.430412,129.1615 C 47.866197,129.01973 49.773707,128.46644 49.6836,127.579 49.53713,126.13646 47.444,124.445 47.3977,127.093 47.3977,137.798 49.738,142.948 59.3452,142.948

        #z0 = P(0, -0)
        #c0 = P(0.153735, 0.0500133)
        #c1 = P(0.826662, 0.245202)
        #z1 = P(0.794875, 0.558271)
        #c2 = P(0.743203, 1.06717)
        #c3 = P(0.00479354, 1.66388)
        #z2 = P(-0.0115401, 0.729721)
        #c4 = P(-0.0115401, -3.04677)
        #c5 = P(0.814066, -4.86357)
        z3 = P(4.20327, -4.86357)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.153735, 0.0500133)
        #z1 = z0 + P(0.794875, 0.558271)
        #c1 = z1 + P(0.0317877, -0.313069)
        #c2 = z1 + P(-0.0516714, 0.508896)
        #z2 = z1 + P(-0.806415, 0.17145)
        #c3 = z2 + P(0.0163336, 0.934156)
        #c4 = z2 + P(0, -3.77649)
        #z3 = z2 + P(4.21481, -5.59329)
        #c5 = z3 + P(-3.38921, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(0.161666, 18)
        z1 = z0 + PP(0.971335, 35)
        c1 = z1 + PP(0.314679, -84)
        c2 = z1 + PP(0.511513, 95)
        z2 = z1 + PP(0.824439, 167)
        #z2 = z3 - PP(7.00354, ta + -53)
        c3 = z2 + PP(0.934298, 88)
        #c4 = z2 + PP(3.77649, -90)
        #z3 = z2 + PP(7.00354, -53)
        #c5 = z3 + PP(3.38921, 180)

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
    def path_CLSEL_swingup(cls, ta=None, **kwargs):
        #M 124.14222,272.1685 C 125.46851,272.73746 127.0205,272.03649 126.81119,270.72407 126.48726,268.69306 124.01606,267.5455 124.05286,269.95172 124.28893,285.38691 131.977,288.723 135.91,281.911

        #z0 = P(0, -0)
        #c0 = P(0.467886, -0.200716)
        #c1 = P(1.01539, 0.0465702)
        #z1 = P(0.941553, 0.509563)
        #c2 = P(0.827278, 1.22606)
        #c3 = P(-0.0445064, 1.63089)
        #z2 = P(-0.0315242, 0.782031)
        #c4 = P(0.051756, -4.66316)
        #c5 = P(2.76394, -5.84006)
        z3 = P(4.15141, -3.43694)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.467886, -0.200716)
        #z1 = z0 + P(0.941553, 0.509563)
        #c1 = z1 + P(0.0738399, -0.462993)
        #c2 = z1 + P(-0.114275, 0.716495)
        #z2 = z1 + P(-0.973078, 0.272468)
        #c3 = z2 + P(-0.0129822, 0.848861)
        #c4 = z2 + P(0.0832802, -5.44519)
        #z3 = z2 + P(4.18294, -4.21897)
        #c5 = z3 + P(-1.38747, -2.40312)

        z0 = P(0, -0)
        c0 = z0 + PP(0.509121, -23)
        z1 = z0 + PP(1.0706, 28)
        c1 = z1 + PP(0.468844, -80)
        c2 = z1 + PP(0.725551, 99)
        z2 = z1 + PP(1.0105, 164)
        #z2 = z3 - PP(5.9411, ta + 255)
        c3 = z2 + PP(0.84896, 90)
        c4 = z2 + PP(5.44583, -89)
        z3 = z2 + PP(5.9411, -45)
        c5 = z3 + PP(2.7749, -120)

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
    def path_CLSEL(cls, ta=None, **kwargs):
        #M 47.38479,61.727859 C 47.38479,62.255724 49.627111,61.080093 49.723858,60.143329 49.872882,58.70038 47.435984,57.028382 47.433719,59.677728 47.424567,70.382424 49.620065,75.647429 59.227265,75.647429

        #z0 = P(0, -0)
        #c0 = P(0, -0.186219)
        #c1 = P(0.791041, 0.228517)
        #z1 = P(0.825171, 0.558987)
        #c2 = P(0.877744, 1.06803)
        #c3 = P(0.0180601, 1.65787)
        #z2 = P(0.0172611, 0.723241)
        #c4 = P(0.0140324, -3.05314)
        #c5 = P(0.788555, -4.91051)
        z3 = P(4.17776, -4.91051)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.186219)
        #z1 = z0 + P(0.825171, 0.558987)
        #c1 = z1 + P(-0.0341302, -0.33047)
        #c2 = z1 + P(0.0525724, 0.50904)
        #z2 = z1 + P(-0.80791, 0.164254)
        #c3 = z2 + P(0.000799042, 0.93463)
        #c4 = z2 + P(-0.00322862, -3.77638)
        #z3 = z2 + P(4.1605, -5.63376)
        #c5 = z3 + P(-3.38921, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(0.186219, -90)
        z1 = z0 + PP(0.996681, 34)
        c1 = z1 + PP(0.332227, -95)
        c2 = z1 + PP(0.511748, 84)
        z2 = z1 + PP(0.824438, 168)
        #z2 = z3 - PP(7.0035, ta + -53)
        c3 = z2 + PP(0.934631, 89)
        c4 = z2 + PP(3.77638, -90)
        z3 = z2 + PP(7.0035, -53)
        c5 = z3 + PP(3.38921, 180)

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
    def path_CLSELe(cls, ta=None, **kwargs):
        return cls.path_CLSEL_swingup()

    @classmethod
    def path_CLSELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELel(cls, ta=None, **kwargs):
        return cls.path_CLSEL_swingup()

    @classmethod
    def path_CLSELne(cls, ta=None, **kwargs):
        #M 419.775,129.159 C 421.103,129.723 422.685,129.043 422.454,127.734 422.133,125.703 419.701,124.538 419.701,126.945 419.97,142.38 432.79809,143.29075 431.609,138.853

        #z0 = P(0, -0)
        #c0 = P(0.468489, -0.198967)
        #c1 = P(1.02658, 0.0409222)
        #z1 = P(0.945092, 0.502708)
        #c2 = P(0.83185, 1.2192)
        #c3 = P(-0.0261056, 1.63019)
        #z2 = P(-0.0261056, 0.78105)
        #c4 = P(0.0687917, -4.66408)
        #c5 = P(4.59426, -4.98537)
        z3 = P(4.17477, -3.41983)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.468489, -0.198967)
        #z1 = z0 + P(0.945092, 0.502708)
        #c1 = z1 + P(0.0814917, -0.461786)
        #c2 = z1 + P(-0.113242, 0.716492)
        #z2 = z1 + P(-0.971197, 0.278342)
        #c3 = z2 + P(0, 0.849136)
        #c4 = z2 + P(0.0948972, -5.44513)
        #z3 = z2 + P(4.20088, -4.20088)
        #c5 = z3 + P(0.419485, -1.56554)

        z0 = P(0, -0)
        c0 = z0 + PP(0.508989, -23)
        z1 = z0 + PP(1.07047, 28)
        c1 = z1 + PP(0.468921, -79)
        c2 = z1 + PP(0.725385, 98)
        z2 = z1 + PP(1.0103, 164)
        #z2 = z3 - PP(5.94094, ta + 210)
        c3 = z2 + PP(0.849136, 90)
        c4 = z2 + PP(5.44595, -89)
        z3 = z2 + PP(5.94094, -45)
        c5 = z3 + PP(1.62077, -75)

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
    def path_CLSELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELnel(cls, ta=None, **kwargs):
        #M 162.77806,130.35036 C 162.77806,130.87836 164.97751,129.70135 165.12106,128.77036 165.3372,127.36865 161.57416,125.76095 162.18115,128.33885 164.48312,138.11534 171.55212,144.13936 174.78206,144.13936

        #z0 = P(0, -0)
        #c0 = P(0, -0.186267)
        #c1 = P(0.775917, 0.228956)
        #z1 = P(0.826558, 0.557389)
        #c2 = P(0.902808, 1.05188)
        #c3 = P(-0.424709, 1.61904)
        #z2 = P(-0.210577, 0.709616)
        #c4 = P(0.601507, -2.73931)
        #c5 = P(3.09529, -4.86445)
        z3 = P(4.23474, -4.86445)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.186267)
        #z1 = z0 + P(0.826558, 0.557389)
        #c1 = z1 + P(-0.0506413, -0.328433)
        #c2 = z1 + P(0.0762494, 0.494492)
        #z2 = z1 + P(-1.03713, 0.152227)
        #c3 = z2 + P(-0.214133, 0.909426)
        #c4 = z2 + P(0.812084, -3.44893)
        #z3 = z2 + P(4.44532, -5.57407)
        #c5 = z3 + P(-1.13945, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(0.186267, -90)
        z1 = z0 + PP(0.996936, 33)
        c1 = z1 + PP(0.332314, -98)
        c2 = z1 + PP(0.500336, 81)
        z2 = z1 + PP(1.04825, 171)
        #z2 = z3 - PP(7.12959, ta + -51)
        c3 = z2 + PP(0.934296, 103)
        c4 = z2 + PP(3.54325, -76)
        z3 = z2 + PP(7.12959, -51)
        c5 = z3 + PP(1.13945, 180)

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
    def path_CLSELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELse(cls, ta=None, **kwargs):
        return cls.path_CLSEL_swingup()

    @classmethod
    def path_CLSELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELsw(cls, ta=None, **kwargs):
        #M 124.14222,272.1685 C 125.46851,272.73746 127.0205,272.03649 126.81119,270.72407 126.48726,268.69306 124.01606,267.5455 124.05286,269.95172 124.28893,285.38691 131.977,288.723 135.91,281.911

        #z0 = P(0, -0)
        #c0 = P(0.467886, -0.200716)
        #c1 = P(1.01539, 0.0465702)
        #z1 = P(0.941553, 0.509563)
        #c2 = P(0.827278, 1.22606)
        #c3 = P(-0.0445064, 1.63089)
        #z2 = P(-0.0315242, 0.782031)
        #c4 = P(0.051756, -4.66316)
        #c5 = P(2.76394, -5.84006)
        z3 = P(4.15141, -3.43694)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.467886, -0.200716)
        #z1 = z0 + P(0.941553, 0.509563)
        #c1 = z1 + P(0.0738399, -0.462993)
        #c2 = z1 + P(-0.114275, 0.716495)
        #z2 = z1 + P(-0.973078, 0.272468)
        #c3 = z2 + P(-0.0129822, 0.848861)
        #c4 = z2 + P(0.0832802, -5.44519)
        #z3 = z2 + P(4.18294, -4.21897)
        #c5 = z3 + P(-1.38747, -2.40312)

        z0 = P(0, -0)
        c0 = z0 + PP(0.509121, -23)
        z1 = z0 + PP(1.0706, 28)
        c1 = z1 + PP(0.468844, -80)
        c2 = z1 + PP(0.725551, 99)
        z2 = z1 + PP(1.0105, 164)
        #z2 = z3 - PP(5.9411, ta + 255)
        c3 = z2 + PP(0.84896, 90)
        #c4 = z2 + PP(5.44583, -89)
        #z3 = z2 + PP(5.9411, -45)
        #c5 = z3 + PP(2.7749, -120)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta+180)])

    @classmethod
    def path_CLSELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLSELswl(cls, ta=None, **kwargs):
        pass
