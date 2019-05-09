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

class CharI(WasedaChar):
    def __init__(self, name='i', kana='い',
                 model='ER4', head_type='ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_ER(cls, ta=-90):
        return mpath([
            beginknot(0, 0, angle=30),
            tensioncurve(1.2),
            endknot(4, 0, angle=ta)])

    @classmethod
    def path_ER_smooth(cls, ta=-90):
        return cls.path_ER(ta=ta)

    @classmethod
    def path_ER_down(cls, ta=-110, deep=False):
        if deep:
            return cls.path_ER(ta=ta-90+10)
        else:
            return cls.path_ER(ta)

    @classmethod
    def path_ERNE(cls, ta=None):
        #M 47.3414,172.063 C 52.5553,169.053 59.9456,168.586 58.68,172.063 59.449333,171.5946 60.218667,171.12621 60.988,170.65781

        #z0 = P(0, -0)
        #c0 = P(1.83248, 1.05789)
        #c1 = P(4.42987, 1.22203)
        #z1 = P(3.98506, -0)
        #c2 = P(4.25545, 0.164624)
        #c3 = P(4.52584, 0.329244)
        #z2 = P(4.79623, 0.493868)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.83248, 1.05789)
        #z1 = z0 + P(3.98506, 0)
        #c1 = z1 + P(0.444808, 1.22203)
        #c2 = z1 + P(0.27039, 0.164624)
        #z2 = z1 + P(0.811169, 0.493868)
        #c3 = z2 + P(-0.27039, -0.164624)

        z0 = P(0, -0)
        c0 = z0 + PP(2.11592, 29)
        z1 = z0 + PP(3.98506, 0)
        #z1 = z2 - PP(0.949685, ta + 359)
        c1 = z1 + PP(1.30046, 69)
        c2 = z1 + PP(0.316562, 31)
        z2 = z1 + PP(0.949685, 31)
        c3 = z2 + PP(0.316562, -148)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_ER_cr1(cls, ta=-90):
        return mpath([
            beginknot(0, 0, angle=28),
            tensioncurve(1.75, 1.1),
            endknot(*PP(4, 4), angle=ta)])

    def get_paths(self):
        if self.after is None:
            return [self.path_ER()]

        if self.tail_type.endswith('F'):
            return [self.path_ERNE()]

        if self.after.head_type in {'EL', 'SW', 'SWR'}:
            return [self.path_ER_smooth(self.after.head_angle)]
        
        if self.after.head_type in {'E', 'N', 
                                    'NL', 'NW', 'SR', 'SE', 'SER'}:
            return [self.path_ER_down(ta=self.after.head_angle, deep=True)] 

        if self.after.head_type in {'NE', 'NER'}:
            return [self.path_ER_down(deep=False)] 
        
        return [self.path_ER()]

class CharIn(CharI):
    def __init__(self, name='in', kana='いん',
                 model='ER4F', head_type='ER', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharIku(CharI):
    def __init__(self, name='iku', kana='いく',
                 model='BER4', head_type='BER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {'', 'P', 'E'}:
            return self.barb(super().get_paths())
        else:
            paths = super().get_paths()
            paths[-1] = (
                paths[-1].transformed(pyx.trafo.translate(*(-P(*paths[-1].at(2))))))
            return paths

class CharItsu(CharI):
    def __init__(self, name='itsu', kana='いつ',
                 model='CR1ER4', head_type='CR1ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'EL', 'SR', 'S', 'SW', 'SWR', 'SER', 'SE'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()

    @classmethod
    def path_CRER(cls, ta=None, **kwargs):
        #M 51.577794,55.996783 C 51.424916,57.500559 51.06808,58.587765 50.037375,58.698316 49.418922,58.764649 47.797323,57.930714 48.790331,57.310208 53.17309,54.571528 59.849175,54.587713 59.849175,58.092613

        #z0 = P(0, -0)
        #c0 = P(-0.053932, -0.530499)
        #c1 = P(-0.179816, -0.914041)
        #z1 = P(-0.543426, -0.953041)
        #c2 = P(-0.761602, -0.976442)
        #c3 = P(-1.33367, -0.682248)
        #z2 = P(-0.983355, -0.463347)
        #c4 = P(0.562785, 0.502798)
        #c5 = P(2.91796, 0.497089)
        z3 = P(2.91796, -0.739362)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.053932, -0.530499)
        #z1 = z0 + P(-0.543426, -0.953041)
        #c1 = z1 + P(0.36361, 0.0389999)
        #c2 = z1 + P(-0.218176, -0.0234008)
        #z2 = z1 + P(-0.439929, 0.489694)
        #c3 = z2 + P(-0.350311, -0.218901)
        #c4 = z2 + P(1.54614, 0.966145)
        #z3 = z2 + P(3.90131, -0.276015)
        #c5 = z3 + P(0, 1.23645)

        z0 = P(0, -0)
        c0 = z0 + PP(0.533233, -95)
        z1 = z0 + PP(1.09709, -119)
        c1 = z1 + PP(0.365695, 6)
        c2 = z1 + PP(0.219428, -173)
        z2 = z1 + PP(0.658284, 131)
        #z2 = z3 - PP(3.91107, ta + 86)
        c3 = z2 + PP(0.41308, -147)
        c4 = z2 + PP(1.82318, 32)
        z3 = z2 + PP(3.91107, -4)
        c5 = z3 + PP(1.23645, 90)

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
    def path_CRERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERel(cls, ta=None, **kwargs):
        #M 47.3414,117.60116 C 47.2097,119.10716 46.8647,120.067 45.8337,120.175 45.2164,120.251 43.6275,119.404 44.6095,118.767 48.9923,116.028 52.775674,117.82531 55.669,119.54

        #z0 = P(0, -0)
        #c0 = P(-0.0464608, -0.531283)
        #c1 = P(-0.168169, -0.869894)
        #z1 = P(-0.531883, -0.907994)
        #c2 = P(-0.749653, -0.934805)
        #c3 = P(-1.31018, -0.636002)
        #z2 = P(-0.963754, -0.411282)
        #c4 = P(0.582401, 0.554976)
        #c5 = P(1.91709, -0.0790751)
        z3 = P(2.93779, -0.68398)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0464608, -0.531283)
        #z1 = z0 + P(-0.531883, -0.907994)
        #c1 = z1 + P(0.363714, 0.0381)
        #c2 = z1 + P(-0.21777, -0.0268111)
        #z2 = z1 + P(-0.431871, 0.496711)
        #c3 = z2 + P(-0.346428, -0.224719)
        #c4 = z2 + P(1.54615, 0.966258)
        #z3 = z2 + P(3.90155, -0.272697)
        #c5 = z3 + P(-1.0207, 0.604905)

        z0 = P(0, -0)
        c0 = z0 + PP(0.533311, -94)
        z1 = z0 + PP(1.05231, -120)
        c1 = z1 + PP(0.365704, 5)
        c2 = z1 + PP(0.219414, -172)
        z2 = z1 + PP(0.658205, 131)
        #z2 = z3 - PP(3.91106, ta + 28)
        c3 = z2 + PP(0.41293, -147)
        #c4 = z2 + PP(1.82325, 32)
        #z3 = z2 + PP(3.91106, -3)
        #c5 = z3 + PP(1.18648, 149)

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
    def path_CRERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERs(cls, ta=None, **kwargs):
        #M 239.38221,117.49955 C 239.25121,119.00555 238.927,120.067 237.896,120.175 237.278,120.251 235.689,119.404 236.671,118.767 241.054,116.028 247.731,116.035 247.731,119.54

        #z0 = P(0, -0)
        #c0 = P(-0.0462139, -0.531283)
        #c1 = P(-0.160588, -0.905739)
        #z1 = P(-0.524302, -0.943839)
        #c2 = P(-0.742319, -0.97065)
        #c3 = P(-1.30288, -0.671848)
        #z2 = P(-0.956455, -0.447128)
        #c4 = P(0.58977, 0.51913)
        #c5 = P(2.94527, 0.516661)
        z3 = P(2.94527, -0.719825)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0462139, -0.531283)
        #z1 = z0 + P(-0.524302, -0.943839)
        #c1 = z1 + P(0.363714, 0.0381)
        #c2 = z1 + P(-0.218017, -0.0268111)
        #z2 = z1 + P(-0.432153, 0.496711)
        #c3 = z2 + P(-0.346428, -0.224719)
        #c4 = z2 + P(1.54623, 0.966258)
        #z3 = z2 + P(3.90172, -0.272697)
        #c5 = z3 + P(0, 1.23649)

        z0 = P(0, -0)
        c0 = z0 + PP(0.53329, -94)
        z1 = z0 + PP(1.07969, -119)
        c1 = z1 + PP(0.365704, 5)
        c2 = z1 + PP(0.219659, -172)
        #z2 = z1 + PP(0.65839, 131)
        z2 = z3 - PP(3.91124, ta + 87)
        c3 = z2 + PP(0.41293, -147)
        #c4 = z2 + PP(1.82331, 32)
        #z3 = z2 + PP(3.91124, -3)
        #c5 = z3 + PP(1.23649, 90)

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
    def path_CRERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERsr(cls, ta=None, **kwargs):
        #M 202.66985,117.55238 C 202.53885,119.05838 202.25,120.067 201.219,120.175 200.601,120.251 199.012,119.404 199.995,118.767 204.377,116.028 213.2073,115.81038 211.054,119.54

        #z0 = P(0, -0)
        #c0 = P(-0.0462139, -0.531283)
        #c1 = P(-0.148114, -0.887102)
        #z1 = P(-0.511828, -0.925202)
        #c2 = P(-0.729844, -0.952013)
        #c3 = P(-1.29041, -0.65321)
        #z2 = P(-0.943628, -0.428491)
        #c4 = P(0.602245, 0.537767)
        #c5 = P(3.71738, 0.614539)
        z3 = P(2.95774, -0.701188)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0462139, -0.531283)
        #z1 = z0 + P(-0.511828, -0.925202)
        #c1 = z1 + P(0.363714, 0.0381)
        #c2 = z1 + P(-0.218017, -0.0268111)
        #z2 = z1 + P(-0.4318, 0.496711)
        #c3 = z2 + P(-0.346781, -0.224719)
        #c4 = z2 + P(1.54587, 0.966258)
        #z3 = z2 + P(3.90137, -0.272697)
        #c5 = z3 + P(0.759636, 1.31573)

        z0 = P(0, -0)
        c0 = z0 + PP(0.53329, -94)
        z1 = z0 + PP(1.05734, -118)
        c1 = z1 + PP(0.365704, 5)
        c2 = z1 + PP(0.219659, -172)
        z2 = z1 + PP(0.658159, 131)
        #z2 = z3 - PP(3.91089, ta + 118)
        c3 = z2 + PP(0.413226, -147)
        c4 = z2 + PP(1.82301, 32)
        z3 = z2 + PP(3.91089, -3)
        c5 = z3 + PP(1.51927, 59)

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
    def path_CRERse(cls, ta=None, **kwargs):
        #M 96.127396,161.80258 C 95.995596,163.30858 95.7411,164.268 94.7102,164.376 94.0928,164.452 92.5039,163.606 93.486,162.968 97.8687,160.229 106.21094,160.65836 104.545,163.741

        #z0 = P(0, -0)
        #c0 = P(-0.0464961, -0.531283)
        #c1 = P(-0.136277, -0.869745)
        #z1 = P(-0.499955, -0.907845)
        #c2 = P(-0.71776, -0.934656)
        #c3 = P(-1.27829, -0.636206)
        #z2 = P(-0.931826, -0.411134)
        #c4 = P(0.614293, 0.555124)
        #c5 = P(3.55725, 0.403655)
        z3 = P(2.96954, -0.683832)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0464961, -0.531283)
        #z1 = z0 + P(-0.499955, -0.907845)
        #c1 = z1 + P(0.363679, 0.0381)
        #c2 = z1 + P(-0.217805, -0.0268111)
        #z2 = z1 + P(-0.431871, 0.496711)
        #c3 = z2 + P(-0.346463, -0.225072)
        #c4 = z2 + P(1.54612, 0.966258)
        #z3 = z2 + P(3.90137, -0.272697)
        #c5 = z3 + P(0.587707, 1.08749)

        z0 = P(0, -0)
        c0 = z0 + PP(0.533314, -95)
        z1 = z0 + PP(1.03641, -118)
        c1 = z1 + PP(0.365669, 5)
        c2 = z1 + PP(0.219449, -172)
        z2 = z1 + PP(0.658205, 131)
        #z2 = z3 - PP(3.91089, ta + 116)
        c3 = z2 + PP(0.413151, -146)
        c4 = z2 + PP(1.82322, 32)
        z3 = z2 + PP(3.91089, -3)
        c5 = z3 + PP(1.23613, 61)

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
    def path_CRERser(cls, ta=None, **kwargs):
        #M 96.127396,161.80258 C 95.995596,163.30858 95.7411,164.268 94.7102,164.376 94.0928,164.452 92.5039,163.606 93.486,162.968 97.8687,160.229 106.21094,160.65836 104.545,163.741

        #z0 = P(0, -0)
        #c0 = P(-0.0464961, -0.531283)
        #c1 = P(-0.136277, -0.869745)
        #z1 = P(-0.499955, -0.907845)
        #c2 = P(-0.71776, -0.934656)
        #c3 = P(-1.27829, -0.636206)
        #z2 = P(-0.931826, -0.411134)
        #c4 = P(0.614293, 0.555124)
        #c5 = P(3.55725, 0.403655)
        z3 = P(2.96954, -0.683832)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0464961, -0.531283)
        #z1 = z0 + P(-0.499955, -0.907845)
        #c1 = z1 + P(0.363679, 0.0381)
        #c2 = z1 + P(-0.217805, -0.0268111)
        #z2 = z1 + P(-0.431871, 0.496711)
        #c3 = z2 + P(-0.346463, -0.225072)
        #c4 = z2 + P(1.54612, 0.966258)
        #z3 = z2 + P(3.90137, -0.272697)
        #c5 = z3 + P(0.587707, 1.08749)

        z0 = P(0, -0)
        c0 = z0 + PP(0.533314, -95)
        z1 = z0 + PP(1.03641, -118)
        c1 = z1 + PP(0.365669, 5)
        c2 = z1 + PP(0.219449, -172)
        z2 = z1 + PP(0.658205, 131)
        #z2 = z3 - PP(3.91089, ta + 116)
        c3 = z2 + PP(0.413151, -146)
        c4 = z2 + PP(1.82322, 32)
        z3 = z2 + PP(3.91089, -3)
        c5 = z3 + PP(1.23613, 61)

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
    def path_CRERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRERsw(cls, ta=None, **kwargs):
        #M 275.68702,117.82392 C 275.91165,119.28591 275.603,120.067 274.572,120.175 273.955,120.251 272.366,119.404 273.348,118.767 277.731,116.028 285.28178,116.27903 284.408,119.54

        #z0 = P(0, -0)
        #c0 = P(0.0792445, -0.515758)
        #c1 = P(-0.0296404, -0.791309)
        #z1 = P(-0.393354, -0.829409)
        #c2 = P(-0.611018, -0.85622)
        #c3 = P(-1.17158, -0.557417)
        #z2 = P(-0.825154, -0.332698)
        #c4 = P(0.721071, 0.633561)
        #c5 = P(3.38482, 0.545003)
        z3 = P(3.07657, -0.605395)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0792445, -0.515758)
        #z1 = z0 + P(-0.393354, -0.829409)
        #c1 = z1 + P(0.363714, 0.0381)
        #c2 = z1 + P(-0.217664, -0.0268111)
        #z2 = z1 + P(-0.4318, 0.496711)
        #c3 = z2 + P(-0.346428, -0.224719)
        #c4 = z2 + P(1.54622, 0.966258)
        #z3 = z2 + P(3.90172, -0.272697)
        #c5 = z3 + P(0.30825, 1.1504)

        z0 = P(0, -0)
        c0 = z0 + PP(0.52181, -81)
        z1 = z0 + PP(0.917958, -115)
        c1 = z1 + PP(0.365704, 5)
        c2 = z1 + PP(0.219309, -172)
        #z2 = z1 + PP(0.658159, 131)
        z2 = z3 - PP(3.91124, ta + 103)
        c3 = z2 + PP(0.41293, -147)
        #c4 = z2 + PP(1.82331, 32)
        #z3 = z2 + PP(3.91124, -3)
        #c5 = z3 + PP(1.19098, 74)

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
    def path_CRERswr(cls, ta=None, **kwargs):
        #M 69.4417,161.656 C 69.31,163.162 68.9649,164.268 67.934,164.376 67.3166,164.452 65.7278,163.606 66.7098,162.968 71.0926,160.229 77.125043,160.23156 77.7693,163.741

        #z0 = P(0, -0)
        #c0 = P(-0.0464608, -0.531283)
        #c1 = P(-0.168204, -0.921456)
        #z1 = P(-0.531883, -0.959556)
        #c2 = P(-0.749688, -0.986367)
        #c3 = P(-1.31018, -0.687917)
        #z2 = P(-0.963754, -0.462844)
        #c4 = P(0.582401, 0.503414)
        #c5 = P(2.71051, 0.502511)
        z3 = P(2.93779, -0.735542)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0464608, -0.531283)
        #z1 = z0 + P(-0.531883, -0.959556)
        #c1 = z1 + P(0.363679, 0.0381)
        #c2 = z1 + P(-0.217805, -0.0268111)
        #z2 = z1 + P(-0.431871, 0.496711)
        #c3 = z2 + P(-0.346428, -0.225072)
        #c4 = z2 + P(1.54615, 0.966258)
        #z3 = z2 + P(3.90155, -0.272697)
        #c5 = z3 + P(-0.22728, 1.23805)

        z0 = P(0, -0)
        c0 = z0 + PP(0.533311, -94)
        z1 = z0 + PP(1.09711, -118)
        c1 = z1 + PP(0.365669, 5)
        c2 = z1 + PP(0.219449, -172)
        #z2 = z1 + PP(0.658205, 131)
        z2 = z3 - PP(3.91106, ta + 77)
        c3 = z2 + PP(0.413122, -146)
        #c4 = z2 + PP(1.82325, 32)
        #z3 = z2 + PP(3.91106, -3)
        #c5 = z3 + PP(1.25874, 100)

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
    def path_CRERswl(cls, ta=None, **kwargs):
        pass
