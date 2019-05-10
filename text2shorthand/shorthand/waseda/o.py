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

class CharO(WasedaChar):
    def __init__(self, name='o', kana='お', model='SW4', head_type='SW', tail_type='SW'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5

    @classmethod
    def path_SW(cls, ta=-110):
        return pyx.path.line(0, 0, *PP(4, ta))

    @classmethod
    def path_SW_tan(cls, a):
        return cls.path_SW(a + 180)

    def get_paths(self):
        if self.before is None:
            paths = [self.path_SW()]
        elif self.before.tail_type == 'SWCL1':
            paths = [self.path_SW(self.before.head_angle)]
        elif self.before.tail_type in {'SW', 'SW|NE'}:
            paths = [self.path_SW(self.before.tail_angle+180+10)]
        elif self.before.tail_type in {'SERCR1'}:
            paths = [self.path_SW_tan(self.before.tail_angle)]
        else:
            paths = [self.path_SW()]

        if self.tail_type.endswith('F'):
            return paths

        if getattr(self.after, 'head_type', '') in {'SW', 'SL'}:
            paths = self.jog(paths)

        return paths


class CharOn(WasedaChar):
    def __init__(self, name='on', kana='おん', model='SW4NE1F', head_type='SW', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5

    @classmethod
    def path_SWNE(cls, ta = -110):
        return pyx.path.path(
            pyx.path.moveto(0, 0),
            pyx.path.rlineto(*PP(4, ta)),
            pyx.path.rlineto(*PP(1, 45)))

    @classmethod
    def path_SWNE_tan(cls, a):
        return cls.path_SWNE(a + 180)

    def get_paths(self):
        paths = [self.path_SWNE()]                           if self.before is None else \
                [self.path_SWNE(self.before.head_angle)]     if self.before.tail_type in {'SW'} else \
                [self.path_SWNE(self.before.tail_angle)]     if self.before.tail_type in {'ECL4'} else \
                [self.path_SWNE_tan(self.before.tail_angle)] if self.before.tail_type in {'SERCR1'} else \
                [self.path_SWNE()]

        return paths

class CharOku(CharO):
    def __init__(self, name='oku', kana='おく',
                 model='BSW4', head_type='BSW', tail_type='SW'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return self.barb(super().get_paths())


class CharTsuki(CharO):
    def __init__(self, name='tsuki', kana='つき', model='CR1SW4F',
    head_type='CR1', tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5

    def get_paths(self):
        return [self.path_CRSW()]

    @classmethod
    def path_CRSW(cls, ta=None, **kwargs):
        #M 46.022554,57.746558 C 43.780533,57.307478 44.540489,55.222819 45.26118,54.496973 45.716405,54.038492 48.111866,52.532066 46.65414,56.313481 45.475331,59.371372 44.467632,62.169126 43.4634,65.08

        #z0 = P(0, -0)
        #c0 = P(-0.790935, 0.154898)
        #c1 = P(-0.52284, 0.890319)
        #z1 = P(-0.268596, 1.14638)
        #c2 = P(-0.108003, 1.30812)
        #c3 = P(0.737063, 1.83956)
        #z2 = P(0.22281, 0.505558)
        #c4 = P(-0.193048, -0.573198)
        #c5 = P(-0.548542, -1.56018)
        z3 = P(-0.902813, -2.58708)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.790935, 0.154898)
        #z1 = z0 + P(-0.268596, 1.14638)
        #c1 = z1 + P(-0.254244, -0.256062)
        #c2 = z1 + P(0.160593, 0.161742)
        #z2 = z1 + P(0.491405, -0.640824)
        #c3 = z2 + P(0.514253, 1.334)
        #c4 = z2 + P(-0.415858, -1.07876)
        #z3 = z2 + P(-1.12562, -3.09263)
        #c5 = z3 + P(0.354271, 1.02689)

        z0 = P(0, -0)
        c0 = z0 + PP(0.80596, 168)
        z1 = z0 + PP(1.17743, 103)
        c1 = z1 + PP(0.360843, -134)
        c2 = z1 + PP(0.227927, 45)
        z2 = z1 + PP(0.807548, -52)
        #z2 = z3 - PP(3.29111, ta + 1)
        c3 = z2 + PP(1.42969, 68)
        c4 = z2 + PP(1.15614, -111)
        z3 = z2 + PP(3.29111, -109)
        c5 = z3 + PP(1.08628, 70)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

class CharOki(CharO):
    def __init__(self, name='oki', kana='おき', model='CL1SW4', head_type='CL1', tail_type='SW'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5

    @classmethod
    def path_CLSW(cls, ta=None, **kwargs):
        #M 46.081001,57.994217 C 48.307497,57.746247 49.127683,56.619753 48.789781,55.421106 48.634383,54.86986 47.531571,53.823507 47.109397,55.062641 45.972456,58.399707 44.703449,61.74088 43.4634,65.08

        #z0 = P(0, -0)
        #c0 = P(0.785458, 0.0874783)
        #c1 = P(1.0748, 0.48488)
        #z1 = P(0.955597, 0.907736)
        #c2 = P(0.900776, 1.1022)
        #c3 = P(0.511729, 1.47133)
        #z2 = P(0.362795, 1.03419)
        #c4 = P(-0.0382923, -0.143048)
        #c5 = P(-0.48597, -1.32174)
        z3 = P(-0.923431, -2.49971)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.785458, 0.0874783)
        #z1 = z0 + P(0.955597, 0.907736)
        #c1 = z1 + P(0.119204, -0.422856)
        #c2 = z1 + P(-0.054821, 0.194467)
        #z2 = z1 + P(-0.592802, 0.126458)
        #c3 = z2 + P(0.148934, 0.437139)
        #c4 = z2 + P(-0.401088, -1.17724)
        #z3 = z2 + P(-1.28623, -3.5339)
        #c5 = z3 + P(0.437462, 1.17797)

        z0 = P(0, -0)
        c0 = z0 + PP(0.790315, 6)
        z1 = z0 + PP(1.31801, 43)
        c1 = z1 + PP(0.439337, -74)
        c2 = z1 + PP(0.202047, 105)
        z2 = z1 + PP(0.60614, 167)
        #z2 = z3 - PP(3.7607, ta + 2)
        c3 = z2 + PP(0.461813, 71)
        c4 = z2 + PP(1.24369, -108)
        z3 = z2 + PP(3.7607, -109)
        c5 = z3 + PP(1.25657, 69)

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
        if getattr(self.after, 'head_type', '') in {'SW'}:
            return self.jog([self.path_CLSW()])
        else:
            return [self.path_CLSW()]

class CharShitsumon(CharOki):
    def __init__(self, name='shitsumon', kana='しつもん', model='CL1SW4F',
    head_type='CL1', tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_CLSW()]

class CharOtsu(CharO):
    def __init__(self, name='otsu', kana='おつ', model='CR1SW4', head_type='CRSW', tail_type='SW'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'SW', 'SL'}
        self.head_circles = {'', 'P', 'SW'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        bak = self.head_type
        self.head_type = 'CRSW'
        super().set_next_head(flick_len, dz)
        self.head_type = bak

    @classmethod
    def path_CRSW(cls, ta=None, **kwargs):
        #M 46.234079,57.335437 C 45.183062,56.527422 44.674476,54.64038 45.612968,54.022846 46.123551,53.686879 47.74108,53.387998 47.134363,55.046311 45.910709,58.390874 44.687054,61.735437 43.4634,65.08

        #z0 = P(0, -0)
        #c0 = P(-0.370775, 0.28505)
        #c1 = P(-0.550193, 0.950756)
        #z1 = P(-0.219114, 1.16861)
        #c2 = P(-0.0389918, 1.28713)
        #c3 = P(0.531636, 1.39257)
        #z2 = P(0.3176, 0.807553)
        #c4 = P(-0.114078, -0.372335)
        #c5 = P(-0.545756, -1.55222)
        z3 = P(-0.977434, -2.73211)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.370775, 0.28505)
        #z1 = z0 + P(-0.219114, 1.16861)
        #c1 = z1 + P(-0.331079, -0.217852)
        #c2 = z1 + P(0.180122, 0.118522)
        #z2 = z1 + P(0.536714, -0.361056)
        #c3 = z2 + P(0.214036, 0.585016)
        #c4 = z2 + P(-0.431678, -1.17989)
        #z3 = z2 + P(-1.29503, -3.53966)
        #c5 = z3 + P(0.431678, 1.17989)

        z0 = -PP(1.3, 70)
        c0 = z0 + PP(0.467683, 142)
        z1 = z0 + PP(1.18897, 100)
        c1 = z1 + PP(0.396324, -146)
        c2 = z1 + PP(0.215619, 33)
        z2 = z1 + PP(0.646857, -33)
        #z2 = z3 - PP(3.76913, ta + 1)
        c3 = z2 + PP(0.622941, 69)
        c4 = z2 + PP(1.25638, -110)
        z3 = z2 + PP(3.76913, -110)
        c5 = z3 + PP(1.25638, 69)

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
    def path_CRSWe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWsl(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRSW()])[0]

    @classmethod
    def path_CRSWsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWsw(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRSW()])[0]

    @classmethod
    def path_CRSWswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSWswl(cls, ta=None, **kwargs):
        pass

class CharNado(WasedaChar):
    def __init__(self, name='nado', kana='など', model='PSW4CNEL4', head_type='P', tail_type='SWCNEL4'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5
        self.tail_ligature -= {'EL', 'E'};

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        self.head = self.before.head + self.before.get_pos_aru()
        super(WasedaChar, self).set_next_head(flick_len, dz)

    def get_paths(self):
        return super(WasedaChar, self).get_paths(me='SWCNEL')

    @classmethod
    def path_SWCNEL(cls, ta=None, **kwargs):
        #M 403.495,160.109 C 402.25556,163.76713 400.95538,167.30376 399.617,170.764 401.13098,170.69838 403.3917,169.34038 404.81759,168.17457 405.96144,167.23936 408.24176,164.2438 406.76514,164.19284 405.64934,164.15433 401.5524,168.31145 399.617,170.764

        #z0 = P(0, -0)
        #c0 = P(-0.437247, -1.29051)
        #c1 = P(-0.895922, -2.53815)
        #z1 = P(-1.36807, -3.75885)
        #c2 = P(-0.833974, -3.7357)
        #c3 = P(-0.0364419, -3.25663)
        #z2 = P(0.46658, -2.84535)
        #c4 = P(0.870105, -2.51543)
        #c5 = P(1.67455, -1.45867)
        #z3 = P(1.15363, -1.44069)
        #c6 = P(0.760003, -1.4271)
        #c7 = P(-0.685306, -2.89364)
        z4 = P(-1.36807, -3.75885)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.437247, -1.29051)
        #z1 = z0 + P(-1.36807, -3.75885)
        #c1 = z1 + P(0.472151, 1.2207)
        #c2 = z1 + P(0.534099, 0.0231493)
        #z2 = z1 + P(1.83465, 0.913493)
        #c3 = z2 + P(-0.503022, -0.411272)
        #c4 = z2 + P(0.403525, 0.329921)
        #z3 = z2 + P(0.687052, 1.40467)
        #c5 = z3 + P(0.520919, -0.0179776)
        #c6 = z3 + P(-0.393629, 0.0135855)
        #z4 = z3 + P(-2.5217, -2.31816)
        #c7 = z4 + P(0.682766, 0.865205)

        z0 = P(0, -0)
        c0 = z0 + PP(1.36257, -108)
        z1 = z0 + PP(4.00007, -109)
        c1 = z1 + PP(1.30883, 68)
        c2 = z1 + PP(0.5346, 2)
        z2 = z1 + PP(2.04949, 26)
        c3 = z2 + PP(0.649751, -140)
        c4 = z2 + PP(0.52123, 39)
        z3 = z2 + PP(1.56369, 63)
        #z3 = z4 - PP(3.42533, ta + -8)
        c5 = z3 + PP(0.521229, -1)
        c6 = z3 + PP(0.393864, 178)
        z4 = z3 + PP(3.42533, -137)
        c7 = z4 + PP(1.10216, 51)

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
    def path_SWCNELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWCNELswl(cls, ta=None, **kwargs):
        pass
