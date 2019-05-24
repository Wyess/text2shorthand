import math
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
    path)

class CharSa(WasedaChar):
    def __init__(self, name='sa', kana='さ',
                 model='NEL8|SWR8', head_type='NEL|SWR', tail_type='NEL|SWR'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_NEL(cls, ha=30, tn=1.2, ta=90, d=42, dz=P(0, 0),
                 before=None, after=None):
        if before:
            if before.tail_type == 'EL':
                ha = 0
                d = 42
            elif before.tail_type == 'SWL':
                ha = -60
                d = P(1.2, math.sqrt(7.6**2 - 1.2**2)).a
            elif before.tail_type == 'SL':
                ha = 0
                d = 60
            elif before.tail_type == 'SEL':
                ha = 0
                d = 60
                dz = P(0.5, -0.2)
            else:
                ha = 30
                d = 42

        if after:
            if after.head_type in {'ER', 'E', 'NE'}:
                tn = 1.5
                ta = 120
            elif after.head_type == 'EL':
                tn = 1.2
                ta = 120
            elif after.head_type == 'SW':
                tn = 1.2
                ta = after.head_angle + 180
                dz = P(1.4, 1.4)
            #elif after.head_type in {'SWL', 'S', 'SL'}:
            elif after.head_type in {'S', 'SL'}:
                tn = 1.2
                ta = after.head_angle + 180
            elif after.head_type == 'SWL':
                tn = 1.2
                ha = -30
                ta = after.head_angle + 185
                dz = P(1.0, -3.0)
            else:
                tn = 1.2
                ta = 90

        return path([beginknot(0, 0, angle=ha),
            tensioncurve(tn), 
            endknot(*(PP(7.6, d) + dz), angle=ta)])

    @classmethod
    def path_SWR(cls, ha=-90, tn=1.0, ta=180, d=-120, dz=P(0, 0),
                 before=None, after=None):
        if before:
            if before.tail_type == 'ER':
                ha = -45
                tn = 1.5
            elif before.tail_type == 'NER':
                ha = -40
                tn = 1.5

        if after:
            if after.head_type == 'ER':
                ta = after.head_angle + 180
            elif after.head_type == 'E':
                ta = after.head_angle + 180
            elif after.head_type == 'NER':
                ta = after.head_angle + 180 - 10
                dz = P(2.0, 0)
            elif after.head_type == 'NE':
                ta = after.head_angle + 180
            elif after.head_type == 'NEL':
                ta = after.head_angle + 180
                dz = P(1.0, 0)
            elif after.head_type in {'SW', 'SWR', 'SWL'}:
                ta = 150
                dz = P(0.0, 0.8)

        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(*(PP(7.6, d) + dz), angle=ta)])

    @classmethod
    def path_SWRNE(cls):
        #M 233.677,217.236 C 233.677,226.357 230.55238,231.78754 224.54358,236.71229 225.69526,236.02853 226.84695,235.48196 227.99864,234.65026

        #z0 = P(0, -0)
        #c0 = P(0, -3.21769)
        #c1 = P(-1.1023, -5.13346)
        #z1 = P(-3.22207, -6.8708)
        #c2 = P(-2.81578, -6.62959)
        #c3 = P(-2.40949, -6.43677)
        z2 = P(-2.0032, -6.14336)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.21769)
        #z1 = z0 + P(-3.22207, -6.8708)
        #c1 = z1 + P(2.11977, 1.73734)
        #c2 = z1 + P(0.406287, 0.241215)
        #z2 = z1 + P(1.21887, 0.727438)
        #c3 = z2 + P(-0.406291, -0.293405)

        z0 = P(0, -0)
        c0 = z0 + PP(3.21769, -90)
        z1 = z0 + PP(7.58878, -115)
        #z1 = z2 - PP(1.41944, ta + 354)
        c1 = z1 + PP(2.74076, 39)
        c2 = z1 + PP(0.472498, 30)
        #z2 = z1 + PP(1.41944, 30)
        c3 = z2 + PP(0.501157, -144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def to_reverse(self):
        if getattr(self.before, 'model', '') == 'ER4':
            return False
        else:
            return getattr(self.before, 'tail_type', '') in {
                'ER', 'ERCL1', 'ERCL4',
                'E', 'ECL1', 'ECL4',
                'ELC4',
                'NER', 'NERCL1', 'NERCL4',
                'NE', 'NECL1', 'NECL4',
                'SECL1', 'SECL1', 'SECL4'}

    def get_paths(self):
        if self.to_reverse():
            if self.tail_type.endswith('F'):
                self.tail_type = 'SWRF'
                return [self.path_SWRNE()]

            self.head_type = self.tail_type = 'SWR'

            return [self.path_SWR(before=self.before, after=self.after)]
        else:
            if self.tail_type.endswith('F'):
                self.tail_type = 'NELF'
                if self.before.tail_type == 'SEL':
                    return [self.path_NEL(ha=0, d=60, dz=P(0.5, -0.2), ta=75)]
                return [self.path_NEL(ta=75)]

            self.head_type = self.tail_type = 'NEL'
            return [self.path_NEL(before=self.before, after=self.after)]

class CharSaku(CharSa):
    def __init__(self, name='saku', kana='さく',
                 model='SWR8F', head_type='SWR', tail_type='SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_SWR()]

class CharSatsu(CharSaku):
    def __init__(self, name='satsu', kana='さつ',
                 model='SWR8F', head_type='SWR', tail_type='SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSaku(CharSa):
    def __init__(self, name='saku', kana='さく',
                 model='BNEL8', head_type='BNEL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.head_type.startswith('B') and self.before and self.before.tail_type not in {'', 'P', 'E'}:
            self.head = self.before.tail - self.get_pos_xku()
        super().set_next_head(flick_len=flick_len, dz=dz)

    def get_paths(self):
        before = self.before
        self.before = None
        if getattr(self.before, 'tail_type', '') in {'', 'P', 'E'}:
            paths = self.barb(super().get_paths())
        else:
            paths = super().get_paths()

        self.before = before
        return paths
            
class CharSatsu(CharSa):
    def __init__(self, name='satsu', kana='さつ',
                 model='CL1NEL8|XSWR8', head_type='CLNEL|CRSWR', tail_type='NEL|SWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'ER', 'SW', 'SL', 'NE', 'NER', 'SE'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            self.model='CL1NEL8'
            self.head_type='CLNEL'
            self.tail_type='NEL'
            return super(WasedaChar, self).get_paths(me='CLNEL')
        else:
            paths = super().get_paths()
            self.head_type = f'CL{self.head_type}'
            return paths


    @classmethod
    def path_CLNEL(cls, ta=None, **kwargs):
        #M 49.784806,57.997719 C 49.361812,56.384808 48.783494,55.693718 47.927256,55.999874 47.118751,56.288963 45.397614,58.341565 47.76704,58.57079 51.057874,58.889155 63.3512,50.7863 63.3512,44.2619

        #z0 = P(0, -0)
        #c0 = P(-0.149223, 0.568999)
        #c1 = P(-0.353241, 0.8128)
        #z1 = P(-0.655302, 0.704795)
        #c2 = P(-0.940525, 0.602811)
        #c3 = P(-1.5477, -0.121301)
        #z2 = P(-0.711823, -0.202167)
        #c4 = P(0.44911, -0.314479)
        #c5 = P(4.78592, 2.54403)
        z3 = P(4.78592, 4.84569)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.149223, 0.568999)
        #z1 = z0 + P(-0.655302, 0.704795)
        #c1 = z1 + P(0.302062, 0.108005)
        #c2 = z1 + P(-0.285223, -0.101984)
        #z2 = z1 + P(-0.0565206, -0.906962)
        #c3 = z2 + P(-0.835881, 0.0808655)
        #c4 = z2 + P(1.16093, -0.112312)
        #z3 = z2 + P(5.49775, 5.04786)
        #c5 = z3 + P(0, -2.30166)

        z0 = P(0, -0)
        c0 = z0 + PP(0.588241, 104)
        z1 = z0 + PP(0.962371, 132)
        c1 = z1 + PP(0.32079, 19)
        c2 = z1 + PP(0.302907, -160)
        z2 = z1 + PP(0.908721, -93)
        #z2 = z3 - PP(7.46365, ta + 312)
        c3 = z2 + PP(0.839783, 174)
        c4 = z2 + PP(1.16635, -5)
        z3 = z2 + PP(7.46365, 42)
        c5 = z3 + PP(2.30166, -90)

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
    def path_CLNELe(cls, ta=None, **kwargs):
        #M 100.792,101.759 C 100.388,100.141 99.8261,99.4352 98.9663,99.7312 98.1594,100.025 96.464,102.055 98.8315,102.304 102.125,102.592 116.24264,94.448986 114.554,88.1469

        #z0 = P(0, -0)
        #c0 = P(-0.142522, 0.570794)
        #c1 = P(-0.340748, 0.819785)
        #z1 = P(-0.644066, 0.715363)
        #c2 = P(-0.928723, 0.611717)
        #c3 = P(-1.52682, -0.104422)
        #z2 = P(-0.691621, -0.192264)
        #c4 = P(0.470253, -0.293864)
        #c5 = P(5.45064, 2.57881)
        z3 = P(4.85493, 4.80205)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.142522, 0.570794)
        #z1 = z0 + P(-0.644066, 0.715363)
        #c1 = z1 + P(0.303318, 0.104422)
        #c2 = z1 + P(-0.284656, -0.103646)
        #z2 = z1 + P(-0.0475544, -0.907627)
        #c3 = z2 + P(-0.835201, 0.0878417)
        #c4 = z2 + P(1.16187, -0.1016)
        #z3 = z2 + P(5.54655, 4.99431)
        #c5 = z3 + P(0.595715, -2.22324)

        z0 = P(0, -0)
        c0 = z0 + PP(0.588319, 104)
        z1 = z0 + PP(0.962583, 131)
        c1 = z1 + PP(0.32079, 18)
        c2 = z1 + PP(0.302939, -159)
        z2 = z1 + PP(0.908872, -92)
        #z2 = z3 - PP(7.46373, ta + 296)
        c3 = z2 + PP(0.839808, 173)
        c4 = z2 + PP(1.16631, -4)
        z3 = z2 + PP(7.46373, 42)
        c5 = z3 + PP(2.30166, -74)

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
    def path_CLNELer(cls, ta=None, **kwargs):
        return cls.path_CLNELe()

    @classmethod
    def path_CLNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELne(cls, ta=None, **kwargs):
        return cls.path_CLNELe()

    @classmethod
    def path_CLNELner(cls, ta=None, **kwargs):
        #M 303.254,101.759 C 302.851,100.141 302.289,99.4352 301.429,99.7312 300.622,100.025 298.926,102.055 301.294,102.304 304.588,102.592 314.78692,94.278703 317.016,88.1469

        #z0 = P(0, -0)
        #c0 = P(-0.142169, 0.570794)
        #c1 = P(-0.340431, 0.819785)
        #z1 = P(-0.643819, 0.715363)
        #c2 = P(-0.928511, 0.611717)
        #c3 = P(-1.52682, -0.104422)
        #z2 = P(-0.691444, -0.192264)
        #c4 = P(0.470606, -0.293864)
        #c5 = P(4.06856, 2.63888)
        z3 = P(4.85493, 4.80205)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.142169, 0.570794)
        #z1 = z0 + P(-0.643819, 0.715363)
        #c1 = z1 + P(0.303389, 0.104422)
        #c2 = z1 + P(-0.284692, -0.103646)
        #z2 = z1 + P(-0.047625, -0.907627)
        #c3 = z2 + P(-0.835378, 0.0878417)
        #c4 = z2 + P(1.16205, -0.1016)
        #z3 = z2 + P(5.54637, 4.99431)
        #c5 = z3 + P(-0.78637, -2.16316)

        z0 = P(0, -0)
        c0 = z0 + PP(0.588233, 103)
        z1 = z0 + PP(0.962417, 131)
        c1 = z1 + PP(0.320856, 18)
        c2 = z1 + PP(0.302972, -159)
        z2 = z1 + PP(0.908875, -93)
        #z2 = z3 - PP(7.4636, ta + 331)
        c3 = z2 + PP(0.839983, 173)
        c4 = z2 + PP(1.16648, -4)
        z3 = z2 + PP(7.4636, 42)
        #c5 = z3 + PP(2.30166, -109)
        c5 = z3 + PP(2.30166, ta+180)

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
    def path_CLNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELsl(cls, ta=None, **kwargs):
        return cls.path_CLNELsw(ta=ta)

    @classmethod
    def path_CLNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELse(cls, ta=None, **kwargs):
        return cls.path_CLNELe()

    @classmethod
    def path_CLNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELsw(cls, ta=None, **kwargs):
        #M 303.254,101.759 C 302.851,100.141 302.289,99.4352 301.429,99.7312 300.622,100.025 298.926,102.055 301.294,102.304 304.588,102.592 314.78692,94.278703 317.016,88.1469

        #z0 = P(0, -0)
        #c0 = P(-0.142169, 0.570794)
        #c1 = P(-0.340431, 0.819785)
        #z1 = P(-0.643819, 0.715363)
        #c2 = P(-0.928511, 0.611717)
        #c3 = P(-1.52682, -0.104422)
        #z2 = P(-0.691444, -0.192264)
        #c4 = P(0.470606, -0.293864)
        #c5 = P(4.06856, 2.63888)
        z3 = P(4.85493, 4.80205)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.142169, 0.570794)
        #z1 = z0 + P(-0.643819, 0.715363)
        #c1 = z1 + P(0.303389, 0.104422)
        #c2 = z1 + P(-0.284692, -0.103646)
        #z2 = z1 + P(-0.047625, -0.907627)
        #c3 = z2 + P(-0.835378, 0.0878417)
        #c4 = z2 + P(1.16205, -0.1016)
        #z3 = z2 + P(5.54637, 4.99431)
        #c5 = z3 + P(-0.78637, -2.16316)

        z0 = P(0, -0)
        c0 = z0 + PP(0.588233, 103)
        z1 = z0 + PP(0.962417, 131)
        c1 = z1 + PP(0.320856, 18)
        c2 = z1 + PP(0.302972, -159)
        z2 = z1 + PP(0.908875, -93)
        #z2 = z3 - PP(7.4636, ta + 331)
        c3 = z2 + PP(0.839983, 173)
        c4 = z2 + PP(1.16648, -4)
        z3 = z2 + PP(7.4636, 42)
        #c5 = z3 + PP(2.30166, -109)
        c5 = z3 + PP(2.30166, ta)

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
    def path_CLNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELswl(cls, ta=None, **kwargs):
        pass

class CharSashi(CharSa):
    def __init__(self, name='sashi', kana='さし',
                 model='NEL8CR1|SWR8CL1', head_type='NEL|SWR', tail_type='NELCR1|SWRCL1'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_ligature = {'NER'}
            self.tail_ligature = {'SL', 'SW', 'SWL'}
            self.head_type = 'SWR'
            self.tail_type = 'SWRCL1'
            return super(WasedaChar, self).get_paths(me='SWRCL')
        else:
            self.head_ligature = {'SEL'}
            self.tail_ligature = {'E', 'ER', 'NE', 'NER', 'NEL'}
            self.head_type = 'NEL'
            self.tail_type = 'NELCR1'
            return super(WasedaChar, self).get_paths(me='NELCR')

    @classmethod
    def path_NELCR(cls, ta=None, **kwargs):
        #M 46.555297,58.462808 C 52.271097,55.162708 61.572306,50.495931 62.565097,44.047508 62.779489,42.65498 64.736441,43.204871 65.023104,44.032301 65.286015,44.791172 65.30454,45.917817 64.674901,46.416377 63.946801,46.992899 62.875507,46.675878 61.899132,46.176219

        #z0 = P(0, -0)
        #c0 = P(2.01641, 1.1642)
        #c1 = P(5.29767, 2.81054)
        #z1 = P(5.6479, 5.0854)
        #c2 = P(5.72353, 5.57665)
        #c3 = P(6.4139, 5.38266)
        #z2 = P(6.51503, 5.09076)
        #c4 = P(6.60778, 4.82305)
        #c5 = P(6.61432, 4.42559)
        #z3 = P(6.39219, 4.24971)
        #c6 = P(6.13534, 4.04633)
        #c7 = P(5.75741, 4.15817)
        z4 = P(5.41296, 4.33444)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01641, 1.1642)
        #z1 = z0 + P(5.6479, 5.0854)
        #c1 = z1 + P(-0.350235, -2.27486)
        #c2 = z1 + P(0.0756327, 0.491253)
        #z2 = z1 + P(0.86713, 0.00536469)
        #c3 = z2 + P(-0.101128, 0.291899)
        #c4 = z2 + P(0.0927492, -0.267713)
        #z3 = z2 + P(-0.122838, -0.841049)
        #c5 = z3 + P(0.222123, 0.175881)
        #c6 = z3 + P(-0.256858, -0.203384)
        #z4 = z3 + P(-0.97923, 0.0847224)
        #c7 = z4 + P(0.344443, -0.176269)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32836, 30)
        z1 = z0 + PP(7.6, 42)
        c1 = z1 + PP(2.30166, -98)
        c2 = z1 + PP(0.497041, 81)
        z2 = z1 + PP(0.867147, 0)
        c3 = z2 + PP(0.308921, 109)
        c4 = z2 + PP(0.283324, -70)
        z3 = z2 + PP(0.849972, -98)
        #z3 = z4 - PP(0.982888, ta + 382)
        c5 = z3 + PP(0.283324, 38)
        c6 = z3 + PP(0.327629, -141)
        z4 = z3 + PP(0.982888, 175)
        c7 = z4 + PP(0.386926, -27)

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
    def path_NELCRe(cls, ta=None, **kwargs):
        #M 102.386,103.098 C 108.102,99.7978 117.488,95.1435 118.396,88.6826 118.616,87.291 120.5097,87.877449 120.854,88.6826 121.6652,90.579603 119.05221,90.8257 117.743,90.8257

        #z0 = P(0, -0)
        #c0 = P(2.01648, 1.16424)
        #c1 = P(5.32765, 2.80617)
        #z1 = P(5.64797, 5.08543)
        #c2 = P(5.72558, 5.57636)
        #c3 = P(6.39364, 5.36947)
        #z2 = P(6.5151, 5.08543)
        #c4 = P(6.80127, 4.41621)
        #c5 = P(5.87947, 4.32939)
        z3 = P(5.41761, 4.32939)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01648, 1.16424)
        #z1 = z0 + P(5.64797, 5.08543)
        #c1 = z1 + P(-0.320322, -2.27926)
        #c2 = z1 + P(0.0776111, 0.490926)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.121461, 0.284039)
        #c4 = z2 + P(0.286173, -0.669221)
        #z3 = z2 + P(-1.09749, -0.756038)
        #c5 = z3 + P(0.46186, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32844, 30)
        z1 = z0 + PP(7.60008, 41)
        c1 = z1 + PP(2.30166, -97)
        c2 = z1 + PP(0.497023, 81)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.3327, ta + 35)
        c3 = z2 + PP(0.308919, 113)
        c4 = z2 + PP(0.72784, -66)
        z3 = z2 + PP(1.3327, -145)
        c5 = z3 + PP(0.46186, 0)

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
    def path_NELCRer(cls, ta=None, **kwargs):
        #M 168.77,103.098 C 174.486,99.7978 183.872,95.1435 184.78,88.6826 185,87.291 186.94492,87.917478 187.238,88.6826 187.83276,90.235311 184.97662,91.013226 183.52632,92.015065

        #z0 = P(0, -0)
        #c0 = P(2.01648, 1.16424)
        #c1 = P(5.32765, 2.80617)
        #z1 = P(5.64797, 5.08543)
        #c2 = P(5.72558, 5.57636)
        #c3 = P(6.41171, 5.35535)
        #z2 = P(6.5151, 5.08543)
        #c4 = P(6.72492, 4.53767)
        #c5 = P(5.71734, 4.26324)
        z3 = P(5.2057, 3.90981)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01648, 1.16424)
        #z1 = z0 + P(5.64797, 5.08543)
        #c1 = z1 + P(-0.320322, -2.27926)
        #c2 = z1 + P(0.0776111, 0.490926)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.103392, 0.269918)
        #c4 = z2 + P(0.209818, -0.547762)
        #z3 = z2 + P(-1.3094, -1.17562)
        #c5 = z3 + P(0.511634, 0.353427)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32844, 30)
        z1 = z0 + PP(7.60008, 41)
        c1 = z1 + PP(2.30166, -97)
        c2 = z1 + PP(0.497023, 81)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.75972, ta + 8)
        c3 = z2 + PP(0.289043, 110)
        c4 = z2 + PP(0.586572, -69)
        z3 = z2 + PP(1.75972, -138)
        c5 = z3 + PP(0.621835, 34)

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
    def path_NELCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRne(cls, ta=None, **kwargs):
        #M 447.025,103.098 C 452.741,99.7978 462.127,95.1435 463.035,88.6826 463.256,87.291 464.46564,87.357599 464.88024,87.884157 465.97701,89.277087 463.12321,91.157573 461.68192,92.133757

        #z0 = P(0, -0)
        #c0 = P(2.01648, 1.16424)
        #c1 = P(5.32765, 2.80617)
        #z1 = P(5.64797, 5.08543)
        #c2 = P(5.72594, 5.57636)
        #c3 = P(6.15267, 5.55286)
        #z2 = P(6.29893, 5.36711)
        #c4 = P(6.68585, 4.87571)
        #c5 = P(5.67909, 4.21232)
        z3 = P(5.17064, 3.86794)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01648, 1.16424)
        #z1 = z0 + P(5.64797, 5.08543)
        #c1 = z1 + P(-0.320322, -2.27926)
        #c2 = z1 + P(0.0779639, 0.490926)
        #z2 = z1 + P(0.65096, 0.281673)
        #c3 = z2 + P(-0.146262, 0.185758)
        #c4 = z2 + P(0.386916, -0.491395)
        #z3 = z2 + P(-1.1283, -1.49916)
        #c5 = z3 + P(0.508455, 0.344376)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32844, 30)
        z1 = z0 + PP(7.60008, 41)
        c1 = z1 + PP(2.30166, -97)
        c2 = z1 + PP(0.497078, 80)
        z2 = z1 + PP(0.709287, 23)
        #z2 = z3 - PP(1.87631, ta + 20)
        c3 = z2 + PP(0.236429, 128)
        c4 = z2 + PP(0.625438, -51)
        z3 = z2 + PP(1.87631, -126)
        c5 = z3 + PP(0.614102, 34)

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
    def path_NELCRner(cls, ta=None, **kwargs):
        #M 500.02,103.098 C 505.735,99.7978 515.1005,95.140585 516.029,88.6826 516.22952,87.287902 517.62785,87.42416 518.17288,87.947327 519.03524,88.775088 518.34304,91.322248 517.1493,91.384163 516.17573,91.434659 515.40911,90.108922 516.029,88.6826

        #z0 = P(0, -0)
        #c0 = P(2.01613, 1.16424)
        #c1 = P(5.32007, 2.8072)
        #z1 = P(5.64762, 5.08543)
        #c2 = P(5.71836, 5.57745)
        #c3 = P(6.21166, 5.52938)
        #z2 = P(6.40393, 5.34482)
        #c4 = P(6.70815, 5.05281)
        #c5 = P(6.46396, 4.15422)
        #z3 = P(6.04284, 4.13238)
        #c6 = P(5.69938, 4.11457)
        #c7 = P(5.42894, 4.58226)
        z4 = P(5.64762, 5.08543)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01613, 1.16424)
        #z1 = z0 + P(5.64762, 5.08543)
        #c1 = z1 + P(-0.327554, -2.27823)
        #c2 = z1 + P(0.070739, 0.492018)
        #z2 = z1 + P(0.756313, 0.259388)
        #c3 = z2 + P(-0.192274, 0.184562)
        #c4 = z2 + P(0.304221, -0.292016)
        #z3 = z2 + P(-0.361096, -1.21244)
        #c5 = z3 + P(0.421125, 0.0218422)
        #c6 = z3 + P(-0.343454, -0.0178139)
        #z4 = z3 + P(-0.395217, 0.953051)
        #c7 = z4 + P(-0.218683, -0.503175)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32813, 30)
        z1 = z0 + PP(7.59982, 42)
        c1 = z1 + PP(2.30166, -98)
        c2 = z1 + PP(0.497078, 81)
        z2 = z1 + PP(0.799557, 18)
        c3 = z2 + PP(0.266519, 136)
        c4 = z2 + PP(0.421692, -43)
        #z3 = z2 + PP(1.26507, -106)
        z3 = z4 - PP(1.03175, ta + 405)
        c5 = z3 + PP(0.421691, 2)
        #c6 = z3 + PP(0.343916, -177)
        #z4 = z3 + PP(1.03175, 112)
        #c7 = z4 + PP(0.548641, -113)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_NELCRnel(cls, ta=None, **kwargs):
        #M 394.762,103.098 C 400.478,99.7978 409.864,95.1435 410.772,88.6826 410.992,87.291 412.98661,87.900252 413.23,88.6826 413.60407,89.884998 412.22325,90.224744 410.119,90.8257

        #z0 = P(0, -0)
        #c0 = P(2.01648, 1.16424)
        #c1 = P(5.32765, 2.80617)
        #z1 = P(5.64797, 5.08543)
        #c2 = P(5.72558, 5.57636)
        #c3 = P(6.42924, 5.36143)
        #z2 = P(6.5151, 5.08543)
        #c4 = P(6.64706, 4.66125)
        #c5 = P(6.15994, 4.5414)
        z3 = P(5.41761, 4.32939)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01648, 1.16424)
        #z1 = z0 + P(5.64797, 5.08543)
        #c1 = z1 + P(-0.320322, -2.27926)
        #c2 = z1 + P(0.0776111, 0.490926)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.0858626, 0.275995)
        #c4 = z2 + P(0.131964, -0.424179)
        #z3 = z2 + P(-1.09749, -0.756038)
        #c5 = z3 + P(0.742333, 0.212004)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32844, 30)
        z1 = z0 + PP(7.60008, 41)
        c1 = z1 + PP(2.30166, -97)
        c2 = z1 + PP(0.497023, 81)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.3327, ta + 20)
        c3 = z2 + PP(0.289043, 107)
        c4 = z2 + PP(0.444232, -72)
        z3 = z2 + PP(1.3327, -145)
        c5 = z3 + PP(0.772013, 15)

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
    def path_NELCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCR(cls, ta=None, **kwargs):
        #M 60.0973,384.232 C 67.38545,384.232 72.4195,374.509 73.2146,368.034 73.4594,366.646 75.402,367.201 75.6726,368.034 75.9603,368.783 76.0032,369.92 75.379,370.425 74.7563,370.948 73.9325,370.736 72.9461,370.255

        #z0 = P(0, -0)
        #c0 = P(2.5711, -0)
        #c1 = P(4.347, 3.43006)
        #z1 = P(4.62749, 5.71429)
        #c2 = P(4.71385, 6.20395)
        #c3 = P(5.39916, 6.00816)
        #z2 = P(5.49462, 5.71429)
        #c4 = P(5.59611, 5.45006)
        #c5 = P(5.61125, 5.04896)
        #z3 = P(5.39104, 4.8708)
        #c6 = P(5.17137, 4.6863)
        #c7 = P(4.88075, 4.76109)
        z4 = P(4.53277, 4.93078)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.5711, 0)
        #z1 = z0 + P(4.62749, 5.71429)
        #c1 = z1 + P(-0.280494, -2.28424)
        #c2 = z1 + P(0.08636, 0.489656)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.0954617, 0.293864)
        #c4 = z2 + P(0.101494, -0.264231)
        #z3 = z2 + P(-0.103576, -0.843492)
        #c5 = z3 + P(0.220204, 0.178153)
        #c6 = z3 + P(-0.219675, -0.184503)
        #z4 = z3 + P(-0.858273, 0.0599722)
        #c7 = z4 + P(0.34798, -0.169686)

        z0 = P(0, -0)
        c0 = z0 + PP(2.5711, 0)
        z1 = z0 + PP(7.35302, 50)
        c1 = z1 + PP(2.30139, -97)
        c2 = z1 + PP(0.497213, 79)
        z2 = z1 + PP(0.867128, 0)
        c3 = z2 + PP(0.30898, 107)
        c4 = z2 + PP(0.283053, -68)
        z3 = z2 + PP(0.849827, -97)
        #z3 = z4 - PP(0.860366, ta + 381)
        c5 = z3 + PP(0.283246, 38)
        c6 = z3 + PP(0.286877, -139)
        z4 = z3 + PP(0.860366, 176)
        c7 = z4 + PP(0.387148, -25)

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
    def path_selNELCRe(cls, ta=None, **kwargs):
        #M 113.985,334.422 C 123.20086,334.422 126.178,324.67126 127.086,318.21026 127.307,316.81826 129.27164,317.43752 129.544,318.21026 129.93782,319.32763 128.36442,320.43882 126.77524,320.43882

        #z0 = P(0, -0)
        #c0 = P(3.25115, -0)
        #c1 = P(4.30142, 3.43984)
        #z1 = P(4.62174, 5.71914)
        #c2 = P(4.69971, 6.21021)
        #c3 = P(5.39279, 5.99175)
        #z2 = P(5.48887, 5.71914)
        #c4 = P(5.6278, 5.32496)
        #c5 = P(5.07274, 4.93296)
        z3 = P(4.51211, 4.93296)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.25115, 0)
        #z1 = z0 + P(4.62174, 5.71914)
        #c1 = z1 + P(-0.320322, -2.2793)
        #c2 = z1 + P(0.0779639, 0.491067)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.0960826, 0.272605)
        #c4 = z2 + P(0.138931, -0.394183)
        #z3 = z2 + P(-0.976757, -0.786186)
        #c5 = z3 + P(0.560627, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(3.25115, 0)
        z1 = z0 + PP(7.35317, 51)
        c1 = z1 + PP(2.3017, -97)
        c2 = z1 + PP(0.497217, 80)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.25385, ta + 39)
        c3 = z2 + PP(0.289043, 109)
        c4 = z2 + PP(0.41795, -70)
        z3 = z2 + PP(1.25385, -141)
        c5 = z3 + PP(0.560627, 0)

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
    def path_selNELCRer(cls, ta=None, **kwargs):
        #M 310.714,331.594 C 318.002,331.594 323.037,321.872 323.832,315.396 324.076,314.008 326.01542,314.62405 326.29,315.396 326.68289,316.50054 324.90167,316.94611 323.563,317.617

        #z0 = P(0, -0)
        #c0 = P(2.57104, -0)
        #c1 = P(4.34728, 3.42971)
        #z1 = P(4.62774, 5.71429)
        #c2 = P(4.71382, 6.20395)
        #c3 = P(5.398, 5.98662)
        #z2 = P(5.49487, 5.71429)
        #c4 = P(5.63347, 5.32464)
        #c5 = P(5.00509, 5.16745)
        z3 = P(4.53284, 4.93077)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.57104, 0)
        #z1 = z0 + P(4.62774, 5.71429)
        #c1 = z1 + P(-0.280458, -2.28459)
        #c2 = z1 + P(0.0860778, 0.489656)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.0968657, 0.272327)
        #c4 = z2 + P(0.138603, -0.389657)
        #z3 = z2 + P(-0.962025, -0.783519)
        #c5 = z3 + P(0.472253, 0.236675)

        z0 = P(0, -0)
        c0 = z0 + PP(2.57104, 0)
        z1 = z0 + PP(7.35317, 50)
        c1 = z1 + PP(2.30174, -96)
        c2 = z1 + PP(0.497164, 80)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.24072, ta + 14)
        c3 = z2 + PP(0.289041, 109)
        c4 = z2 + PP(0.413574, -70)
        z3 = z2 + PP(1.24072, -140)
        c5 = z3 + PP(0.52824, 26)

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
    def path_selNELCRel(cls, ta=None, **kwargs):
        #M 113.985,334.422 C 123.20086,334.422 126.178,324.67126 127.086,318.21026 127.307,316.81826 129.259,317.38226 129.544,318.21026 129.819,318.96426 129.8318,320.08916 129.209,320.59626 128.57859,321.10955 127.75324,320.93682 126.77524,320.43882

        #z0 = P(0, -0)
        #c0 = P(3.25115, -0)
        #c1 = P(4.30142, 3.43984)
        #z1 = P(4.62174, 5.71914)
        #c2 = P(4.69971, 6.21021)
        #c3 = P(5.38833, 6.01124)
        #z2 = P(5.48887, 5.71914)
        #c4 = P(5.58588, 5.45315)
        #c5 = P(5.5904, 5.05631)
        #z3 = P(5.37069, 4.87741)
        #c6 = P(5.14829, 4.69634)
        #c7 = P(4.85713, 4.75727)
        z4 = P(4.51211, 4.93296)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.25115, 0)
        #z1 = z0 + P(4.62174, 5.71914)
        #c1 = z1 + P(-0.320322, -2.2793)
        #c2 = z1 + P(0.0779639, 0.491067)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.100542, 0.2921)
        #c4 = z2 + P(0.0970139, -0.265994)
        #z3 = z2 + P(-0.118181, -0.841728)
        #c5 = z3 + P(0.21971, 0.178894)
        #c6 = z3 + P(-0.222395, -0.181077)
        #z4 = z3 + P(-0.858576, 0.0555413)
        #c7 = z4 + P(0.345017, -0.175683)

        z0 = P(0, -0)
        c0 = z0 + PP(3.25115, 0)
        z1 = z0 + PP(7.35317, 51)
        c1 = z1 + PP(2.3017, -97)
        c2 = z1 + PP(0.497217, 80)
        z2 = z1 + PP(0.867128, 0)
        c3 = z2 + PP(0.308919, 108)
        c4 = z2 + PP(0.283134, -69)
        z3 = z2 + PP(0.849984, -97)
        #z3 = z4 - PP(0.860371, ta + 382)
        c5 = z3 + PP(0.283329, 39)
        c6 = z3 + PP(0.28679, -140)
        z4 = z3 + PP(0.860371, 176)
        c7 = z4 + PP(0.387171, -26)

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
    def path_selNELCRne(cls, ta=None, **kwargs):
        #M 60.0973,384.232 C 67.38545,384.232 72.4195,374.509 73.2146,368.034 73.4594,366.646 75.355642,367.27846 75.6726,368.034 76.246816,369.40278 74.079812,370.42393 72.552379,371.21105

        #z0 = P(0, -0)
        #c0 = P(2.5711, -0)
        #c1 = P(4.347, 3.43006)
        #z1 = P(4.62749, 5.71429)
        #c2 = P(4.71385, 6.20395)
        #c3 = P(5.3828, 5.98083)
        #z2 = P(5.49462, 5.71429)
        #c4 = P(5.69719, 5.23142)
        #c5 = P(4.93272, 4.87118)
        z3 = P(4.39388, 4.5935)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.5711, 0)
        #z1 = z0 + P(4.62749, 5.71429)
        #c1 = z1 + P(-0.280494, -2.28424)
        #c2 = z1 + P(0.08636, 0.489656)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.111816, 0.266538)
        #c4 = z2 + P(0.202571, -0.482875)
        #z3 = z2 + P(-1.10074, -1.12079)
        #c5 = z3 + P(0.538844, 0.277678)

        z0 = P(0, -0)
        c0 = z0 + PP(2.5711, 0)
        z1 = z0 + PP(7.35302, 50)
        c1 = z1 + PP(2.30139, -97)
        c2 = z1 + PP(0.497213, 79)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.57093, ta + 19)
        c3 = z2 + PP(0.289042, 112)
        c4 = z2 + PP(0.523644, -67)
        z3 = z2 + PP(1.57093, -134)
        c5 = z3 + PP(0.606184, 27)

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
    def path_selNELCRner(cls, ta=None, **kwargs):
        #M 123.339,384.232 C 130.627,384.232 135.662,374.509 136.457,368.034 136.701,366.646 138.16799,367.19607 138.63892,367.75792 139.29889,368.5453 138.74853,370.62823 137.72373,370.70108 136.742,370.77087 135.90524,369.7499 136.457,368.034

        #z0 = P(0, -0)
        #c0 = P(2.57104, -0)
        #c1 = P(4.34728, 3.43006)
        #z1 = P(4.62774, 5.71429)
        #c2 = P(4.71382, 6.20395)
        #c3 = P(5.23134, 6.0099)
        #z2 = P(5.39747, 5.81169)
        #c4 = P(5.63029, 5.53392)
        #c5 = P(5.43614, 4.79911)
        #z3 = P(5.07461, 4.77341)
        #c6 = P(4.72828, 4.74879)
        #c7 = P(4.43309, 5.10896)
        z4 = P(4.62774, 5.71429)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.57104, 0)
        #z1 = z0 + P(4.62774, 5.71429)
        #c1 = z1 + P(-0.280458, -2.28424)
        #c2 = z1 + P(0.0860778, 0.489656)
        #z2 = z1 + P(0.769733, 0.0973949)
        #c3 = z2 + P(-0.166134, 0.198208)
        #c4 = z2 + P(0.232823, -0.27777)
        #z3 = z2 + P(-0.322859, -1.03828)
        #c5 = z3 + P(0.361527, 0.0256999)
        #c6 = z3 + P(-0.346333, -0.0246204)
        #z4 = z3 + P(-0.446874, 0.940887)
        #c7 = z4 + P(-0.194649, -0.605331)

        z0 = P(0, -0)
        c0 = z0 + PP(2.57104, 0)
        z1 = z0 + PP(7.35317, 50)
        c1 = z1 + PP(2.30139, -96)
        c2 = z1 + PP(0.497164, 80)
        z2 = z1 + PP(0.77587, 7)
        c3 = z2 + PP(0.258625, 129)
        c4 = z2 + PP(0.36244, -50)
        #z3 = z2 + PP(1.08732, -107)
        z3 = z4 - PP(1.04162, ta + 402)
        c5 = z3 + PP(0.362439, 4)
        #c6 = z3 + PP(0.347207, -175)
        #z4 = z3 + PP(1.04162, 115)
        #c7 = z4 + PP(0.635857, -107)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_selNELCRnel(cls, ta=None, **kwargs):
        #M 587.945,331.594 C 597.161,331.594 600.267,321.872 601.062,315.396 601.307,314.008 603.24535,314.62407 603.52,315.396 603.9129,316.50026 602.41542,317.10299 600.794,317.617

        #z0 = P(0, -0)
        #c0 = P(3.2512, -0)
        #c1 = P(4.34693, 3.42971)
        #z1 = P(4.62739, 5.71429)
        #c2 = P(4.71382, 6.20395)
        #c3 = P(5.39762, 5.98661)
        #z2 = P(5.49451, 5.71429)
        #c4 = P(5.63312, 5.32474)
        #c5 = P(5.10484, 5.11211)
        z3 = P(4.53284, 4.93077)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.2512, 0)
        #z1 = z0 + P(4.62739, 5.71429)
        #c1 = z1 + P(-0.280458, -2.28459)
        #c2 = z1 + P(0.0864306, 0.489656)
        #z2 = z1 + P(0.867128, 0)
        #c3 = z2 + P(-0.0968904, 0.27232)
        #c4 = z2 + P(0.138606, -0.389558)
        #z3 = z2 + P(-0.961672, -0.783519)
        #c5 = z3 + P(0.572001, 0.181331)

        z0 = P(0, -0)
        c0 = z0 + PP(3.2512, 0)
        z1 = z0 + PP(7.35295, 50)
        c1 = z1 + PP(2.30174, -96)
        c2 = z1 + PP(0.497225, 79)
        z2 = z1 + PP(0.867128, 0)
        #z2 = z3 - PP(1.24045, ta + 23)
        c3 = z2 + PP(0.289043, 109)
        c4 = z2 + PP(0.413482, -70)
        z3 = z2 + PP(1.24045, -140)
        c5 = z3 + PP(0.600055, 17)

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
    def path_selNELCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerNELCRswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCL(cls, ta=None, **kwargs):
        #M 302.086,128.656 C 302.086,137.777 299.85554,146.96435 291.94922,147.313 289.41026,147.42496 290.23126,148.89211 290.72547,149.25315 291.58029,149.87761 293.23878,149.90469 293.9448,149.09482 294.34153,148.63973 293.96453,147.64713 293.78624,147.29056

        #z0 = P(0, -0)
        #c0 = P(0, -3.21769)
        #c1 = P(-0.786857, -6.45878)
        #z1 = P(-3.57603, -6.58177)
        #c2 = P(-4.47172, -6.62127)
        #c3 = P(-4.18209, -7.13885)
        #z2 = P(-4.00774, -7.26622)
        #c4 = P(-3.70618, -7.48651)
        #c5 = P(-3.1211, -7.49607)
        #z3 = P(-2.87203, -7.21036)
        #c6 = P(-2.73208, -7.04982)
        #c7 = P(-2.86507, -6.69965)
        z4 = P(-2.92797, -6.57386)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.21769)
        #z1 = z0 + P(-3.57603, -6.58177)
        #c1 = z1 + P(2.78917, 0.122996)
        #c2 = z1 + P(-0.895689, -0.039497)
        #z2 = z1 + P(-0.431712, -0.684442)
        #c3 = z2 + P(-0.174346, 0.127367)
        #c4 = z2 + P(0.301562, -0.220296)
        #z3 = z2 + P(1.13571, 0.0558553)
        #c5 = z3 + P(-0.249068, -0.285704)
        #c6 = z3 + P(0.139958, 0.160546)
        #z4 = z3 + P(-0.0559364, 0.636503)
        #c7 = z4 + P(0.0628968, -0.12579)

        z0 = P(0, -0)
        c0 = z0 + PP(3.21769, -90)
        z1 = z0 + PP(7.49051, -118)
        c1 = z1 + PP(2.79188, 2)
        c2 = z1 + PP(0.896559, -177)
        z2 = z1 + PP(0.809219, -122)
        c3 = z2 + PP(0.215914, 143)
        c4 = z2 + PP(0.373456, -36)
        z3 = z2 + PP(1.13708, 2)
        #z3 = z4 - PP(0.638956, ta + 338)
        c5 = z3 + PP(0.379027, -131)
        c6 = z3 + PP(0.212986, 48)
        z4 = z3 + PP(0.638956, 95)
        c7 = z4 + PP(0.140638, -63)

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
    def path_SWRCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLsl(cls, ta=None, **kwargs):
        #M 151.953,228.945 C 151.953,238.066 149.894,247.416 141.984,247.693 139.446,247.826 140.21241,249.114 140.769,249.638 141.6923,250.50724 143.44146,248.20643 143.86816,247.43172

        #z0 = P(0, -0)
        #c0 = P(0, -3.21769)
        #c1 = P(-0.726369, -6.51616)
        #z1 = P(-3.51684, -6.61388)
        #c2 = P(-4.41219, -6.6608)
        #c3 = P(-4.14182, -7.11518)
        #z2 = P(-3.94547, -7.30003)
        #c4 = P(-3.61975, -7.60668)
        #c5 = P(-3.00268, -6.795)
        z3 = P(-2.85215, -6.5217)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.21769)
        #z1 = z0 + P(-3.51684, -6.61388)
        #c1 = z1 + P(2.79047, 0.0977194)
        #c2 = z1 + P(-0.89535, -0.0469194)
        #z2 = z1 + P(-0.428625, -0.686153)
        #c3 = z2 + P(-0.196353, 0.184856)
        #c4 = z2 + P(0.32572, -0.306649)
        #z3 = z2 + P(1.09331, 0.778327)
        #c5 = z3 + P(-0.15053, -0.2733)

        z0 = P(0, -0)
        c0 = z0 + PP(3.21769, -90)
        z1 = z0 + PP(7.49076, -118)
        c1 = z1 + PP(2.79218, 2)
        c2 = z1 + PP(0.896579, -177)
        z2 = z1 + PP(0.809027, -121)
        #z2 = z3 - PP(1.34206, ta + 333)
        c3 = z2 + PP(0.269677, 136)
        c4 = z2 + PP(0.447355, -43)
        z3 = z2 + PP(1.34206, 35)
        c5 = z3 + PP(0.312014, -118)

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
    def path_SWRCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLsw(cls, ta=None, **kwargs):
        #M 112.925,228.945 C 112.925,238.066 110.866,247.416 102.956,247.693 100.418,247.826 101.18513,249.11324 101.741,249.638 102.66668,250.51188 104.1061,249.50817 104.85824,247.43172

        #z0 = P(0, -0)
        #c0 = P(0, -3.21769)
        #c1 = P(-0.726369, -6.51616)
        #z1 = P(-3.51684, -6.61388)
        #c2 = P(-4.41219, -6.6608)
        #c3 = P(-4.14157, -7.11491)
        #z2 = P(-3.94547, -7.30003)
        #c4 = P(-3.61891, -7.60832)
        #c5 = P(-3.11111, -7.25423)
        z3 = P(-2.84577, -6.5217)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.21769)
        #z1 = z0 + P(-3.51684, -6.61388)
        #c1 = z1 + P(2.79047, 0.0977194)
        #c2 = z1 + P(-0.89535, -0.0469194)
        #z2 = z1 + P(-0.428625, -0.686153)
        #c3 = z2 + P(-0.196099, 0.185124)
        #c4 = z2 + P(0.326559, -0.308285)
        #z3 = z2 + P(1.09969, 0.778327)
        #c5 = z3 + P(-0.265338, -0.732525)

        z0 = P(0, -0)
        c0 = z0 + PP(3.21769, -90)
        z1 = z0 + PP(7.49076, -118)
        c1 = z1 + PP(2.79218, 2)
        c2 = z1 + PP(0.896579, -177)
        z2 = z1 + PP(0.809027, -121)
        #z2 = z3 - PP(1.34726, ta + 324)
        c3 = z2 + PP(0.269677, 136)
        c4 = z2 + PP(0.449089, -43)
        z3 = z2 + PP(1.34726, 35)
        c5 = z3 + PP(0.779101, -109)

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
    def path_SWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLswl(cls, ta=None, **kwargs):
        #M 363.76954,229.05883 C 363.76954,238.17983 361.71054,247.53083 353.80054,247.80683 351.26254,247.93983 351.78165,249.94629 352.44879,250.31961 353.06251,250.66303 354.58292,250.66471 355.09066,249.02471 355.32691,248.26161 353.80493,247.67802 352.10631,248.46423

        #z0 = P(0, -0)
        #c0 = P(0, -3.21769)
        #c1 = P(-0.726369, -6.51651)
        #z1 = P(-3.51684, -6.61388)
        #c2 = P(-4.41219, -6.6608)
        #c3 = P(-4.22906, -7.36863)
        #z2 = P(-3.99371, -7.50033)
        #c4 = P(-3.7772, -7.62148)
        #c5 = P(-3.24084, -7.62207)
        #z3 = P(-3.06172, -7.04352)
        #c6 = P(-2.97837, -6.77431)
        #c7 = P(-3.51529, -6.56844)
        z4 = P(-4.11453, -6.84579)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.21769)
        #z1 = z0 + P(-3.51684, -6.61388)
        #c1 = z1 + P(2.79047, 0.0973667)
        #c2 = z1 + P(-0.89535, -0.0469194)
        #z2 = z1 + P(-0.476867, -0.886453)
        #c3 = z2 + P(-0.235352, 0.131699)
        #c4 = z2 + P(0.216507, -0.121151)
        #z3 = z2 + P(0.931993, 0.456812)
        #c5 = z3 + P(-0.179119, -0.578556)
        #c6 = z3 + P(0.0833437, 0.269205)
        #z4 = z3 + P(-1.05281, 0.197725)
        #c7 = z4 + P(0.599235, 0.277357)

        z0 = P(0, -0)
        c0 = z0 + PP(3.21769, -90)
        z1 = z0 + PP(7.49076, -118)
        c1 = z1 + PP(2.79217, 1)
        c2 = z1 + PP(0.896579, -177)
        z2 = z1 + PP(1.00658, -118)
        c3 = z2 + PP(0.269695, 150)
        c4 = z2 + PP(0.248098, -29)
        #z3 = z2 + PP(1.03792, 26)
        z3 = z4 - PP(1.07122, ta + 325)
        c5 = z3 + PP(0.605649, -107)
        #c6 = z3 + PP(0.281811, 72)
        #z4 = z3 + PP(1.07122, 169)
        #c7 = z4 + PP(0.660311, 24)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_selSWRCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selSWRCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCL(cls, ta=None, **kwargs):
        #M 480.381,352.295 C 484.54063,355.9301 478.322,370.766 470.413,371.042 467.875,371.175 468.708,372.619 469.197,372.987 470.054,373.61 471.714,373.686 472.419,372.875 472.823,372.426 472.442,371.426 472.261,371.071

        #z0 = P(0, -0)
        #c0 = P(1.46743, -1.28238)
        #c1 = P(-0.726369, -6.51616)
        #z1 = P(-3.51649, -6.61352)
        #c2 = P(-4.41184, -6.66044)
        #c3 = P(-4.11797, -7.16986)
        #z2 = P(-3.94547, -7.29968)
        #c4 = P(-3.64314, -7.51946)
        #c5 = P(-3.05752, -7.54627)
        #z3 = P(-2.80882, -7.26017)
        #c6 = P(-2.66629, -7.10177)
        #c7 = P(-2.8007, -6.74899)
        z4 = P(-2.86456, -6.62376)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.46743, -1.28238)
        #z1 = z0 + P(-3.51649, -6.61352)
        #c1 = z1 + P(2.79012, 0.0973667)
        #c2 = z1 + P(-0.89535, -0.0469194)
        #z2 = z1 + P(-0.428978, -0.686153)
        #c3 = z2 + P(-0.172508, 0.129822)
        #c4 = z2 + P(0.302331, -0.219781)
        #z3 = z2 + P(1.13665, 0.0395111)
        #c5 = z3 + P(-0.248708, -0.286103)
        #c6 = z3 + P(0.142522, 0.158397)
        #z4 = z3 + P(-0.0557389, 0.636411)
        #c7 = z4 + P(0.0638528, -0.125236)

        z0 = P(0, -0)
        c0 = z0 + PP(1.94881, -41)
        z1 = z0 + PP(7.49029, -118)
        c1 = z1 + PP(2.79182, 1)
        c2 = z1 + PP(0.896579, -177)
        z2 = z1 + PP(0.809214, -122)
        c3 = z2 + PP(0.2159, 143)
        c4 = z2 + PP(0.373774, -36)
        z3 = z2 + PP(1.13734, 1)
        #z3 = z4 - PP(0.638847, ta + 337)
        c5 = z3 + PP(0.379092, -131)
        c6 = z3 + PP(0.213078, 48)
        z4 = z3 + PP(0.638847, 95)
        c7 = z4 + PP(0.140575, -62)

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
    def path_nerSWRCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLsl(cls, ta=None, **kwargs):
        return cls.path_nerSWRCLsw()

    @classmethod
    def path_nerSWRCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLsw(cls, ta=None, **kwargs):
        #M 188.861,413.514 C 193.03,417.138 186.80454,432.05585 178.893,432.261 176.35237,432.32688 177.11881,433.68478 177.678,434.206 178.60198,435.06725 179.92291,434.07804 180.743,431.97773

        #z0 = P(0, -0)
        #c0 = P(1.47073, -1.27847)
        #c1 = P(-0.725473, -6.54115)
        #z1 = P(-3.51649, -6.61353)
        #c2 = P(-4.41277, -6.63677)
        #c3 = P(-4.14238, -7.1158)
        #z2 = P(-3.94511, -7.29968)
        #c4 = P(-3.61915, -7.60351)
        #c5 = P(-3.15316, -7.25454)
        z3 = P(-2.86385, -6.51359)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.47073, -1.27847)
        #z1 = z0 + P(-3.51649, -6.61353)
        #c1 = z1 + P(2.79102, 0.0723724)
        #c2 = z1 + P(-0.896278, -0.023241)
        #z2 = z1 + P(-0.428625, -0.686153)
        #c3 = z2 + P(-0.19727, 0.183875)
        #c4 = z2 + P(0.32596, -0.30383)
        #z3 = z2 + P(1.08126, 0.786084)
        #c5 = z3 + P(-0.28931, -0.740943)

        z0 = P(0, -0)
        c0 = z0 + PP(1.94872, -40)
        z1 = z0 + PP(7.49029, -118)
        c1 = z1 + PP(2.79195, 1)
        c2 = z1 + PP(0.896579, -178)
        z2 = z1 + PP(0.809027, -121)
        #z2 = z3 - PP(1.33681, ta + 327)
        c3 = z2 + PP(0.269676, 137)
        c4 = z2 + PP(0.445603, -42)
        z3 = z2 + PP(1.33681, 36)
        c5 = z3 + PP(0.795422, -111)

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
    def path_nerSWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLswl(cls, ta=None, **kwargs):
        #M 413.318,413.514 C 417.487,417.138 411.262,432.123 403.35,432.261 400.812,432.394 401.53144,434.2034 402.23384,434.50551 403.09525,434.87601 405.20188,434.40378 405.14621,433.36237 405.08995,432.31001 404.01394,431.66777 402.09684,432.52755

        #z0 = P(0, -0)
        #c0 = P(1.47073, -1.27847)
        #c1 = P(-0.725311, -6.56484)
        #z1 = P(-3.51649, -6.61353)
        #c2 = P(-4.41184, -6.66044)
        #c3 = P(-4.15804, -7.29876)
        #z2 = P(-3.91025, -7.40534)
        #c4 = P(-3.60636, -7.53604)
        #c5 = P(-2.86319, -7.36945)
        #z3 = P(-2.88283, -7.00206)
        #c6 = P(-2.90267, -6.63081)
        #c7 = P(-3.28227, -6.40425)
        z4 = P(-3.95858, -6.70756)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.47073, -1.27847)
        #z1 = z0 + P(-3.51649, -6.61353)
        #c1 = z1 + P(2.79118, 0.0486833)
        #c2 = z1 + P(-0.89535, -0.0469194)
        #z2 = z1 + P(-0.393756, -0.791813)
        #c3 = z2 + P(-0.247791, 0.106578)
        #c4 = z2 + P(0.303886, -0.130704)
        #z3 = z2 + P(1.02742, 0.403274)
        #c5 = z3 + P(0.0196391, -0.367386)
        #c6 = z3 + P(-0.0198473, 0.371249)
        #z4 = z3 + P(-1.07575, 0.294506)
        #c7 = z4 + P(0.67631, 0.303311)

        z0 = P(0, -0)
        c0 = z0 + PP(1.94872, -40)
        z1 = z0 + PP(7.49029, -118)
        c1 = z1 + PP(2.7916, 0)
        c2 = z1 + PP(0.896579, -177)
        z2 = z1 + PP(0.884315, -116)
        c3 = z2 + PP(0.269739, 156)
        c4 = z2 + PP(0.330803, -23)
        #z3 = z2 + PP(1.10373, 21)
        z3 = z4 - PP(1.11533, ta + 320)
        c5 = z3 + PP(0.367911, -86)
        #c6 = z3 + PP(0.371779, 93)
        #z4 = z3 + PP(1.11533, 164)
        #c7 = z4 + PP(0.741211, 24)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

