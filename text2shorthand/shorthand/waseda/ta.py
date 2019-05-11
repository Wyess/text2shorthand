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


class CharTa(WasedaChar):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'ta'
        self.kana      = 'た'
        self.model     = 'SW8|NE8'
        self.head_type = 'SW|NE' if reverse is None else \
                         'NE'    if reverse else \
                         'SW'
        self.tail_type = self.head_type
        self.tail_ligature = {'SW'}

    def to_reverse(self):
        return getattr(self.before, 'tail_type', '') in {
            'SWR', 'SWRCR1', 'SWRCR4', 'NELCL1|SWRCR1',  'SW', 'SR', 'S', 'SER'}

    @classmethod
    def path_NE(cls, a=34, **kwargs):
        return pyx.path.line(0, 0, *PP(8, a))

    @classmethod
    def path_NENE(cls, a=None, **kwargs):
        #M 40.166344,314.42502 C 46.374392,310.08065 52.629613,305.83063 58.966544,301.74402 59.067661,301.15785 59.259954,300.48371 59.721677,299.75827

        #z0 = P(0, -0)
        #c0 = P(2.19006, 1.5326)
        #c1 = P(4.39676, 3.03191)
        #z1 = P(6.63229, 4.47358)
        #c2 = P(6.66796, 4.68036)
        #c3 = P(6.7358, 4.91818)
        #z2 = P(6.89869, 5.1741)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.19006, 1.5326)
        #z1 = z0 + P(6.63229, 4.47358)
        #c1 = z1 + P(-2.23553, -1.44167)
        #c2 = z1 + P(0.0356718, 0.206788)
        #z2 = z1 + P(0.266394, 0.700528)
        #c3 = z2 + P(-0.162886, -0.255919)

        z0 = P(0, -0)
        c0 = z0 + PP(2.67305, 34)
        z1 = z0 + PP(8.00001, 34)
        #z1 = z2 - PP(0.74947, ta + 371)
        c1 = z1 + PP(2.66007, -147)
        c2 = z1 + PP(0.209842, 80)
        z2 = z1 + PP(0.74947, 69)
        c3 = z2 + PP(0.303358, -122)

        return pyx.metapost.path.path([
            pyx.metapost.path.beginknot(*z0),
            pyx.metapost.path.controlcurve(c0, c1),
            pyx.metapost.path.knot(*z1),
            pyx.metapost.path.controlcurve(c2, c3),
            #curve(),
            pyx.metapost.path.endknot(*z2)])

    @classmethod
    def path_SW(cls, a=-110, **kwargs):
        return pyx.path.line(0, 0, *PP(8, a))

    @classmethod
    def path_SWsw(cls, a=-110, **kwargs):
        return cls.jog(cls.path_SW())

    @classmethod
    def path_SWNE(cls, a=None, **kwargs):
        #M 175.069,136.68 C 172.49728,143.76939 169.94705,150.83728 167.313,157.989 168.2661,157.16413 169.46272,156.25534 170.60199,155.43535

        #z0 = P(0, -0)
        #c0 = P(-0.907246, -2.50098)
        #c1 = P(-1.80691, -4.99437)
        #z1 = P(-2.73614, -7.51734)
        #c2 = P(-2.39991, -7.22635)
        #c3 = P(-1.97777, -6.90574)
        #z2 = P(-1.57586, -6.61647)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.907246, -2.50098)
        #z1 = z0 + P(-2.73614, -7.51734)
        #c1 = z1 + P(0.929234, 2.52297)
        #c2 = z1 + P(0.336233, 0.290996)
        #z2 = z1 + P(1.16028, 0.900871)
        #c3 = z2 + P(-0.401909, -0.289274)

        z0 = P(0, -0)
        c0 = z0 + PP(2.66045, -109)
        z1 = z0 + PP(7.99981, -110)
        #z1 = z2 - PP(1.46895, ta + 361)
        c1 = z1 + PP(2.68865, 69)
        c2 = z1 + PP(0.444669, 40)
        z2 = z1 + PP(1.46895, 37)
        c3 = z2 + PP(0.495187, -144)

        return pyx.metapost.path.path([
            pyx.metapost.path.beginknot(*z0),
            pyx.metapost.path.controlcurve(c0, c1),
            pyx.metapost.path.knot(*z1),
            pyx.metapost.path.controlcurve(c2, c3),
            #curve(),
            pyx.metapost.path.endknot(*z2)])

    def get_paths(self):
        if self.to_reverse():
            self.head_type = self.tail_type = 'NE'
            return super(WasedaChar, self).get_paths(me='NE')
        else:
            self.head_type = self.tail_type = 'SW'
            return super(WasedaChar, self).get_paths(me='SW')


    def _get_paths(self):
        if self.before:
            if self.head_type == 'NE' or (self.head_type == 'SW|NE' and self.before.tail_type in {'SWR', 'SW', 'SR', 'S', 'SER'}):
                if self.tail_type.endswith('F'):
                    return [self.path_NENE()]

                path = self.path_NE()
                self.head_type = self.tail_type = 'NE'
            else:
                if self.name != 'shoku' and self.tail_type.endswith('F'):
                    return [self.path_SWNE()]

                path = self.path_SW()
                self.head_type = self.tail_type = 'SW'

        else:
            if self.name != 'shoku' and self.tail_type.endswith('F'):
                return [self.path_SWNE()]

            path = self.path_SW()
            self.head_type = self.tail_type = 'SW'

        
        if self.after and (self.after.head_type == self.head_type or self.after.head_type == 'CR1SW'):
            path = self.jog([path])[0]
        
        if self.after and self.after.head_type in {'ER'} and self.tail_type in {'NE'}:
            path = self.jog([path])[0]

        return [path]

class CharTan(CharTa):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'tan'
        self.kana      = 'たん'
        self.model     = 'SW8NE1F|NE8NE1F'
        self.head_type = 'SW|NE' if reverse is None else \
                         'NE'    if reverse else \
                         'SW'
        self.tail_type = 'NEF'

    def get_paths(self):
        if self.to_reverse():
            self.head_type = 'NE'
            self.tail_type = 'NEF'
            return super(WasedaChar, self).get_paths(me='NENE')
        else:
            self.head_type = 'SW'
            self.tail_type = 'NEF'
            return super(WasedaChar, self).get_paths(me='SWNE')


class CharTara(CharTa):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'tara'
        self.kana      = 'たら'
        self.model     = 'SW8F'
        self.head_type = 'SW'
        self.tail_type = 'SWF'

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') == 'SW':
            return [self.path_SW(self.before.tail_angle)]
        else:
            return [self.path_SW()]

class CharTari(CharTara):
    def __init__(self, to_reveArse = None):
        super().__init__()
        self.name      = 'tari'
        self.kana      = 'たり'
        self.model     = 'SW8F'
        self.head_type = 'SW'
        self.tail_type = 'SWF'

class CharToi(CharTara):
    def __init__(self):
        super().__init__()
        self.name      = 'toi'
        self.kana      = 'とい'
        self.model     = 'SW8F'
        self.head_type = 'SW'
        self.tail_type = 'SWF'

class CharShoku(CharTa):
    def __init__(self):
        super().__init__(reverse=False)
        self.name = 'shoku'
        self.kana = 'しょく'
        self.model = 'SW8F'
        self.head_type = 'SW'
        self.tail_type = 'SWF'
        self.to_flick = True

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {'P', ''}:
            return self.barb([self.path_SW()])
        else:
            return [self.path_SW()]

    def set_next_head(self):
        if self.before and self.before.tail_type != 'P':
            self.head = self.before.tail - self.get_pos_xku()

        super().set_next_head()

