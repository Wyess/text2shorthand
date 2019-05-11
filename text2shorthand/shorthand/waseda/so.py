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

class CharSo(WasedaChar):
    def __init__(self, name='so', kana='そ',
                 model='NEL16|SWR16', head_type='NEL|SWR',
                 tail_type='NEL|SWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = -7

    def get_pos_shita(self):
        return super().get_pos_shita() + P(1.5, 1.5)

    @classmethod
    def path_template(cls, ha=34, tn=1.6, ta=90, d=45, dz=P(0, 0)):
        z0 = P(0, 0)
        z1 = PP(16, d) + dz

        return pyx.metapost.path.path([
            beginknot(*z0, angle=ha),
            tensioncurve(tn),
            endknot(*z1, angle=ta)])

    @classmethod
    def path_template_reversed(cls, ha=-90, tn=1.6, ta=180, d=-120, dz = P(0, 0)):
        z0 = P(0, 0)
        z1 = PP(16, d) + dz

        return pyx.metapost.path.path([
            beginknot(*z0, angle=ha),
            tensioncurve(tn),
            endknot(*z1, angle=ta)])

    @classmethod
    def path_SWR(cls, ta=None, **kwargs):
        return cls.path_template_reversed()

    @classmethod
    def path_SWRer(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180)

    @classmethod
    def path_SWRe(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180)

    @classmethod
    def path_SWRel(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180+10)

    @classmethod
    def path_SWRner(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180-10, dz=P(3, 0))

    @classmethod
    def path_SWRne(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180)

    @classmethod
    def path_SWRnel(cls, ta=None, **kwargs):
        return cls.path_template_reversed(ta=ta+180, dz=P(3, 0))

    @classmethod
    def path_SWRsw(cls, ta=None, **kwargs):
        return cls.path_template_reversed(tn=2.0, ta=120, dz=P(2, 0))

    @classmethod
    def path_nerSWR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NEL(cls, ta=90, **kwargs):
        return cls.path_template()

    @classmethod
    def path_NELer(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.9, ta=120)

    @classmethod
    def path_NELe(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.5, ta=120)

    @classmethod
    def path_NELel(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.5, ta=120)

    @classmethod
    def path_NELne(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.5, ta=120)

    @classmethod
    def path_NELnel(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.5, ta=120)

    @classmethod
    def path_NELsw(cls, ta=None, **kwargs):
        return cls.path_template(ha=15, tn=1.6, ta=ta+180-5)

    @classmethod
    def path_NELswl(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.6, ta=ta+180+10)

    @classmethod
    def path_NELs(cls, ta=None, **kwargs):
        return cls.path_template(tn=1.6, ta=ta+180-5)

    @classmethod
    def path_NELsl(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta+180+10)

    @classmethod
    def path_elNEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNEL(cls, ta=None, **kwargs):
        #M 370.827,135.103 C 381.09465,135.103 402.897,113.255 402.897,103.032

        #z0 = P(0, -0)
        #c0 = P(3.6222, -0)
        #c1 = P(11.3136, 7.70749)
        #z1 = P(11.3136, 11.3139)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.6222, 0)
        #z1 = z0 + P(11.3136, 11.3139)
        #c1 = z1 + P(0, -3.60645)

        z0 = P(0, -0)
        c0 = z0 + PP(3.6222, 0)
        z1 = z0 + PP(16.0001, 45)
        c1 = z1 + PP(3.60645, -90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    @classmethod
    def path_selNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRNE(cls, ta=None, **kwargs):
        #M 315.718,213.047 C 315.718,223.039 301.271,246.563 293.041,252.325 294.93701,251.22013 296.12792,250.53691 297.56769,249.56303

        #z0 = P(0, -0)
        #c0 = P(0, -3.52496)
        #c1 = P(-5.09658, -11.8237)
        #z1 = P(-7.99994, -13.8564)
        #c2 = P(-7.33107, -13.4666)
        #c3 = P(-6.91094, -13.2256)
        #z2 = P(-6.40303, -12.882)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.52496)
        #z1 = z0 + P(-7.99994, -13.8564)
        #c1 = z1 + P(2.90336, 2.03271)
        #c2 = z1 + P(0.66887, 0.389774)
        #z2 = z1 + P(1.59692, 0.974362)
        #c3 = z2 + P(-0.507919, -0.343563)

        z0 = P(0, -0)
        c0 = z0 + PP(3.52496, -90)
        z1 = z0 + PP(16, -119)
        #z1 = z2 - PP(1.8707, ta + 356)
        c1 = z1 + PP(3.54421, 34)
        c2 = z1 + PP(0.774152, 30)
        z2 = z1 + PP(1.8707, 31)
        c3 = z2 + PP(0.613202, -145)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def to_reverse(self):
        if self.before:
            to_reverse = self.before.tail_type in {
                'ER', 'ERCL1', 'ERCL4', 'E', 'ECL1', 'ECL4', 'ELCL4', 
                'NER', 'NE', 'NECL1', 'NECL4', 'NECL4', 'NELCL4'}
            to_reverse = to_reverse and self.before.model != 'ER4' 
            to_reverse = to_reverse and self.before.model != 'ER8SWR4'
        else:
            to_reverse = False
        
        return to_reverse

    def get_paths(self):
        if self.to_reverse():
            if self.tail_type.endswith('F'):
                self.head_type = 'SWR'
                self.tail_type = 'NEF'
                self.model = 'SWR16NE1F'
                return [self.path_SWRNE()]

            self.head_type = 'SWR'
            self.tail_type = 'SWR'
            self.model = 'SWR16'

            self.head_ligature = {'NER'}
            self.tail_ligature = {'ER', 'E', 'EL', 'NER', 'NE', 'NEL', 'SW'}
            self.both_ligature = {}
            self.offset_from_centerline = 5
        else:
            if self.tail_type.endswith('F'):
                self.head_type = 'NEL'
                self.tail_type = 'NELF'
                self.model = 'NEL16F'
                
                if getattr(self.before, 'tail_type', '') == 'SEL':
                    return [self.path_selNEL()]
                else:
                    return [self.path_NEL()]
                    

            self.head_type = 'NEL'
            self.tail_type = 'NEL'
            self.model = 'NEL16'

            self.head_ligature = {'EL', 'SL', 'SEL'}
            self.tail_ligature = {'ER', 'E', 'EL', 'NE', 'NEL', 'SW', 'SWL', 'S', 'SL'}
            self.both_ligature = {}
            self.offset_from_centerline = -5

        return super().get_paths()

class CharSon(CharSo):
    def __init__(self, name='son', kana='そん',
                 model='NEL16|SWR16', head_type='NEL|SWR',
                 tail_type='NELF|NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSoku(CharSo):
    def __init__(self, name='soku', kana='そく',
                 model='SWR16F', head_type='SWR',
                 tail_type='SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def set_next_head(self, flick_len=3.0, dz=P(0, 0)):
        super().set_next_head(flick_len=flick_len, dz=dz)

    @classmethod
    def path_SWR(cls, ta=None, **kwargs):
        #M 58.68,696.818 C 58.68,708.82 45.569021,731.48305 36.6918,736.486
        z0 = P(0, -0)
        c0 = z0 + PP(4.23404, -90)
        z1 = z0 + PP(16.0001, -118)
        c1 = z1 + PP(3.59478, 29)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    def get_paths(self):
        return [self.path_SWR()]

class CharSoku(CharSo):
    def __init__(self, name='soku', kana='そく',
                 model='BNEL16|BSWR16', head_type='BNEL|BSWR',
                 tail_type='NEL|SWR'):
        super().__init__(name, kana, model, head_type, tail_type)

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if getattr(self.before, 'tail_type', '') not in {'', 'P'}:
            self.head = self.before.tail - self.get_pos_xku()
        super().set_next_head(flick_len=flick_len, dz=dz)

    def get_paths(self):
        before = self.before
        #self.before = None
        if getattr(self.before, 'tail_type', '') in {'', 'P'}:
            paths = self.barb(super().get_paths())
        else:
            paths = super().get_paths()

        self.before = before
        return paths
            
class CharSotsu(CharSo):
    def __init__(self, name='so', kana='そ',
                 model='CL1NEL16|SWR16', head_type='CL1NEL|SWR',
                 tail_type='NEL|SWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'ER', 'S', 'SW', 'SL', 'NEL', 'NE', 'SWL'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            self.head_type = 'C1NEL'
            self.tail_type = 'NEL'
            return super(WasedaChar, self).get_paths(me='CLNEL')
        else:
            return super().get_paths()

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        bak = self.head_type
        self.head_type = 'CLNEL'
        super().set_next_head(flick_len, dz)
        self.head_type = bak

    @classmethod
    def path_CLNEL_bend(cls, ta=None, **kwargs):
        #M 116.53,85.1045 C 116.695,83.2189 114.881,83.4309 113.799,84.217 113.143,84.7112 112.6,87.6204 114.226,86.6431 123.119,81.5088 151.1425,63.692278 146.031,54.8389

        #z0 = P(0, -0)
        #c0 = P(0.0582083, 0.665198)
        #c1 = P(-0.581731, 0.590409)
        #z1 = P(-0.963436, 0.31309)
        #c2 = P(-1.19486, 0.138747)
        #c3 = P(-1.38642, -0.887554)
        #z2 = P(-0.8128, -0.542784)
        #c4 = P(2.32445, 1.26848)
        #c5 = P(12.2105, 7.55376)
        z3 = P(10.4073, 10.677)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0582083, 0.665198)
        #z1 = z0 + P(-0.963436, 0.31309)
        #c1 = z1 + P(0.381706, 0.277319)
        #c2 = z1 + P(-0.231422, -0.174343)
        #z2 = z1 + P(0.150636, -0.855874)
        #c3 = z2 + P(-0.573617, -0.34477)
        #c4 = z2 + P(3.13725, 1.81127)
        #z3 = z2 + P(11.2201, 11.2198)
        #c5 = z3 + P(1.80322, -3.12328)

        z0 = P(0, -0)
        c0 = z0 + PP(0.66774, 84)
        z1 = z0 + PP(1.01303, 161)
        c1 = z1 + PP(0.47181, 35)
        c2 = z1 + PP(0.289744, -143)
        z2 = z1 + PP(0.869029, -80)
        #z2 = z3 - PP(15.8674, ta + 284)
        c3 = z2 + PP(0.669255, -148)
        c4 = z2 + PP(3.62257, 29)
        z3 = z2 + PP(15.8674, 44)
        c5 = z3 + PP(3.60645, -60)

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
    def path_CLNEL_tan(cls, ta=None, **kwargs):
        #M197.057 85.1045C197.222 83.2189 195.408 83.4309 194.326 84.217C193.67 84.7112 193.127 87.6204 194.754 86.6431C203.646 81.5088 226.558 65.0619 226.558 54.8389

        #z0 = P(0, -0)
        #c0 = P(0.0582083, 0.665198)
        #c1 = P(-0.581731, 0.590409)
        #z1 = P(-0.963436, 0.31309)
        #c2 = P(-1.19486, 0.138747)
        #c3 = P(-1.38642, -0.887554)
        #z2 = P(-0.812447, -0.542784)
        #c4 = P(2.32445, 1.26848)
        #c5 = P(10.4073, 7.07058)
        z3 = P(10.4073, 10.677)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0582083, 0.665198)
        #z1 = z0 + P(-0.963436, 0.31309)
        #c1 = z1 + P(0.381706, 0.277319)
        #c2 = z1 + P(-0.231422, -0.174343)
        #z2 = z1 + P(0.150989, -0.855874)
        #c3 = z2 + P(-0.573969, -0.34477)
        #c4 = z2 + P(3.1369, 1.81127)
        #z3 = z2 + P(11.2197, 11.2198)
        #c5 = z3 + P(0, -3.60645)

        z0 = P(0, -0)
        c0 = z0 + PP(0.66774, 84)
        z1 = z0 + PP(1.01303, 161)
        c1 = z1 + PP(0.47181, 35)
        c2 = z1 + PP(0.289744, -143)
        z2 = z1 + PP(0.86909, -79)
        #z2 = z3 - PP(15.8672, ta + 315)
        c3 = z2 + PP(0.669557, -149)
        #c4 = z2 + PP(3.62227, 30)
        #z3 = z2 + PP(15.8672, 45)
        #c5 = z3 + PP(3.60645, -90)

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
    def path_CLNEL(cls, ta=None, **kwargs):
        #M 50.0595,56.971031 C 50.203034,55.083653 48.389478,55.317438 47.317507,56.117161 46.659329,56.608182 46.109285,59.51212 47.741261,58.543913 56.572561,53.304541 79.4118,36.8298 79.4118,26.6068

        #z0 = P(0, -0)
        #c0 = P(0.0506356, 0.665825)
        #c1 = P(-0.589147, 0.583351)
        #z1 = P(-0.967314, 0.301226)
        #c2 = P(-1.1995, 0.128005)
        #c3 = P(-1.39355, -0.89644)
        #z2 = P(-0.817823, -0.554878)
        #c4 = P(2.29766, 1.29346)
        #c5 = P(10.3548, 7.10538)
        z3 = P(10.3548, 10.7118)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0506356, 0.665825)
        #z1 = z0 + P(-0.967314, 0.301226)
        #c1 = z1 + P(0.378168, 0.282125)
        #c2 = z1 + P(-0.232191, -0.173221)
        #z2 = z1 + P(0.149491, -0.856104)
        #c3 = z2 + P(-0.575725, -0.341562)
        #c4 = z2 + P(3.11549, 1.84833)
        #z3 = z2 + P(11.1727, 11.2667)
        #c5 = z3 + P(0, -3.60645)

        z0 = P(0, -0)
        c0 = z0 + PP(0.667748, 85)
        z1 = z0 + PP(1.01313, 162)
        c1 = z1 + PP(0.47181, 36)
        c2 = z1 + PP(0.289686, -143)
        z2 = z1 + PP(0.869058, -80)
        #z2 = z3 - PP(15.8672, ta + 315)
        c3 = z2 + PP(0.66942, -149)
        c4 = z2 + PP(3.62251, 30)
        z3 = z2 + PP(15.8672, 45)
        c5 = z3 + PP(3.60645, -90)

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
        return cls.path_CLNEL_bend()

    @classmethod
    def path_CLNELer(cls, ta=None, **kwargs):
        return cls.path_CLNEL_bend()

    @classmethod
    def path_CLNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELne(cls, ta=None, **kwargs):
        return cls.path_CLNEL_bend()

    @classmethod
    def path_CLNELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELnel(cls, ta=None, **kwargs):
        return cls.path_CLNEL_bend()

    @classmethod
    def path_CLNELs(cls, ta=None, **kwargs):
        return cls.path_CLNEL_tan(ta=ta)

    @classmethod
    def path_CLNELsl(cls, ta=None, **kwargs):
        return cls.path_CLNEL_tan(ta=ta)

    @classmethod
    def path_CLNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELsw(cls, ta=None, **kwargs):
        return cls.path_CLNEL_tan(ta=ta)

    @classmethod
    def path_CLNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLNELswl(cls, ta=None, **kwargs):
        return cls.path_CLNEL_tan(ta=ta)

class CharSoshi(CharSo):
    def __init__(self, name='so', kana='そし',
                 model='NEL16|SWR16', head_type='NEL|SWR',
                 tail_type='NELCR1|SWRCL1'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_ligature = {'ER', 'NER'}
            self.tail_ligature = {'SWL'}
            self.head_type = 'SWR'
            self.tail_type = 'SWRCL1'
            self.model = 'SWR16CL1'
            return super(WasedaChar, self).get_paths(me='SWRCL')
        else:
            self.head_ligature = {'EL', 'SL', 'SEL'}
            self.tail_ligature = {'NE', 'NER'}
            self.head_type = 'NEL'
            self.tail_type = 'NELCR1'
            self.model = 'NEL16CR1'
            return super(WasedaChar, self).get_paths(me='NELCR')

    @classmethod
    def path_NELCR(cls, ta=None, **kwargs):
        #M 47.3414,58.6772 C 55.8544,52.9351 77.848432,37.678531 79.127996,27.836616 79.555908,24.545281 81.78587,27.125115 81.770975,28.007829 81.751316,29.172871 80.855838,30.104291 78.508254,30.256143

        #z0 = P(0, -0)
        #c0 = P(3.0032, 2.02569)
        #c1 = P(10.7622, 7.40786)
        #z1 = P(11.2136, 10.8799)
        #c2 = P(11.3646, 12.041)
        #c3 = P(12.1512, 11.1309)
        #z2 = P(12.146, 10.8195)
        #c4 = P(12.1391, 10.4085)
        #c5 = P(11.8231, 10.0799)
        z3 = P(10.995, 10.0263)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.0032, 2.02569)
        #z1 = z0 + P(11.2136, 10.8799)
        #c1 = z1 + P(-0.451402, -3.47201)
        #c2 = z1 + P(0.150958, 1.16111)
        #z2 = z1 + P(0.932384, -0.0604001)
        #c3 = z2 + P(0.00525463, 0.311402)
        #c4 = z2 + P(-0.00693526, -0.411001)
        #z3 = z2 + P(-1.15102, -0.793155)
        #c5 = z3 + P(0.828175, 0.05357)

        z0 = P(0, -0)
        c0 = z0 + PP(3.62251, 34)
        z1 = z0 + PP(15.6242, 44)
        c1 = z1 + PP(3.50123, -97)
        c2 = z1 + PP(1.17088, 82)
        z2 = z1 + PP(0.934339, -3)
        #z2 = z3 - PP(1.39783, ta + 32)
        c3 = z2 + PP(0.311446, 89)
        c4 = z2 + PP(0.411059, -90)
        z3 = z2 + PP(1.39783, -145)
        c5 = z3 + PP(0.829906, 3)

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
    def path_NELCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCRne(cls, ta=None, **kwargs):
        #M 47.3414,100.939 C 55.8544,95.1967 77.9908,80.0238 79.2003,70.173 79.6622,66.8863 81.261289,68.679761 81.245889,69.562461 81.245889,70.727761 80.349389,71.262578 78.5994,72.5844

        #z0 = P(0, -0)
        #c0 = P(3.0032, 2.02576)
        #c1 = P(10.8124, 7.37842)
        #z1 = P(11.2391, 10.8536)
        #c2 = P(11.4021, 12.013)
        #c3 = P(11.9662, 11.3803)
        #z2 = P(11.9608, 11.0689)
        #c4 = P(11.9608, 10.6579)
        #c5 = P(11.6445, 10.4692)
        z3 = P(11.0271, 10.0029)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.0032, 2.02576)
        #z1 = z0 + P(11.2391, 10.8536)
        #c1 = z1 + P(-0.426685, -3.47514)
        #c2 = z1 + P(0.162948, 1.15947)
        #z2 = z1 + P(0.721638, 0.215385)
        #c3 = z2 + P(0.00543278, 0.311397)
        #c4 = z2 + P(0, -0.411092)
        #z3 = z2 + P(-0.933623, -1.06607)
        #c5 = z3 + P(0.617357, 0.466309)

        z0 = P(0, -0)
        c0 = z0 + PP(3.62255, 34)
        z1 = z0 + PP(15.6243, 44)
        c1 = z1 + PP(3.50124, -96)
        c2 = z1 + PP(1.17087, 82)
        z2 = z1 + PP(0.753095, 16)
        #z2 = z3 - PP(1.4171, ta + 12)
        c3 = z2 + PP(0.311444, 89)
        c4 = z2 + PP(0.411092, -90)
        z3 = z2 + PP(1.4171, -131)
        #c5 = z3 + PP(0.773676, 37)
        c5 = z3 + PP(0.773676, ta)

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
        #M 116.237,100.939 C 124.75,95.1967 146.886,80.0238 148.096,70.173 148.558,66.8863 150.38143,70.327867 150.36643,71.210567 149.93835,73.232021 147.0119,73.013988 147.94448,70.486811

        #z0 = P(0, -0)
        #c0 = P(3.0032, 2.02576)
        #c1 = P(10.8123, 7.37842)
        #z1 = P(11.2391, 10.8536)
        #c2 = P(11.4021, 12.013)
        #c3 = P(12.0454, 10.7989)
        #z2 = P(12.0401, 10.4875)
        #c4 = P(11.8891, 9.77441)
        #c5 = P(10.8567, 9.85132)
        z3 = P(11.1857, 10.7429)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.0032, 2.02576)
        #z1 = z0 + P(11.2391, 10.8536)
        #c1 = z1 + P(-0.426861, -3.47514)
        #c2 = z1 + P(0.162983, 1.15947)
        #z2 = z1 + P(0.800957, -0.366031)
        #c3 = z2 + P(0.00529167, 0.311397)
        #c4 = z2 + P(-0.151017, -0.713124)
        #z3 = z2 + P(-0.85441, 0.255325)
        #c5 = z3 + P(-0.328994, -0.891532)

        z0 = P(0, -0)
        c0 = z0 + PP(3.62255, 34)
        z1 = z0 + PP(15.6243, 44)
        c1 = z1 + PP(3.50126, -97)
        c2 = z1 + PP(1.17087, 81)
        #z2 = z1 + PP(0.880631, -24)
        z2 = z3 - PP(0.891744, ta + 453)
        c3 = z2 + PP(0.311442, 89)
        #c4 = z2 + PP(0.728939, -101)
        #z3 = z2 + PP(0.891744, 163)
        #c5 = z3 + PP(0.950298, -110)

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
    def path_NELCRnel(cls, ta=None, **kwargs):
        pass

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
    def path_SWRCL(cls, ta=None, **kwargs):
        #M 527.053,93.507 C 527.053,105.509 515.01232,131.43645 505.63778,132.53905 502.8243,132.86997 505.0678,134.75646 505.89569,135.16677 507.13105,135.77901 507.89996,133.50279 507.61351,132.07056

        #z0 = P(0, -0)
        #c0 = P(0, -4.23404)
        #c1 = P(-4.24768, -13.3807)
        #z1 = P(-7.55481, -13.7696)
        #c2 = P(-8.54735, -13.8864)
        #c3 = P(-7.75589, -14.5519)
        #z2 = P(-7.46383, -14.6966)
        #c4 = P(-7.02802, -14.9126)
        #c5 = P(-6.75677, -14.1096)
        z3 = P(-6.85782, -13.6044)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.23404)
        #z1 = z0 + P(-7.55481, -13.7696)
        #c1 = z1 + P(3.30713, 0.388973)
        #c2 = z1 + P(-0.992533, -0.116741)
        #z2 = z1 + P(0.0909849, -0.927001)
        #c3 = z2 + P(-0.292061, 0.144748)
        #c4 = z2 + P(0.435808, -0.215985)
        #z3 = z2 + P(0.606009, 1.09227)
        #c5 = z3 + P(0.101053, -0.505259)

        z0 = P(0, -0)
        c0 = z0 + PP(4.23404, -90)
        z1 = z0 + PP(15.706, -118)
        c1 = z1 + PP(3.32993, 6)
        c2 = z1 + PP(0.999375, -173)
        z2 = z1 + PP(0.931456, -84)
        #z2 = z3 - PP(1.24912, ta + 318)
        c3 = z2 + PP(0.325963, 153)
        c4 = z2 + PP(0.486392, -26)
        z3 = z2 + PP(1.24912, 60)
        c5 = z3 + PP(0.515265, -78)

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
        pass

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
        pass

    @classmethod
    def path_SWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCLswl(cls, ta=None, **kwargs):
        #M 70.0186,277.486 C 70.0186,289.488 58.5047,315.809 49.1173,316.796 46.3055,317.141 47.586777,318.67426 48.410077,319.09426 49.029677,319.39626 50.508835,318.45428 50.606493,317.70617 50.69223,317.04937 48.887523,316.7749 48.268655,317.06511

        #z0 = P(0, -0)
        #c0 = P(0, -4.23404)
        #c1 = P(-4.06185, -13.5195)
        #z1 = P(-7.37351, -13.8677)
        #c2 = P(-8.36545, -13.9894)
        #c3 = P(-7.91345, -14.5303)
        #z2 = P(-7.62301, -14.6785)
        #c4 = P(-7.40443, -14.785)
        #c5 = P(-6.88261, -14.4527)
        #z3 = P(-6.84816, -14.1888)
        #c6 = P(-6.81791, -13.9571)
        #c7 = P(-7.45457, -13.8603)
        z4 = P(-7.6729, -13.9626)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.23404)
        #z1 = z0 + P(-7.37351, -13.8677)
        #c1 = z1 + P(3.31167, 0.348192)
        #c2 = z1 + P(-0.991941, -0.121708)
        #z2 = z1 + P(-0.249493, -0.810775)
        #c3 = z2 + P(-0.290442, 0.148167)
        #c4 = z2 + P(0.218581, -0.106539)
        #z3 = z2 + P(0.774847, 0.489687)
        #c5 = z3 + P(-0.0344516, -0.263917)
        #c6 = z3 + P(0.0302461, 0.231704)
        #z4 = z3 + P(-0.824737, 0.226152)
        #c7 = z4 + P(0.218323, 0.10238)

        z0 = P(0, -0)
        c0 = z0 + PP(4.23404, -90)
        z1 = z0 + PP(15.7061, -117)
        c1 = z1 + PP(3.32992, 6)
        c2 = z1 + PP(0.999379, -173)
        z2 = z1 + PP(0.848294, -107)
        c3 = z2 + PP(0.326052, 152)
        c4 = z2 + PP(0.243163, -25)
        #z3 = z2 + PP(0.916614, 32)
        z3 = z4 - PP(0.855182, ta + 319)
        c5 = z3 + PP(0.266156, -97)
        #c6 = z3 + PP(0.23367, 82)
        #z4 = z3 + PP(0.855182, 164)
        #c7 = z4 + PP(0.241136, 25)

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
    def path_erSWRCL(cls, ta=None, **kwargs):
        #M 352.442,277.109 C 360.00418,286.42895 340.929,315.432 331.541,316.419 328.729,316.764 330.994,318.625 331.817,319.045 333.056,319.649 333.891,317.407 333.588,315.978

        #z0 = P(0, -0)
        #c0 = P(2.66777, -3.28787)
        #c1 = P(-4.06153, -13.5195)
        #z1 = P(-7.37341, -13.8677)
        #c2 = P(-8.36542, -13.9894)
        #c3 = P(-7.56638, -14.6459)
        #z2 = P(-7.27604, -14.7941)
        #c4 = P(-6.83895, -15.0072)
        #c5 = P(-6.54438, -14.2162)
        z3 = P(-6.65127, -13.7121)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.66777, -3.28787)
        #z1 = z0 + P(-7.37341, -13.8677)
        #c1 = z1 + P(3.31188, 0.348192)
        #c2 = z1 + P(-0.992011, -0.121708)
        #z2 = z1 + P(0.0973667, -0.926394)
        #c3 = z2 + P(-0.290336, 0.148167)
        #c4 = z2 + P(0.437092, -0.213078)
        #z3 = z2 + P(0.624769, 1.08197)
        #c5 = z3 + P(0.106892, -0.504119)

        z0 = P(0, -0)
        c0 = z0 + PP(4.23404, -50)
        z1 = z0 + PP(15.7061, -117)
        c1 = z1 + PP(3.33013, 6)
        c2 = z1 + PP(0.999449, -173)
        z2 = z1 + PP(0.931497, -84)
        #z2 = z3 - PP(1.2494, ta + 317)
        c3 = z2 + PP(0.325958, 152)
        c4 = z2 + PP(0.486263, -25)
        z3 = z2 + PP(1.2494, 59)
        c5 = z3 + PP(0.515327, -78)

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
    def path_erSWRCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCLswl(cls, ta=None, **kwargs):
        #M 363.267,395.361 C 370.982,404.555 352.443,434.043 343.055,435.03 340.243,435.375 342.40123,436.80236 343.022,437.11526 343.96279,437.58947 345.93121,436.17058 345.53266,435.19533 345.09206,434.1172 342.74809,435.31234 342.06503,435.62424

        #z0 = P(0, -0)
        #c0 = P(2.72168, -3.24344)
        #c1 = P(-3.81847, -13.6462)
        #z1 = P(-7.13034, -13.9943)
        #c2 = P(-8.12236, -14.1161)
        #c3 = P(-7.36098, -14.6196)
        #z2 = P(-7.14199, -14.73)
        #c4 = P(-6.8101, -14.8973)
        #c5 = P(-6.11568, -14.3967)
        #z3 = P(-6.25628, -14.0527)
        #c6 = P(-6.41171, -13.6723)
        #c7 = P(-7.23862, -14.0939)
        z4 = P(-7.47958, -14.204)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.72168, -3.24344)
        #z1 = z0 + P(-7.13034, -13.9943)
        #c1 = z1 + P(3.31188, 0.348192)
        #c2 = z1 + P(-0.992011, -0.121708)
        #z2 = z1 + P(-0.0116417, -0.735633)
        #c3 = z2 + P(-0.218994, 0.110384)
        #c4 = z2 + P(0.33189, -0.167291)
        #z3 = z2 + P(0.885705, 0.677309)
        #c5 = z3 + P(0.1406, -0.344047)
        #c6 = z3 + P(-0.155434, 0.38034)
        #z4 = z3 + P(-1.2233, -0.15131)
        #c7 = z4 + P(0.240968, 0.110031)

        z0 = P(0, -0)
        c0 = z0 + PP(4.23408, -49)
        z1 = z0 + PP(15.7062, -116)
        c1 = z1 + PP(3.33013, 6)
        c2 = z1 + PP(0.999449, -173)
        z2 = z1 + PP(0.735725, -90)
        c3 = z2 + PP(0.245241, 153)
        c4 = z2 + PP(0.371668, -26)
        #z3 = z2 + PP(1.115, 37)
        z3 = z4 - PP(1.23263, ta + -16)
        c5 = z3 + PP(0.371667, -67)
        #c6 = z3 + PP(0.410875, 112)
        #z4 = z3 + PP(1.23263, -172)
        #c7 = z4 + PP(0.264901, 24)

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
    def path_nerSWRCL(cls, ta=None, **kwargs):
        #M 404.114,645.28 C 410.21232,651.18793 392.6,683.603 383.213,684.59 380.401,684.935 382.665,686.796 383.489,687.215 384.728,687.82 385.563,685.578 385.259,684.149

        #z0 = P(0, -0)
        #c0 = P(2.15135, -2.08419)
        #c1 = P(-4.06188, -13.5195)
        #z1 = P(-7.37341, -13.8677)
        #c2 = P(-8.36542, -13.9894)
        #c3 = P(-7.56673, -14.6459)
        #z2 = P(-7.27604, -14.7937)
        #c4 = P(-6.83895, -15.0072)
        #c5 = P(-6.54438, -14.2162)
        z3 = P(-6.65162, -13.7121)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.15135, -2.08419)
        #z1 = z0 + P(-7.37341, -13.8677)
        #c1 = z1 + P(3.31152, 0.348192)
        #c2 = z1 + P(-0.992011, -0.121708)
        #z2 = z1 + P(0.0973667, -0.926042)
        #c3 = z2 + P(-0.290689, 0.147814)
        #c4 = z2 + P(0.437092, -0.213431)
        #z3 = z2 + P(0.624417, 1.08162)
        #c5 = z3 + P(0.107244, -0.504119)

        z0 = P(0, -0)
        c0 = z0 + PP(2.99535, -44)
        z1 = z0 + PP(15.7061, -117)
        c1 = z1 + PP(3.32978, 6)
        c2 = z1 + PP(0.999449, -173)
        z2 = z1 + PP(0.931146, -83)
        #2 = z3 - PP(1.24892, ta + 317)
        c3 = z2 + PP(0.326112, 153)
        c4 = z2 + PP(0.486417, -26)
        z3 = z2 + PP(1.24892, 60)
        c5 = z3 + PP(0.515401, -77)

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
        pass

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
        pass

    @classmethod
    def path_nerSWRCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCR(cls, ta=None, **kwargs):
        #M 70.0186,699.134 C 81.477412,699.1097 92.277737,671.52641 93.486737,661.67641 93.948737,658.38941 96.147737,660.93241 96.131737,661.81441 96.131737,662.97941 95.235737,663.96441 92.886737,664.08741

        #z0 = P(0, -0)
        #c0 = P(4.04241, 0.0085725)
        #c1 = P(7.85253, 9.73934)
        #z1 = P(8.27904, 13.2142)
        #c2 = P(8.44202, 14.3738)
        #c3 = P(9.21778, 13.4767)
        #z2 = P(9.21213, 13.1655)
        #c4 = P(9.21213, 12.7545)
        #c5 = P(8.89605, 12.407)
        z3 = P(8.06737, 12.3637)

        #z0 = P(0, -0)
        #c0 = z0 + P(4.04241, 0.0085725)
        #z1 = z0 + P(8.27904, 13.2142)
        #c1 = z1 + P(-0.426508, -3.47486)
        #c2 = z1 + P(0.162983, 1.15958)
        #z2 = z1 + P(0.933097, -0.0486833)
        #c3 = z2 + P(0.00564444, 0.31115)
        #c4 = z2 + P(0, -0.410986)
        #z3 = z2 + P(-1.14476, -0.801864)
        #c5 = z3 + P(0.828675, 0.0433917)

        z0 = P(0, -0)
        c0 = z0 + PP(4.04242, 0)
        z1 = z0 + PP(15.5935, 57)
        c1 = z1 + PP(3.50094, -96)
        c2 = z1 + PP(1.17098, 81)
        z2 = z1 + PP(0.934366, -2)
        #z2 = z3 - PP(1.39767, ta + 34)
        c3 = z2 + PP(0.311201, 88)
        c4 = z2 + PP(0.410986, -90)
        z3 = z2 + PP(1.39767, -144)
        c5 = z3 + PP(0.82981, 2)

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
    def path_selNELCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCRne(cls, ta=None, **kwargs):
        #M 384.999,616.183 C 396.458,616.183 408.036,588.981 409.073,579.112 409.593,575.833 411.36583,577.58228 411.33483,578.46328 411.33483,579.62828 410.36231,580.17697 408.515,581.533

        #z0 = P(0, -0)
        #c0 = P(4.04248, -0)
        #c1 = P(8.12694, 9.59626)
        #z1 = P(8.49277, 13.0778)
        #c2 = P(8.67622, 14.2346)
        #c3 = P(9.30163, 13.6175)
        #z2 = P(9.2907, 13.3067)
        #c4 = P(9.2907, 12.8957)
        #c5 = P(8.94761, 12.7021)
        z3 = P(8.29592, 12.2237)

        #z0 = P(0, -0)
        #c0 = z0 + P(4.04248, 0)
        #z1 = z0 + P(8.49277, 13.0778)
        #c1 = z1 + P(-0.365831, -3.48156)
        #c2 = z1 + P(0.183444, 1.15676)
        #z2 = z1 + P(0.797923, 0.228854)
        #c3 = z2 + P(0.0109361, 0.310797)
        #c4 = z2 + P(0, -0.410986)
        #z3 = z2 + P(-0.994773, -1.08293)
        #c5 = z3 + P(0.65169, 0.478377)

        z0 = P(0, -0)
        c0 = z0 + PP(4.04248, 0)
        z1 = z0 + PP(15.5935, 57)
        c1 = z1 + PP(3.50073, -95)
        c2 = z1 + PP(1.17121, 80)
        z2 = z1 + PP(0.830094, 16)
        #z2 = z3 - PP(1.47048, ta + 12)
        c3 = z2 + PP(0.31099, 87)
        c4 = z2 + PP(0.410986, -90)
        z3 = z2 + PP(1.47048, -132)
        #c5 = z3 + PP(0.808421, 36)
        c5 = z3 + PP(0.808421, ta)

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
        #M 468.829,616.183 C 480.288,616.183 491.866,588.981 492.904,579.112 493.423,575.833 495.22614,578.38308 495.551,579.204 495.97993,580.28789 494.17071,582.11003 493.08561,581.68414 492.28438,581.36967 492.63708,580.03811 492.99683,579.10345

        #z0 = P(0, -0)
        #c0 = P(4.04248, -0)
        #c1 = P(8.12694, 9.59626)
        #z1 = P(8.49312, 13.0778)
        #c2 = P(8.67622, 14.2346)
        #c3 = P(9.31232, 13.335)
        #z2 = P(9.42693, 13.0454)
        #c4 = P(9.57824, 12.663)
        #c5 = P(8.93999, 12.0202)
        #z3 = P(8.55719, 12.1704)
        #c6 = P(8.27454, 12.2814)
        #c7 = P(8.39896, 12.7511)
        z4 = P(8.52587, 13.0808)

        #z0 = P(0, -0)
        #c0 = z0 + P(4.04248, 0)
        #z1 = z0 + P(8.49312, 13.0778)
        #c1 = z1 + P(-0.366183, -3.48156)
        #c2 = z1 + P(0.183092, 1.15676)
        #z2 = z1 + P(0.933803, -0.0324556)
        #c3 = z2 + P(-0.114603, 0.289602)
        #c4 = z2 + P(0.151317, -0.382372)
        #z3 = z2 + P(-0.869735, -0.874938)
        #c5 = z3 + P(0.382799, -0.150245)
        #c6 = z3 + P(-0.282656, 0.110938)
        #z4 = z3 + P(-0.0313196, 0.91041)
        #c7 = z4 + P(-0.126912, -0.329727)

        z0 = P(0, -0)
        c0 = z0 + PP(4.04248, 0)
        z1 = z0 + PP(15.5937, 56)
        c1 = z1 + PP(3.50077, -96)
        c2 = z1 + PP(1.17116, 81)
        z2 = z1 + PP(0.934367, -1)
        c3 = z2 + PP(0.311454, 111)
        c4 = z2 + PP(0.411224, -68)
        z3 = z2 + PP(1.23368, -134)
        #z3 = z4 - PP(0.910949, ta + 382)
        c5 = z3 + PP(0.411228, -21)
        #c6 = z3 + PP(0.303647, 158)
        #z4 = z3 + PP(0.910949, 91)
        #c7 = z4 + PP(0.353308, -111)

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
        pass

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