class CharSasu(CharSa):
    def __init__(self, name='sasu', kana='さす',
                 model='NEL8TS3|SWR8TS3', head_type='NEL|SWR', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_ligature = {'NER'}
            self.tail_ligature = {'S', 'SEL'}
            self.head_type = 'SWR'
            self.tail_type = 'S'
            return super(WasedaChar, self).get_paths(me='SWRS')
        else:
            self.head_ligature = {'SEL'}
            self.tail_ligature = {'S', 'SEL'}
            self.head_type = 'NEL'
            self.tail_type = 'S'
            return super(WasedaChar, self).get_paths(me='NELS')

    @classmethod
    def path_SWRS(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(302.086, 128.656),
            pyx.path.curveto(302.086, 137.777, 299.229, 147.313, 291.315, 147.313),
            pyx.path.moveto(291.315, 142.77488),
            pyx.path.lineto(291.315, 151.27883)).transformed(pyx.trafo.trafo().translated(-302.086, -128.656).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_SWRSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRS())

    @classmethod
    def path_SWRSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRS())

    @classmethod
    def path_nerSWRS(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(64.7131, 446.262),
            pyx.path.curveto(68.82992, 450.1612, 61.8561, 464.919, 53.9421, 464.919),
            pyx.path.moveto(53.9421, 460.381),
            pyx.path.lineto(53.9421, 468.885)).transformed(pyx.trafo.trafo().translated(-64.7131, -446.262).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_nerSWRSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_nerSWRS())

    @classmethod
    def path_nerSWRSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_nerSWRS())

    @classmethod
    def path_NELS(cls, ta=None, **kwargs):
        #M 270.132,97.83924 C 275.848,94.53904 286.142,89.94814 286.142,83.42374 286.142,86.360299 286.142,89.975397 286.142,91.92769

        #z0 = P(0, -0)
        #c0 = P(2.01648, 1.16424)
        #c1 = P(5.64797, 2.7838)
        #z1 = P(5.64797, 5.08547)
        #c2 = P(5.64797, 4.04952)
        #c3 = P(5.64797, 2.77419)
        z2 = P(5.64797, 2.08546)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.01648, 1.16424)
        #z1 = z0 + P(5.64797, 5.08547)
        #c1 = z1 + P(0, -2.30166)
        #c2 = z1 + P(0, -1.03595)
        #z2 = z1 + P(0, -3)
        #c3 = z2 + P(0, 0.688726)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32844, 30)
        z1 = z0 + PP(7.6001, 42)
        #z1 = z2 - PP(3, ta + 0)
        c1 = z1 + PP(2.30166, -90)
        c2 = z1 + PP(1.03595, -90)
        z2 = z1 + PP(3, -90)
        c3 = z2 + PP(0.688726, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_NELSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_NELS())

    @classmethod
    def path_NELSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_NELS())

    @classmethod
    def path_selNELS(cls, ta=None, **kwargs):
        #M 112.468,354.152 C 118.27988,354.09533 128.11381,343.25644 128.11381,336.73244 128.11381,339.56711 128.11381,342.40177 128.11381,345.23644

        #z0 = P(0, -0)
        #c0 = P(2.0503, 0.0199919)
        #c1 = P(5.51949, 3.84371)
        #z1 = P(5.51949, 6.14523)
        #c2 = P(5.51949, 5.14523)
        #c3 = P(5.51949, 4.14522)
        z2 = P(5.51949, 3.14521)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.0503, 0.0199919)
        #z1 = z0 + P(5.51949, 6.14523)
        #c1 = z1 + P(0, -2.30152)
        #c2 = z1 + P(0, -1.00001)
        #z2 = z1 + P(0, -3.00002)
        #c3 = z2 + P(0, 1.00001)

        z0 = P(0, -0)
        c0 = z0 + PP(2.0504, 0)
        z1 = z0 + PP(8.26007, 48)
        #z1 = z2 - PP(3.00002, ta + 0)
        c1 = z1 + PP(2.30152, -90)
        c2 = z1 + PP(1.00001, -90)
        z2 = z1 + PP(3.00002, -90)
        c3 = z2 + PP(1.00001, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_selNELSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELS())

    @classmethod
    def path_selNELSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELS())