class CharTaki(CharTa):
    def __init__(self):
        super().__init__(reverse=False)
        self.name = 'taki'
        self.kana = 'たき'
        self.model = 'XCL1SW8'
        self.head_type = 'XCL'
        self.tail_type = 'SW'

    @classmethod
    def path_CLSW(cls, ta=None, **kwargs):
        #M 46.149472,140.32422 C 47.569761,141.36824 49.448059,139.31762 48.932782,137.80579 48.235171,135.75899 47.325268,136.3534 46.340085,139.30242 44.260932,145.52608 41.845925,151.75297 39.5854,157.989

        #z0 = P(0, -0)
        #c0 = P(0.501046, -0.368307)
        #c1 = P(1.16367, 0.355106)
        #z1 = P(0.98189, 0.888446)
        #c2 = P(0.735788, 1.61051)
        #c3 = P(0.414795, 1.40082)
        #z2 = P(0.067244, 0.360468)
        #c4 = P(-0.666235, -1.8351)
        #c5 = P(-1.5182, -4.03181)
        z3 = P(-2.31566, -6.23174)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.501046, -0.368307)
        #z1 = z0 + P(0.98189, 0.888446)
        #c1 = z1 + P(0.181778, -0.53334)
        #c2 = z1 + P(-0.246102, 0.722066)
        #z2 = z1 + P(-0.914646, -0.527978)
        #c3 = z2 + P(0.347551, 1.04035)
        #c4 = z2 + P(-0.733479, -2.19557)
        #z3 = z2 + P(-2.3829, -6.59221)
        #c5 = z3 + P(0.797463, 2.19993)

        z0 = P(0, -0)
        c0 = z0 + PP(0.62185, -36)
        z1 = z0 + PP(1.32418, 42)
        c1 = z1 + PP(0.563467, -71)
        c2 = z1 + PP(0.762853, 108)
        z2 = z1 + PP(1.0561, -150)
        #z2 = z3 - PP(7.00967, ta + 1)
        c3 = z2 + PP(1.09687, 71)
        c4 = z2 + PP(2.31485, -108)
        z3 = z2 + PP(7.00967, -109)
        c5 = z3 + PP(2.34001, 70)

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
    def path_XCLSW(cls, ta=None, **kwargs):
        #M 43.345268,140.39433 C 44.765557,141.43835 49.031292,139.95714 48.932782,137.87424 48.75248,134.06193 47.567293,136.45021 46.436895,139.35082 44.054242,145.46473 41.845925,151.75297 39.5854,157.989

        #z0 = P(0, -0)
        #c0 = P(0.501046, -0.368307)
        #c1 = P(2.0059, 0.154231)
        #z1 = P(1.97115, 0.889032)
        #c2 = P(1.90754, 2.23393)
        #c3 = P(1.48944, 1.3914)
        #z2 = P(1.09066, 0.368127)
        #c4 = P(0.25011, -1.78872)
        #c5 = P(-0.528935, -4.00708)
        z3 = P(-1.3264, -6.20701)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.501046, -0.368307)
        #z1 = z0 + P(1.97115, 0.889032)
        #c1 = z1 + P(0.0347521, -0.734801)
        #c2 = z1 + P(-0.0636065, 1.3449)
        #z2 = z1 + P(-0.880493, -0.520905)
        #c3 = z2 + P(0.398779, 1.02327)
        #c4 = z2 + P(-0.840547, -2.15685)
        #z3 = z2 + P(-2.41706, -6.57514)
        #c5 = z3 + P(0.797463, 2.19993)

        z0 = P(0, -0)
        c0 = z0 + PP(0.62185, -36)
        z1 = z0 + PP(2.16236, 24)
        c1 = z1 + PP(0.735622, -87)
        c2 = z1 + PP(1.3464, 92)
        z2 = z1 + PP(1.02304, -149)
        #z2 = z3 - PP(7.00532, ta + 0)
        c3 = z2 + PP(1.09823, 68)
        c4 = z2 + PP(2.31485, -111)
        z3 = z2 + PP(7.00532, -110)
        c5 = z3 + PP(2.34001, 70)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    def get_paths(self):
        if self.head_type == 'XCL':
            path = self.path_XCLSW()
        else:
            path = self.path_CLSW()

        if getattr(self.after, 'head_type', '') == 'SW':
            return self.jog([path])
        else:
            return [path]

class CharTaku(CharTa):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'taku'
        self.kana      = 'たく'
        self.model     = 'SW8|NE8'
        self.head_type = 'SW|NE' if reverse is None else \
                         'NE'    if reverse else \
                         'SW'
        self.tail_type = self.head_type

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {'', 'P'}:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()
        
    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.before and self.before.tail_type not in {'', 'P'}:
            self.head = self.before.tail - self.get_pos_xku()
        super().set_next_head(flick_len=flick_len, dz=dz)

class CharTatsu(CharTa):
    def __init__(self, reverse=False):
        super().__init__()
        self.name      = 'tatsu'
        self.kana      = 'たつ'
        self.model     = 'CR1SW8'
        self.head_type = 'CR1SW'

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            paths = [self.path_CRSW()]
        else:
            paths = [super().path_SW()]

        if getattr(self.after, 'head_type', '') in {'SW', 'SW|NE'}:
            paths = self.jog(paths)

        return paths

    @classmethod
    def path_CRSW(cls, ta=None, **kwargs):
        #M 46.044466,62.240675 C 44.891499,62.462019 44.004266,60.119332 44.750989,58.991799 45.330554,58.116672 47.905937,57.136508 47.031069,59.530061 44.549179,66.320265 42.06729,73.070466 39.5854,79.9867

        #z0 = P(0, -0)
        #c0 = P(-0.406741, -0.0780852)
        #c1 = P(-0.719737, 0.748363)
        #z1 = P(-0.45631, 1.14613)
        #c2 = P(-0.251852, 1.45486)
        #c3 = P(0.656686, 1.80064)
        #z2 = P(0.348052, 0.956244)
        #c4 = P(-0.527504, -1.43919)
        #c5 = P(-1.40306, -3.82051)
        z3 = P(-2.27861, -6.2604)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.406741, -0.0780852)
        #z1 = z0 + P(-0.45631, 1.14613)
        #c1 = z1 + P(-0.263427, -0.397769)
        #c2 = z1 + P(0.204458, 0.308725)
        #z2 = z1 + P(0.804362, -0.189887)
        #c3 = z2 + P(0.308634, 0.844392)
        #c4 = z2 + P(-0.875556, -2.39543)
        #z3 = z2 + P(-2.62667, -7.21665)
        #c5 = z3 + P(0.875556, 2.43989)

        z0 = P(0, -0)
        c0 = z0 + PP(0.414169, -169)
        z1 = z0 + PP(1.23363, 111)
        c1 = z1 + PP(0.477089, -123)
        c2 = z1 + PP(0.370289, 56)
        z2 = z1 + PP(0.826471, -13)
        #z2 = z3 - PP(7.6798, ta + 0)
        c3 = z2 + PP(0.899029, 69)
        c4 = z2 + PP(2.55043, -110)
        z3 = z2 + PP(7.6798, -110)
        c5 = z3 + PP(2.59223, 70)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

class CharTato(CharTa):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'ta'
        self.kana      = 'た'
        self.model     = 'SW8PSE1'
        self.head_type = 'SW'
        self.tail_type = 'P'
        self.tail_ligature = {'SW'}

    def to_reverse(self):
        return False

    def get_paths(self):
        if getattr(self.after, 'head_type', '') in {'', 'P'}:
            return self.path_SWPSE1()
        else:
            return self.path_SWPSE0()
    
    @classmethod
    def path_SWPSE1(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(47.3414, 58.6772),
            pyx.path.lineto(39.5854, 79.9867),
            pyx.path.moveto(41.071343, 75.904094),
            pyx.path.lineto(43.272834, 76.947594)).transformed(pyx.trafo.trafo().translated(-47.3414, -58.6772).scaled(25.4 / 72, -25.4 / 72))]

    @classmethod
    def path_SWPSE0(cls, ta=None, **kwargs):
        return [pyx.path.path(
            pyx.path.moveto(47.3414, 58.6772),
            pyx.path.lineto(39.5854, 79.9867),
            pyx.path.moveto(41.071343, 75.904094),
            pyx.path.lineto(41.419609, 76.129995)).transformed(pyx.trafo.trafo().translated(-47.3414, -58.6772).scaled(25.4 / 72, -25.4 / 72))]