class CharSaso(CharSa):
    def __init__(self, name='saso', kana='さそ',
                 model='NEL8TSW3|SWR8TSW3', head_type='NEL|SWR', tail_type='SW'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_ligature = {'NER', 'ER'}
            self.tail_ligature = {'SW', 'SL'}
            self.head_type = 'SWR'
            self.tail_type = 'SW'
            return super(WasedaChar, self).get_paths(me='SWRTSW')
        else:
            self.head_ligature = {'SEL'}
            self.tail_ligature = {'SW', 'SL'}
            self.head_type = 'NEL'
            self.tail_type = 'SW'
            return super(WasedaChar, self).get_paths(me='NELTSW')

    @classmethod
    def path_SWRTSW(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(200.7497, 257.35299),
            pyx.path.curveto(200.7497, 266.47399, 197.8928, 276.00999, 189.978, 276.00999),
            pyx.path.moveto(191.917, 270.68299),
            pyx.path.lineto(188.039, 281.33699)).transformed(pyx.trafo.trafo().translated(-200.7497, -257.35299).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_SWRTSWsw(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRTSW())

    @classmethod
    def path_SWRTSWsl(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRTSW())

    @classmethod
    def path_nerSWRTSW(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(68.9454, 379.009),
            pyx.path.curveto(74.366201, 385.04338, 66.0885, 397.666, 58.1737, 397.666),
            pyx.path.moveto(60.1127, 392.339),
            pyx.path.lineto(56.2347, 402.993)).transformed(pyx.trafo.trafo().translated(-68.9454, -379.009).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_nerSWRTSWsw(cls, ta=None, **kwargs):
        return cls.jog(cls.path_nerSWRTSW())

    @classmethod
    def path_nerSWRTSWsl(cls, ta=None, **kwargs):
        return cls.jog(cls.path_nerSWRTSW())

    @classmethod
    def path_erSWRTSW(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(64.7131, 559.514),
            pyx.path.curveto(69.43726, 564.12468, 62.1061, 578.171, 53.9415, 578.171),
            pyx.path.moveto(55.8805, 572.844),
            pyx.path.lineto(52.0025, 583.498)).transformed(pyx.trafo.trafo().translated(-64.7131, -559.514).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_erSWRTSWsw(cls, ta=None, **kwargs):
        return cls.jog(cls.path_erSWRTSW())

    @classmethod
    def path_erSWRTSWsl(cls, ta=None, **kwargs):
        return cls.jog(cls.path_erSWRTSW())

    @classmethod
    def path_NELTSW(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(314.19638, 101.95087),
            pyx.path.curveto(320.95738, 98.047374, 331.50438, 90.904174, 334.17438, 83.566874),
            pyx.path.moveto(335.62863, 79.571324),
            pyx.path.lineto(332.72013, 87.562424)).transformed(pyx.trafo.trafo().translated(-314.19638, -101.95087).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_NELTSWsw(cls, ta=None, **kwargs):
        return cls.jog(cls.path_NELTSW())

    @classmethod
    def path_NELTSWsl(cls, ta=None, **kwargs):
        return cls.jog(cls.path_NELTSW())

    @classmethod
    def path_selNELTSW(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(122.29795, 453.66923),
            pyx.path.curveto(128.88142, 453.66923, 132.69129, 443.12672, 135.35395, 436.24347),
            pyx.path.moveto(136.29114, 432.09607),
            pyx.path.lineto(134.41677, 440.39087)).transformed(pyx.trafo.trafo().translated(-122.29795, -453.66923).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_selNELTSWsw(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELTSW())

    @classmethod
    def path_selNELTSWsl(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELTSW())

class CharSa_henki(CharSa):
    def __init__(self, name='sa', kana='さ',
                 model='SWR8', head_type='SWR', tail_type='SWR'):
        super().__init__(name, kana, model, head_type, tail_type)

    def to_reverse(self):
        return True