class CharShou(CharTara):
    def __init__(self):
        super().__init__()
        self.name      = 'shou'
        self.kana      = 'しょう'
        self.model     = 'SW8F'
        self.head_type = 'SW'
        self.tail_type = 'SWF'


    def get_pos_chi(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(2, 45)

class CharTata(CharTa):
    def __init__(self, reverse = None):
        super().__init__()
        self.name      = 'tata'
        self.kana      = 'たた'
        self.model     = 'SW8CL4|NE8CR4'
        self.head_type = 'SW|NE' if reverse is None else \
                         'NE'    if reverse else \
                         'SW'

    def get_paths(self):
        if self.to_reverse():
            self.model = 'NE8CR4'
            self.head_type = 'NE'
            self.tail_type = 'NECR'
            self.head_ligature = {}
            self.tail_ligature = {
                'EL', 'E', 'ER', 'SR', 'NEL', 'NE',
                'NER', 'SER', 'SE'}
            return super(WasedaChar, self).get_paths(me='NECR')
        else:
            self.model = 'SW8CL4'
            self.head_type = 'SW'
            self.tail_type = 'SWCL'
            self.head_ligature = {}
            self.tail_ligature = {'S', 'SW', 'SL', 'SWL', 'SWR', 'SEL'}
            return super(WasedaChar, self).get_paths(me='SWCL')


    @classmethod
    def path_SWCL(cls, ta=None, **kwargs):
        #M 44.678171,143.25974 C 42.864944,148.78494 41.808778,152.87395 39.5854,157.989 38.033097,161.56019 36.697308,162.86341 38.096542,164.66256 38.726683,165.47281 40.44924,165.47902 41.17453,164.75271 43.464963,162.45906 43.403703,157.86203 40.876186,155.03297

        #z0 = P(0, -0)
        #c0 = P(-0.639666, -1.94917)
        #c1 = P(-1.01226, -3.39168)
        #z1 = P(-1.79662, -5.19616)
        #c2 = P(-2.34423, -6.45599)
        #c3 = P(-2.81547, -6.91574)
        #z2 = P(-2.32185, -7.55044)
        #c4 = P(-2.09955, -7.83628)
        #c5 = P(-1.49187, -7.83847)
        #z3 = P(-1.23601, -7.58224)
        #c6 = P(-0.427993, -6.77309)
        #c7 = P(-0.449604, -5.15136)
        z4 = P(-1.34126, -4.15333)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.639666, -1.94917)
        #z1 = z0 + P(-1.79662, -5.19616)
        #c1 = z1 + P(0.784358, 1.80448)
        #c2 = z1 + P(-0.547618, -1.25984)
        #z2 = z1 + P(-0.525236, -2.35428)
        #c3 = z2 + P(-0.493619, 0.6347)
        #c4 = z2 + P(0.2223, -0.285838)
        #z3 = z2 + P(1.08585, -0.0318029)
        #c5 = z3 + P(-0.255866, -0.256226)
        #c6 = z3 + P(0.808014, 0.809149)
        #z4 = z3 + P(-0.105249, 3.42891)
        #c7 = z4 + P(0.891652, -0.998029)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05145, -108)
        z1 = z0 + PP(5.49799, -109)
        c1 = z1 + PP(1.96758, 66)
        c2 = z1 + PP(1.37371, -113)
        z2 = z1 + PP(2.41216, -102)
        c3 = z2 + PP(0.804055, 127)
        c4 = z2 + PP(0.362106, -52)
        z3 = z2 + PP(1.08631, -1)
        #z3 = z4 - PP(3.43052, ta + 319)
        c5 = z3 + PP(0.362104, -134)
        c6 = z3 + PP(1.14351, 45)
        z4 = z3 + PP(3.43052, 91)
        c7 = z4 + PP(1.33832, -48)

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
    def path_SWCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLs(cls, ta=None, **kwargs):
        #M 188.346,127.125 C 186.549,132.655 185.54,136.766 183.272,141.861 181.75,145.445 179.87615,147.4094 181.85,148.549 184.44199,150.04549 185.31862,139.76553 185.31862,136.73231

        #z0 = P(0, -0)
        #c0 = P(-0.633942, -1.95086)
        #c1 = P(-0.989894, -3.40113)
        #z1 = P(-1.78999, -5.19853)
        #c2 = P(-2.32692, -6.46289)
        #c3 = P(-2.98797, -7.15589)
        #z2 = P(-2.29164, -7.55791)
        #c4 = P(-1.37725, -8.08584)
        #c5 = P(-1.06799, -4.4593)
        z3 = P(-1.06799, -3.38925)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633942, -1.95086)
        #z1 = z0 + P(-1.78999, -5.19853)
        #c1 = z1 + P(0.8001, 1.7974)
        #c2 = z1 + P(-0.536928, -1.26436)
        #z2 = z1 + P(-0.50165, -2.35938)
        #c3 = z2 + P(-0.69633, 0.402026)
        #c4 = z2 + P(0.914396, -0.527928)
        #z3 = z2 + P(1.22365, 4.16867)
        #c5 = z3 + P(0, -1.07005)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05128, -108)
        z1 = z0 + PP(5.49808, -108)
        c1 = z1 + PP(1.96744, 66)
        c2 = z1 + PP(1.37364, -113)
        z2 = z1 + PP(2.41212, -102)
        #z2 = z3 - PP(4.34455, ta + 343)
        c3 = z2 + PP(0.804053, 150)
        c4 = z2 + PP(1.05585, -30)
        z3 = z2 + PP(4.34455, 73)
        #c5 = z3 + PP(1.07005, -90)
        c5 = z3 + PP(1.07005, ta)

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
    def path_SWCLsl(cls, ta=None, **kwargs):
        #M 245.728,127.125 C 243.931,132.655 242.922,136.766 240.654,141.861 239.132,145.445 237.66348,146.89542 239.232,148.549 240.1787,149.54704 242.26949,148.80671 243.30828,147.90491 244.57277,146.80717 246.22814,143.9458 244.78159,143.10232 243.15741,142.15526 241.33566,142.29108 238.75032,146.61873

        #z0 = P(0, -0)
        #c0 = P(-0.633942, -1.95086)
        #c1 = P(-0.989894, -3.40113)
        #z1 = P(-1.78999, -5.19853)
        #c2 = P(-2.32692, -6.46289)
        #c3 = P(-2.84498, -6.97456)
        #z2 = P(-2.29164, -7.55791)
        #c4 = P(-1.95767, -7.91)
        #c5 = P(-1.22009, -7.64883)
        #z3 = P(-0.853623, -7.33069)
        #c6 = P(-0.407539, -6.94343)
        #c7 = P(0.176438, -5.934)
        #z4 = P(-0.333872, -5.63644)
        #c8 = P(-0.906847, -5.30234)
        #c9 = P(-1.54952, -5.35026)
        z5 = P(-2.46157, -6.87695)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633942, -1.95086)
        #z1 = z0 + P(-1.78999, -5.19853)
        #c1 = z1 + P(0.8001, 1.7974)
        #c2 = z1 + P(-0.536928, -1.26436)
        #z2 = z1 + P(-0.50165, -2.35938)
        #c3 = z2 + P(-0.553339, 0.583346)
        #c4 = z2 + P(0.333975, -0.352086)
        #z3 = z2 + P(1.43802, 0.227221)
        #c5 = z3 + P(-0.366462, -0.318135)
        #c6 = z3 + P(0.446084, 0.387258)
        #z4 = z3 + P(0.519751, 1.69425)
        #c7 = z4 + P(0.510311, -0.297561)
        #c8 = z4 + P(-0.572975, 0.334102)
        #z5 = z4 + P(-2.1277, -1.24051)
        #c9 = z5 + P(0.912051, 1.5267)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05128, -108)
        z1 = z0 + PP(5.49808, -108)
        c1 = z1 + PP(1.96744, 66)
        c2 = z1 + PP(1.37364, -113)
        z2 = z1 + PP(2.41212, -102)
        c3 = z2 + PP(0.804038, 133)
        c4 = z2 + PP(0.485287, -46)
        z3 = z2 + PP(1.45586, 8)
        c5 = z3 + PP(0.485288, -139)
        c6 = z3 + PP(0.590728, 40)
        #z4 = z3 + PP(1.77218, 72)
        z4 = z5 - PP(2.46292, ta + -28)
        c7 = z4 + PP(0.590728, -30)
        #c8 = z4 + PP(0.663268, 149)
        #z5 = z4 + PP(2.46292, -149)
        #c9 = z5 + PP(1.77838, 59)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_SWCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCLsel(cls, ta=None, **kwargs):
        #M 209.44,181.157 C 207.643,186.688 206.634,190.798 204.366,195.893 202.844,199.478 201.572,200.761 202.944,202.581 203.576,203.39 205.10643,203.59302 206.023,203.09989 207.78119,202.15397 209.17103,199.4834 208.44697,197.62283 208.06184,196.63319 206.51258,195.95058 205.52758,196.34744 203.44129,197.188 202.944,200.25077 202.944,202.581

        #z0 = P(0, -0)
        #c0 = P(-0.633942, -1.95121)
        #c1 = P(-0.989894, -3.40113)
        #z1 = P(-1.78999, -5.19853)
        #c2 = P(-2.32692, -6.46324)
        #c3 = P(-2.77566, -6.91586)
        #z2 = P(-2.29164, -7.55791)
        #c4 = P(-2.06869, -7.84331)
        #c5 = P(-1.52879, -7.91493)
        #z3 = P(-1.20544, -7.74096)
        #c6 = P(-0.585191, -7.40726)
        #c7 = P(-0.0948866, -6.46515)
        #z4 = P(-0.350319, -5.80878)
        #c8 = P(-0.486184, -5.45966)
        #c9 = P(-1.03273, -5.21885)
        #z5 = P(-1.38021, -5.35885)
        #c10 = P(-2.11621, -5.65538)
        #c11 = P(-2.29164, -6.73586)
        z6 = P(-2.29164, -7.55791)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633942, -1.95121)
        #z1 = z0 + P(-1.78999, -5.19853)
        #c1 = z1 + P(0.8001, 1.7974)
        #c2 = z1 + P(-0.536928, -1.26471)
        #z2 = z1 + P(-0.50165, -2.35938)
        #c3 = z2 + P(-0.484011, 0.642056)
        #c4 = z2 + P(0.222956, -0.285397)
        #z3 = z2 + P(1.0862, -0.183053)
        #c5 = z3 + P(-0.323346, -0.173965)
        #c6 = z3 + P(0.62025, 0.3337)
        #z4 = z3 + P(0.855123, 1.93219)
        #c7 = z4 + P(0.255432, -0.656368)
        #c8 = z4 + P(-0.135865, 0.349123)
        #z5 = z4 + P(-1.0299, 0.449929)
        #c9 = z5 + P(0.347486, 0.140003)
        #c10 = z5 + P(-0.735997, -0.296531)
        #z6 = z5 + P(-0.91143, -2.19906)
        #c11 = z6 + P(0, 0.822053)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05161, -107)
        z1 = z0 + PP(5.49808, -108)
        c1 = z1 + PP(1.96744, 66)
        c2 = z1 + PP(1.37396, -113)
        z2 = z1 + PP(2.41212, -102)
        c3 = z2 + PP(0.804054, 127)
        c4 = z2 + PP(0.362161, -52)
        z3 = z2 + PP(1.10152, -9)
        c5 = z3 + PP(0.367173, -151)
        c6 = z3 + PP(0.704319, 28)
        z4 = z3 + PP(2.11295, 66)
        c7 = z4 + PP(0.704318, -68)
        c8 = z4 + PP(0.374628, 111)
        #z5 = z4 + PP(1.12389, 156)
        z5 = z6 - PP(2.38046, ta + -22)
        c9 = z5 + PP(0.37463, 21)
        #c10 = z5 + PP(0.793487, -158)
        #z6 = z5 + PP(2.38046, -112)
        #c11 = z6 + PP(0.822053, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            #controlcurve(c10, c11),
            curve(),
            endknot(*z6, angle=ta)])

    @classmethod
    def path_SWCLsw(cls, ta=None, **kwargs):
        #M 213.108,127.125 C 211.312,132.655 210.303,136.766 208.035,141.861 206.513,145.445 205.19431,146.7652 206.613,148.549 207.25195,149.35239 208.84442,149.18205 209.692,148.603 211.0608,147.66786 211.41403,145.59686 211.41862,143.93912 211.42122,142.99846 211.37334,141.48425 210.45353,141.28727 208.56244,140.88228 206.76917,144.65279 206.41056,145.4486

        #z0 = P(0, -0)
        #c0 = P(-0.633589, -1.95086)
        #c1 = P(-0.989542, -3.40113)
        #z1 = P(-1.78964, -5.19853)
        #c2 = P(-2.32657, -6.46289)
        #c3 = P(-2.79177, -6.92863)
        #z2 = P(-2.29129, -7.55791)
        #c4 = P(-2.06588, -7.84133)
        #c5 = P(-1.5041, -7.78124)
        #z3 = P(-1.20509, -7.57696)
        #c6 = P(-0.722207, -7.24706)
        #c7 = P(-0.597595, -6.51646)
        #z4 = P(-0.595976, -5.93165)
        #c8 = P(-0.595058, -5.5998)
        #c9 = P(-0.611949, -5.06562)
        #z5 = P(-0.936438, -4.99613)
        #c10 = P(-1.60357, -4.85326)
        #c11 = P(-2.2362, -6.18341)
        z6 = P(-2.16271, -6.46416)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633589, -1.95086)
        #z1 = z0 + P(-1.78964, -5.19853)
        #c1 = z1 + P(0.8001, 1.7974)
        #c2 = z1 + P(-0.536928, -1.26436)
        #z2 = z1 + P(-0.50165, -2.35938)
        #c3 = z2 + P(-0.500482, 0.629285)
        #c4 = z2 + P(0.225407, -0.283418)
        #z3 = z2 + P(1.0862, -0.01905)
        #c5 = z3 + P(-0.299007, -0.204276)
        #c6 = z3 + P(0.482882, 0.329897)
        #z4 = z3 + P(0.609113, 1.64531)
        #c7 = z4 + P(-0.00161925, -0.584814)
        #c8 = z4 + P(0.000917222, 0.331844)
        #z5 = z4 + P(-0.340462, 0.935514)
        #c9 = z5 + P(0.324489, -0.0694902)
        #c10 = z5 + P(-0.667135, 0.142871)
        #z6 = z5 + P(-1.42627, -1.46802)
        #c11 = z6 + P(0.12651, 0.280744)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05117, -107)
        z1 = z0 + PP(5.49796, -108)
        c1 = z1 + PP(1.96744, 66)
        c2 = z1 + PP(1.37364, -113)
        z2 = z1 + PP(2.41212, -102)
        c3 = z2 + PP(0.804041, 128)
        c4 = z2 + PP(0.362125, -51)
        z3 = z2 + PP(1.08637, -1)
        c5 = z3 + PP(0.362124, -145)
        c6 = z3 + PP(0.584814, 34)
        z4 = z3 + PP(1.75444, 69)
        c7 = z4 + PP(0.584816, -90)
        c8 = z4 + PP(0.331845, 89)
        z5 = z4 + PP(0.99554, 109)
        #z5 = z6 - PP(2.04679, ta + -19)
        c9 = z5 + PP(0.331846, -12)
        #c10 = z5 + PP(0.682261, 167)
        #z6 = z5 + PP(2.04679, -134)
        #c11 = z6 + PP(0.307932, 65)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            #controlcurve(c10, c11),
            curve(),
            endknot(*z6, angle=ta)])

    @classmethod
    def path_SWCLswr(cls, ta=None, **kwargs):
        #M 133.713,181.157 C 131.916,186.688 130.908,190.798 128.639,195.893 127.118,199.478 125.846,200.761 127.218,202.581 127.85,203.39 129.48749,203.26691 130.296,202.635 131.77214,201.48128 132.87538,198.48992 131.55786,197.15794 130.62517,196.21502 128.50086,196.97422 127.67108,198.00886 126.72225,199.19194 127.62347,200.53228 127.68631,202.55853

        #z0 = P(0, -0)
        #c0 = P(-0.633942, -1.95121)
        #c1 = P(-0.989542, -3.40113)
        #z1 = P(-1.78999, -5.19853)
        #c2 = P(-2.32657, -6.46324)
        #c3 = P(-2.7753, -6.91586)
        #z2 = P(-2.29129, -7.55791)
        #c4 = P(-2.06834, -7.84331)
        #c5 = P(-1.49067, -7.79988)
        #z3 = P(-1.20544, -7.57696)
        #c6 = P(-0.684692, -7.16995)
        #c7 = P(-0.295494, -6.11467)
        #z4 = P(-0.760285, -5.64478)
        #c8 = P(-1.08932, -5.31213)
        #c9 = P(-1.83873, -5.57996)
        #z5 = P(-2.13146, -5.94496)
        #c10 = P(-2.46618, -6.36233)
        #c11 = P(-2.14825, -6.83517)
        z6 = P(-2.12608, -7.54998)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633942, -1.95121)
        #z1 = z0 + P(-1.78999, -5.19853)
        #c1 = z1 + P(0.800453, 1.7974)
        #c2 = z1 + P(-0.536575, -1.26471)
        #z2 = z1 + P(-0.501297, -2.35938)
        #c3 = z2 + P(-0.484011, 0.642056)
        #c4 = z2 + P(0.222956, -0.285397)
        #z3 = z2 + P(1.08585, -0.01905)
        #c5 = z3 + P(-0.285224, -0.222924)
        #c6 = z3 + P(0.520749, 0.407007)
        #z4 = z3 + P(0.445156, 1.93219)
        #c7 = z4 + P(0.464792, -0.469893)
        #c8 = z4 + P(-0.329032, 0.332641)
        #z5 = z4 + P(-1.37117, -0.300186)
        #c9 = z5 + P(0.292728, 0.364998)
        #c10 = z5 + P(-0.334726, -0.417364)
        #z6 = z5 + P(0.00537281, -1.60502)
        #c11 = z6 + P(-0.0221686, 0.714816)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05161, -107)
        z1 = z0 + PP(5.49808, -108)
        c1 = z1 + PP(1.96758, 65)
        c2 = z1 + PP(1.37383, -112)
        z2 = z1 + PP(2.41205, -101)
        c3 = z2 + PP(0.804054, 127)
        c4 = z2 + PP(0.362161, -52)
        z3 = z2 + PP(1.08602, -1)
        c5 = z3 + PP(0.362005, -141)
        c6 = z3 + PP(0.660935, 38)
        z4 = z3 + PP(1.9828, 77)
        c7 = z4 + PP(0.660932, -45)
        c8 = z4 + PP(0.467881, 134)
        z5 = z4 + PP(1.40364, -167)
        #z5 = z6 - PP(1.60503, ta + 0)
        c9 = z5 + PP(0.467882, 51)
        #c10 = z5 + PP(0.535009, -128)
        #z6 = z5 + PP(1.60503, -89)
        #c11 = z6 + PP(0.71516, 91)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            #controlcurve(c10, c11),
            curve(),
            endknot(*z6, angle=ta)])

    @classmethod
    def path_SWCLswl(cls, ta=None, **kwargs):
        #M 123.527,181.157 C 121.73,186.688 120.721,190.798 118.453,195.893 116.931,199.478 115.66,200.761 117.031,202.581 117.663,203.39 119.23754,203.17584 120.11,202.635 121.94725,201.49609 124.01927,198.6218 122.89217,196.77729 122.05548,195.40803 119.90502,195.829 118.08042,196.63114

        #z0 = P(0, -0)
        #c0 = P(-0.633942, -1.95121)
        #c1 = P(-0.989894, -3.40113)
        #z1 = P(-1.78999, -5.19853)
        #c2 = P(-2.32692, -6.46324)
        #c3 = P(-2.7753, -6.91586)
        #z2 = P(-2.29164, -7.55791)
        #c4 = P(-2.06869, -7.84331)
        #c5 = P(-1.51323, -7.76776)
        #z3 = P(-1.20544, -7.57696)
        #c6 = P(-0.557301, -7.17518)
        #c7 = P(0.173662, -6.16119)
        #z4 = P(-0.223954, -5.51049)
        #c8 = P(-0.51912, -5.02745)
        #c9 = P(-1.27775, -5.17596)
        z5 = P(-1.92143, -5.45893)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.633942, -1.95121)
        #z1 = z0 + P(-1.78999, -5.19853)
        #c1 = z1 + P(0.8001, 1.7974)
        #c2 = z1 + P(-0.536928, -1.26471)
        #z2 = z1 + P(-0.50165, -2.35938)
        #c3 = z2 + P(-0.483658, 0.642056)
        #c4 = z2 + P(0.222956, -0.285397)
        #z3 = z2 + P(1.0862, -0.01905)
        #c5 = z3 + P(-0.307785, -0.190796)
        #c6 = z3 + P(0.648141, 0.401782)
        #z4 = z3 + P(0.981488, 2.06647)
        #c7 = z4 + P(0.397616, -0.650702)
        #c8 = z4 + P(-0.295166, 0.483044)
        #z5 = z4 + P(-1.69748, 0.0515585)
        #c9 = z5 + P(0.643678, 0.282977)

        z0 = P(0, -0)
        c0 = z0 + PP(2.05161, -107)
        z1 = z0 + PP(5.49808, -108)
        c1 = z1 + PP(1.96744, 66)
        c2 = z1 + PP(1.37396, -113)
        z2 = z1 + PP(2.41212, -102)
        c3 = z2 + PP(0.803841, 126)
        c4 = z2 + PP(0.362161, -52)
        z3 = z2 + PP(1.08637, -1)
        c5 = z3 + PP(0.362125, -148)
        c6 = z3 + PP(0.762572, 31)
        #z4 = z3 + PP(2.28771, 64)
        z4 = z5 - PP(1.69826, ta + 335)
        c7 = z4 + PP(0.762569, -58)
        #c8 = z4 + PP(0.566087, 121)
        #z5 = z4 + PP(1.69826, 178)
        #c9 = z5 + PP(0.703134, 23)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_NECR(cls, ta=None, **kwargs):
        #M 245.96111,299.579 C 245.96111,299.70336 256.89112,292.70669 263.23204,287.96905 265.64574,286.16565 266.11557,288.67007 266.36671,289.86514 266.84103,292.12226 264.69316,294.97655 262.38853,295.52642 260.52106,295.97199 257.62115,295.43806 258.71634,291.0892

        #z0 = P(0, -0)
        #c0 = P(0, -0.0438714)
        #c1 = P(3.85586, 2.4244)
        #z1 = P(6.0928, 4.09573)
        #c2 = P(6.9443, 4.73193)
        #c3 = P(7.11005, 3.84843)
        #z2 = P(7.19864, 3.42683)
        #c4 = P(7.36597, 2.63057)
        #c5 = P(6.60825, 1.62364)
        #z3 = P(5.79523, 1.42966)
        #c6 = P(5.13643, 1.27247)
        #c7 = P(4.1134, 1.46083)
        z4 = P(4.49976, 2.99501)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0438714)
        #z1 = z0 + P(6.0928, 4.09573)
        #c1 = z1 + P(-2.23694, -1.67133)
        #c2 = z1 + P(0.8515, 0.636199)
        #z2 = z1 + P(1.10584, -0.668898)
        #c3 = z2 + P(-0.0885966, 0.421594)
        #c4 = z2 + P(0.16733, -0.796262)
        #z3 = z2 + P(-1.40341, -1.99717)
        #c5 = z3 + P(0.813022, 0.193982)
        #c6 = z3 + P(-0.658802, -0.157187)
        #z4 = z3 + P(-1.29547, 1.56535)
        #c7 = z4 + P(-0.386359, -1.53418)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0438714, -90)
        z1 = z0 + PP(7.34147, 33)
        c1 = z1 + PP(2.79235, -143)
        c2 = z1 + PP(1.06292, 36)
        z2 = z1 + PP(1.29241, -31)
        c3 = z2 + PP(0.430803, 101)
        c4 = z2 + PP(0.813653, -78)
        z3 = z2 + PP(2.44096, -125)
        #z3 = z4 - PP(2.03189, ta + 413)
        c5 = z3 + PP(0.835843, 13)
        c6 = z3 + PP(0.677294, -166)
        z4 = z3 + PP(2.03189, 129)
        c7 = z4 + PP(1.58208, -104)

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
    def path_NECRe(cls, ta=None, **kwargs):
        #M 316.84,202.467 C 316.84,202.591 327.972,195.896 334.293,191.133 336.731,189.362 337.56729,191.80588 337.434,193.02 336.99577,197.01174 330.55186,196.83581 326.00709,196.83581

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92712, 2.3181)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.0171, 4.62315)
        #c3 = P(7.31213, 3.76101)
        #z2 = P(7.26511, 3.33269)
        #c4 = P(7.11051, 1.92449)
        #c5 = P(4.83724, 1.98656)
        z3 = P(3.23395, 1.98656)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.22991, -1.68028)
        #c2 = z1 + P(0.860072, 0.624769)
        #z2 = z1 + P(1.10808, -0.665692)
        #c3 = z2 + P(0.0470217, 0.428315)
        #c4 = z2 + P(-0.154598, -1.4082)
        #z3 = z2 + P(-4.03116, -1.34613)
        #c5 = z3 + P(1.60329, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.3414, 32)
        c1 = z1 + PP(2.7921, -143)
        c2 = z1 + PP(1.06304, 35)
        z2 = z1 + PP(1.29266, -30)
        #z2 = z3 - PP(4.24998, ta + 19)
        c3 = z2 + PP(0.430888, 83)
        c4 = z2 + PP(1.41666, -96)
        z3 = z2 + PP(4.24998, -161)
        #c5 = z3 + PP(1.60329, 0)
        c5 = z3 + PP(1.60329, ta)

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
    def path_NECRer(cls, ta=None, **kwargs):
        #M 39.5854,272.214 C 39.5854,272.338 50.717,265.643 57.0385,260.88 59.4761,259.109 59.9457,261.568 60.1787,262.767 60.6583,265.023 58.5186,267.902 56.21,268.435 55.2786,268.667 53.651613,267.73276 53.45641,266.22226 53.261208,264.71176 54.834022,263.03679 58.964506,260.34605

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92698, 2.3181)
        #z1 = P(6.15707, 3.99838)
        #c2 = P(7.017, 4.62315)
        #c3 = P(7.18266, 3.75567)
        #z2 = P(7.26486, 3.33269)
        #c4 = P(7.43405, 2.53682)
        #c5 = P(6.67921, 1.52118)
        #z3 = P(5.86479, 1.33315)
        #c6 = P(5.53621, 1.2513)
        #c7 = P(4.96225, 1.58088)
        #z4 = P(4.89338, 2.11375)
        #c8 = P(4.82452, 2.64662)
        #c9 = P(5.37937, 3.23752)
        z5 = P(6.83652, 4.18675)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15707, 3.99838)
        #c1 = z1 + P(-2.23008, -1.68028)
        #c2 = z1 + P(0.859931, 0.624769)
        #z2 = z1 + P(1.10779, -0.665692)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.169192, -0.795867)
        #z3 = z2 + P(-1.40007, -1.99954)
        #c5 = z3 + P(0.814423, 0.188031)
        #c6 = z3 + P(-0.328577, -0.0818444)
        #z4 = z3 + P(-0.971405, 0.780605)
        #c7 = z4 + P(0.0688633, -0.532871)
        #c8 = z4 + P(-0.0688629, 0.532871)
        #z5 = z4 + P(1.94313, 2.073)
        #c9 = z5 + P(-1.45714, -0.949233)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.34143, 32)
        c1 = z1 + PP(2.79224, -143)
        c2 = z1 + PP(1.06293, 35)
        z2 = z1 + PP(1.29242, -31)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813652, -77)
        z3 = z2 + PP(2.44098, -124)
        c5 = z3 + PP(0.835847, 13)
        c6 = z3 + PP(0.338617, -166)
        z4 = z3 + PP(1.24618, 141)
        #z4 = z5 - PP(2.84132, ta + 372)
        c7 = z4 + PP(0.537302, -82)
        #c8 = z4 + PP(0.537302, 97)
        #z5 = z4 + PP(2.84132, 46)
        #c9 = z5 + PP(1.73905, -146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_NECRel(cls, ta=None, **kwargs):
        #M 271.909,202.467 C 271.909,202.591 283.04,195.896 289.362,191.133 291.799,189.362 292.269,191.821 292.502,193.02 292.981,195.276 290.78764,199.17431 288.533,198.688 286.6296,198.27745 285.97692,194.21761 287.45262,192.94726 288.81768,191.77215 288.99094,192.65865 292.55524,194.7253

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92677, 2.3181)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.01675, 4.62315)
        #c3 = P(7.18256, 3.75567)
        #z2 = P(7.26475, 3.33269)
        #c4 = P(7.43373, 2.53683)
        #c5 = P(6.65996, 1.16159)
        #z3 = P(5.86458, 1.33315)
        #c6 = P(5.1931, 1.47798)
        #c7 = P(4.96285, 2.9102)
        #z4 = P(5.48344, 3.35835)
        #c8 = P(5.96501, 3.77291)
        #c9 = P(6.02613, 3.46017)
        z5 = P(7.28353, 2.7311)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.23026, -1.68028)
        #c2 = z1 + P(0.859719, 0.624769)
        #z2 = z1 + P(1.10772, -0.665692)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.168981, -0.795867)
        #z3 = z2 + P(-1.40017, -1.99954)
        #c5 = z3 + P(0.795387, -0.171559)
        #c6 = z3 + P(-0.671477, 0.144833)
        #z4 = z3 + P(-0.381134, 2.02521)
        #c7 = z4 + P(-0.520594, -0.448151)
        #c8 = z4 + P(0.481563, 0.414553)
        #z5 = z4 + P(1.80009, -0.627253)
        #c9 = z5 + P(-1.25741, 0.729068)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.3414, 32)
        c1 = z1 + PP(2.79238, -143)
        c2 = z1 + PP(1.06276, 36)
        z2 = z1 + PP(1.29236, -31)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813608, -78)
        z3 = z2 + PP(2.44104, -125)
        c5 = z3 + PP(0.813679, -12)
        c6 = z3 + PP(0.686919, 167)
        #z4 = z3 + PP(2.06076, 100)
        z4 = z5 - PP(1.90625, ta + 12)
        c7 = z4 + PP(0.686919, -139)
        #c8 = z4 + PP(0.635419, 40)
        #z5 = z4 + PP(1.90625, -19)
        #c9 = z5 + PP(1.45348, 149)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_NECRne(cls, ta=None, **kwargs):
        #M 332.603,272.214 C 332.603,272.338 343.734,265.643 350.056,260.88 352.493,259.109 352.963,261.568 353.196,262.767 353.676,265.023 351.536,267.902 349.227,268.435 345.69258,268.899 343.71859,264.34243 350.22073,260.76466

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92677, 2.3181)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.01675, 4.62315)
        #c3 = P(7.18256, 3.75567)
        #z2 = P(7.26475, 3.33269)
        #c4 = P(7.43409, 2.53682)
        #c5 = P(6.67914, 1.52118)
        #z3 = P(5.86458, 1.33315)
        #c6 = P(4.61771, 1.16946)
        #c7 = P(3.92133, 2.77691)
        z4 = P(6.21514, 4.03907)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.23026, -1.68028)
        #c2 = z1 + P(0.859719, 0.624769)
        #z2 = z1 + P(1.10772, -0.665692)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.169333, -0.795867)
        #z3 = z2 + P(-1.40018, -1.99954)
        #c5 = z3 + P(0.814564, 0.188031)
        #c6 = z3 + P(-1.24686, -0.163689)
        #z4 = z3 + P(0.350566, 2.70593)
        #c7 = z4 + P(-2.29381, -1.26216)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.3414, 32)
        z4 = z1
        c1 = z1 + PP(2.79238, -143)
        c2 = z1 + PP(1.06276, 36)
        z2 = z1 + PP(1.29236, -31)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813681, -77)
        z3 = z2 + PP(2.44104, -125)
        #z3 = z4 - PP(2.72854, ta + 413)
        c5 = z3 + PP(0.835984, 12)
        #c6 = z3 + PP(1.25756, -172)
        #z4 = z3 + PP(2.72854, 82)
        #c7 = z4 + PP(2.61813, -151)

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
    def path_NECRner(cls, ta=None, **kwargs):
        #M 375.484,272.214 C 375.484,272.338 386.616,265.643 392.937,260.88 395.375,259.109 396.28244,260.69112 396.51544,261.89012 396.99544,264.14612 394.417,267.902 392.109,268.435 390.246,268.899 387.11385,268.22881 388.484,263.958

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92712, 2.3181)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.0171, 4.62315)
        #c3 = P(7.33723, 4.06502)
        #z2 = P(7.41942, 3.64204)
        #c4 = P(7.58876, 2.84617)
        #c5 = P(6.67914, 1.52118)
        #z3 = P(5.86493, 1.33315)
        #c6 = P(5.20771, 1.16946)
        #c7 = P(4.10275, 1.40589)
        z4 = P(4.58611, 2.91253)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.22991, -1.68028)
        #c2 = z1 + P(0.860072, 0.624769)
        #z2 = z1 + P(1.26239, -0.356348)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.169333, -0.795867)
        #z3 = z2 + P(-1.55449, -2.30889)
        #c5 = z3 + P(0.814211, 0.188031)
        #c6 = z3 + P(-0.657225, -0.163689)
        #z4 = z3 + P(-1.27882, 1.57939)
        #c7 = z4 + P(-0.483358, -1.50665)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.3414, 32)
        c1 = z1 + PP(2.7921, -143)
        c2 = z1 + PP(1.06304, 35)
        z2 = z1 + PP(1.31173, -15)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813681, -77)
        #z3 = z2 + PP(2.78342, -123)
        z3 = z4 - PP(2.0322, ta + 415)
        c5 = z3 + PP(0.835641, 13)
        #c6 = z3 + PP(0.677303, -166)
        #z4 = z3 + PP(2.0322, 128)
        #c7 = z4 + PP(1.58228, -107)

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
    def path_NECRnel(cls, ta=None, **kwargs):
        #M 240.849,272.214 C 240.849,272.338 251.981,265.643 258.302,260.88 260.74,259.109 261.21,261.568 261.443,262.767 261.922,265.023 259.77649,268.29912 257.474,268.435 255.8651,268.52995 253.92084,266.40497 254.25402,264.82808 254.76517,262.40889 259.67533,262.14502 261.0102,261.76579

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92712, 2.3181)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.0171, 4.62315)
        #c3 = P(7.18291, 3.75567)
        #z2 = P(7.26511, 3.33269)
        #c4 = P(7.43409, 2.53682)
        #c5 = P(6.6772, 1.38108)
        #z3 = P(5.86493, 1.33315)
        #c6 = P(5.29735, 1.29965)
        #c7 = P(4.61145, 2.0493)
        #z4 = P(4.72899, 2.60559)
        #c8 = P(4.90932, 3.45902)
        #c9 = P(6.64151, 3.55211)
        z5 = P(7.11242, 3.6859)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.22991, -1.68028)
        #c2 = z1 + P(0.860072, 0.624769)
        #z2 = z1 + P(1.10807, -0.665692)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.168981, -0.795867)
        #z3 = z2 + P(-1.40017, -1.99954)
        #c5 = z3 + P(0.812267, 0.0479354)
        #c6 = z3 + P(-0.567584, -0.0334962)
        #z4 = z3 + P(-1.13594, 1.27244)
        #c7 = z4 + P(-0.117538, -0.556292)
        #c8 = z4 + P(0.180322, 0.853436)
        #z5 = z4 + P(2.38343, 1.08031)
        #c9 = z5 + P(-0.470912, -0.133784)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.3414, 32)
        c1 = z1 + PP(2.7921, -143)
        c2 = z1 + PP(1.06304, 35)
        z2 = z1 + PP(1.29266, -30)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813608, -78)
        z3 = z2 + PP(2.44104, -125)
        c5 = z3 + PP(0.813681, 3)
        c6 = z3 + PP(0.568572, -176)
        z4 = z3 + PP(1.70571, 131)
        #z4 = z5 - PP(2.61683, ta + 368)
        c7 = z4 + PP(0.568573, -101)
        #c8 = z4 + PP(0.872279, 78)
        #z5 = z4 + PP(2.61683, 24)
        #c9 = z5 + PP(0.489547, -164)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_NECRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECRsr(cls, ta=None, **kwargs):
        #M 84.5172,272.214 C 84.5172,272.338 95.6488,265.643 101.97,260.88 104.408,259.109 105.46259,261.12956 105.69559,262.32856 106.17459,264.58456 105.20376,266.73283 102.89576,267.26583 101.03276,267.72983 99.402531,267.58896 97.5171,263.958

        #z0 = P(0, -0)
        #c0 = P(0, -0.0437444)
        #c1 = P(3.92698, 2.3181)
        #z1 = P(6.15696, 3.99838)
        #c2 = P(7.01703, 4.62315)
        #c3 = P(7.38907, 3.91034)
        #z2 = P(7.47127, 3.48736)
        #c4 = P(7.64025, 2.6915)
        #c5 = P(7.29776, 1.93363)
        #z3 = P(6.48355, 1.7456)
        #c6 = P(5.82632, 1.58192)
        #c7 = P(5.25121, 1.63161)
        z4 = P(4.58608, 2.91253)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0437444)
        #z1 = z0 + P(6.15696, 3.99838)
        #c1 = z1 + P(-2.22998, -1.68028)
        #c2 = z1 + P(0.860072, 0.624769)
        #z2 = z1 + P(1.31431, -0.51102)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.168981, -0.795867)
        #z3 = z2 + P(-0.987718, -1.74176)
        #c5 = z3 + P(0.814211, 0.188031)
        #c6 = z3 + P(-0.657225, -0.163689)
        #z4 = z3 + P(-1.89747, 1.16693)
        #c7 = z4 + P(0.665138, -1.28092)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0437444, -90)
        z1 = z0 + PP(7.34134, 33)
        c1 = z1 + PP(2.79216, -143)
        c2 = z1 + PP(1.06304, 35)
        z2 = z1 + PP(1.41016, -21)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813608, -78)
        z3 = z2 + PP(2.00233, -119)
        #z3 = z4 - PP(2.22758, ta + 390)
        c5 = z3 + PP(0.835641, 13)
        c6 = z3 + PP(0.677303, -166)
        z4 = z3 + PP(2.22758, 148)
        #c7 = z4 + PP(1.44332, -62)
        c7 = z4 + PP(1.44332, ta)

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
    def path_NECRse(cls, ta=None, **kwargs):
        #M 121.557,327.384 C 121.557,327.509 132.689,320.814 139.01,316.05 141.448,314.279 142.1078,316.04665 142.51463,317.20774 143.14955,319.01982 141.24059,321.60478 139.36891,322.03323 137.54268,322.45127 135.5341,320.8214 134.557,319.129

        #z0 = P(0, -0)
        #c0 = P(0, -0.0440972)
        #c1 = P(3.92712, 2.31775)
        #z1 = P(6.15703, 3.99838)
        #c2 = P(7.0171, 4.62315)
        #c3 = P(7.24987, 3.99957)
        #z2 = P(7.39339, 3.58996)
        #c4 = P(7.61737, 2.9507)
        #c5 = P(6.94393, 2.03878)
        #z3 = P(6.28365, 1.88763)
        #c6 = P(5.63939, 1.74016)
        #c7 = P(4.93081, 2.31514)
        z4 = P(4.58611, 2.91218)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0440972)
        #z1 = z0 + P(6.15703, 3.99838)
        #c1 = z1 + P(-2.22991, -1.68063)
        #c2 = z1 + P(0.860072, 0.624769)
        #z2 = z1 + P(1.23636, -0.408425)
        #c3 = z2 + P(-0.143521, 0.409607)
        #c4 = z2 + P(0.223986, -0.639262)
        #z3 = z2 + P(-1.10974, -1.70233)
        #c5 = z3 + P(0.660287, 0.151148)
        #c6 = z3 + P(-0.644253, -0.147475)
        #z4 = z3 + P(-1.69753, 1.02455)
        #c7 = z4 + P(0.344699, -0.597041)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0440972, -90)
        z1 = z0 + PP(7.3414, 32)
        c1 = z1 + PP(2.79231, -142)
        c2 = z1 + PP(1.06304, 35)
        z2 = z1 + PP(1.30207, -18)
        c3 = z2 + PP(0.434023, 109)
        c4 = z2 + PP(0.677366, -70)
        z3 = z2 + PP(2.0321, -123)
        #z3 = z4 - PP(1.98276, ta + 388)
        c5 = z3 + PP(0.677366, 12)
        c6 = z3 + PP(0.660917, -167)
        z4 = z3 + PP(1.98276, 148)
        #c7 = z4 + PP(0.689402, -60)
        c7 = z4 + PP(0.689402, ta)

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
    def path_NECRser(cls, ta=None, **kwargs):
        #M 82.2945,327.384 C 82.2945,327.509 93.4261,320.814 99.7476,316.05 102.185,314.279 102.655,316.738 102.888,317.937 103.367,320.193 101.46648,323.01135 99.557202,322.69343 97.719983,322.3875 96.797916,318.74056 98.008207,317.32488 99.073479,316.07882 101.44844,316.87163 102.888,317.937

        #z0 = P(0, -0)
        #c0 = P(0, -0.0440972)
        #c1 = P(3.92698, 2.31775)
        #z1 = P(6.15707, 3.99838)
        #c2 = P(7.01693, 4.62315)
        #c3 = P(7.18273, 3.75567)
        #z2 = P(7.26493, 3.33269)
        #c4 = P(7.43391, 2.53683)
        #c5 = P(6.76345, 1.54257)
        #z3 = P(6.0899, 1.65473)
        #c6 = P(5.44177, 1.76265)
        #c7 = P(5.11648, 3.04921)
        #z4 = P(5.54345, 3.54863)
        #c8 = P(5.91925, 3.98822)
        #c9 = P(6.75708, 3.70853)
        z5 = P(7.26493, 3.33269)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -0.0440972)
        #z1 = z0 + P(6.15707, 3.99838)
        #c1 = z1 + P(-2.23008, -1.68063)
        #c2 = z1 + P(0.859861, 0.624769)
        #z2 = z1 + P(1.10786, -0.665692)
        #c3 = z2 + P(-0.0821972, 0.422981)
        #c4 = z2 + P(0.168981, -0.795867)
        #z3 = z2 + P(-1.17503, -1.67796)
        #c5 = z3 + P(0.673551, -0.112155)
        #c6 = z3 + P(-0.64813, 0.107925)
        #z4 = z3 + P(-0.546451, 1.89391)
        #c7 = z4 + P(-0.426964, -0.49942)
        #c8 = z4 + P(0.375804, 0.439582)
        #z5 = z4 + P(1.72148, -0.215942)
        #c9 = z5 + P(-0.507845, 0.375839)

        z0 = P(0, -0)
        c0 = z0 + PP(0.0440972, -90)
        z1 = z0 + PP(7.34143, 32)
        c1 = z1 + PP(2.79246, -142)
        c2 = z1 + PP(1.06287, 36)
        z2 = z1 + PP(1.29248, -31)
        c3 = z2 + PP(0.430893, 100)
        c4 = z2 + PP(0.813608, -78)
        z3 = z2 + PP(2.04848, -125)
        c5 = z3 + PP(0.682825, -9)
        c6 = z3 + PP(0.657054, 170)
        #z4 = z3 + PP(1.97116, 106)
        z4 = z5 - PP(1.73497, ta + 30)
        c7 = z4 + PP(0.657053, -130)
        #c8 = z4 + PP(0.578326, 49)
        #z5 = z4 + PP(1.73497, -7)
        #c9 = z5 + PP(0.631792, 143)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_NECRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECRswl(cls, ta=None, **kwargs):
        pass

