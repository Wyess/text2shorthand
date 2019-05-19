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

class CharRa(WasedaChar):
    def __init__(self, name='ra', kana='ら',
                 model='SER8', head_type='SER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SER(cls, ha=-35, tn=1.2, ta=-120, d=-60, dz=P(0, 0), before=None, after=None):
        if getattr(before, 'tail_type', '') == 'NER':
                ha = 0
                tn = 1.5
                d = -60

        if after:
            if after.head_type in {'SWR', 'S', 'SR', 'SE'}:
                ta = -150
            elif after.head_type == 'SW':
                ta = after.head_angle
            elif after.head_type in {'SEL', 'NER', 'N'}:
                ta = -90
            elif before and before.tail_type == 'NER':
                ta = -90

        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn), 
            endknot(*(PP(8, d) + dz), angle=ta)])

    @classmethod
    def path_SERNE(cls):
        #M 251.447,135.009 C 257.865,139.503 266.253,148.642 262.786,154.648 263.80391,153.76737 264.77859,152.92997 265.95378,151.89208

        #z0 = P(0, -0)
        #c0 = P(2.26413, -1.58538)
        #c1 = P(5.22323, -4.80942)
        #z1 = P(4.00015, -6.9282)
        #c2 = P(4.35924, -6.61754)
        #c3 = P(4.70309, -6.32212)
        #z2 = P(5.11767, -5.95598)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.26413, -1.58538)
        #z1 = z0 + P(4.00015, -6.9282)
        #c1 = z1 + P(1.22308, 2.11878)
        #c2 = z1 + P(0.359096, 0.310667)
        #z2 = z1 + P(1.11752, 0.972227)
        #c3 = z2 + P(-0.414581, -0.366145)

        z0 = P(0, -0)
        c0 = z0 + PP(2.764, -35)
        z1 = z0 + PP(8.00007, -59)
        #z1 = z2 - PP(1.48124, ta + 359)
        c1 = z1 + PP(2.44646, 60)
        c2 = z1 + PP(0.47483, 40)
        z2 = z1 + PP(1.48124, 41)
        c3 = z2 + PP(0.553118, -138)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_nerSERNE(cls):
        #M 58.68,258.214 C 64.2342,258.214 70.0186,271.452 70.0186,277.853 70.823361,276.73468 71.61724,276.04912 72.947601,275.41269

        #z0 = P(0, -0)
        #c0 = P(1.9594, -0)
        #c1 = P(4.00001, -4.67007)
        #z1 = P(4.00001, -6.9282)
        #c2 = P(4.28391, -6.53368)
        #c3 = P(4.56397, -6.29183)
        #z2 = P(5.03329, -6.06732)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.9594, 0)
        #z1 = z0 + P(4.00001, -6.9282)
        #c1 = z1 + P(0, 2.25813)
        #c2 = z1 + P(0.283902, 0.394518)
        #z2 = z1 + P(1.03329, 0.860887)
        #c3 = z2 + P(-0.469322, -0.224518)

        z0 = P(0, -0)
        c0 = z0 + PP(1.9594, 0)
        z1 = z0 + PP(8, -59)
        #z1 = z2 - PP(1.34492, ta + 373)
        c1 = z1 + PP(2.25813, 90)
        c2 = z1 + PP(0.48605, 54)
        z2 = z1 + PP(1.34492, 39)
        c3 = z2 + PP(0.520261, -154)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def get_paths(self):
        return [self.path_SER(before=self.before, after=self.after)]

class CharRan(CharRa):
    def __init__(self, name='ran', kana='らん',
                 model='SER8NE1F', head_type='SER', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type') == 'NER':
            return [self.path_nerSERNE()]
        else:
            return [self.path_SERNE()]

class CharRoi(CharRa):
    def __init__(self, name='roi', kana='ろい',
                 model='SER8', head_type='SER', tail_type='SERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharRai(CharRa):
    def __init__(self, name='rai', kana='らい',
                 model='SER4', head_type='SER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)
    
    def get_paths(self):
        return [p.transformed(pyx.trafo.scale(0.5)) for p in super().get_paths()]

class CharReki(WasedaChar):
    def __init__(self, name='reki', kana='れき',
                 model='SER8NWR4', head_type='SER', tail_type='NWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'NER'}
        self.tail_ligature = {'SER'}

    def get_paths(self, **kwargs):
        if getattr(self.after, 'head_type', '') in {'SER', 'E', 'ER', 'NEL', 'NER', 'NE'}: 
            return super().get_paths(me='SERCNWR')
        else:
            return super().get_paths(me='SERNWR')

    @classmethod
    def path_SERNWR(cls, ta=None, **kwargs):
        #M 47.3414,58.6772 C 53.454292,62.290552 62.890598,76.386098 56.3188,79.8304 53.528559,81.292775 49.879,78.5551 48.3927,74.6832

        #z0 = P(0, -0)
        #c0 = P(2.15649, -1.27471)
        #c1 = P(5.48541, -6.24731)
        #z1 = P(3.16703, -7.46238)
        #c2 = P(2.18269, -7.97827)
        #c3 = P(0.895209, -7.01248)
        z2 = P(0.370875, -5.64656)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.15649, -1.27471)
        #z1 = z0 + P(3.16703, -7.46238)
        #c1 = z1 + P(2.31838, 1.21507)
        #c2 = z1 + P(-0.984335, -0.515893)
        #z2 = z1 + P(-2.79615, 1.81582)
        #c3 = z2 + P(0.524334, -1.36592)

        z0 = P(0, -0)
        c0 = z0 + PP(2.50506, -30)
        z1 = z0 + PP(8.10661, -67)
        #z1 = z2 - PP(3.33402, ta + 395)
        c1 = z1 + PP(2.6175, 27)
        c2 = z1 + PP(1.11133, -152)
        z2 = z1 + PP(3.33402, 147)
        c3 = z2 + PP(1.4631, -68)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_SERNWRe(cls, ta=None, **kwargs):
        pass
    
    @classmethod
    def path_SERNWRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERNWRel(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERNWRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERNWRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERNWRs(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRsl(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRsr(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRse(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRser(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRsel(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRsw(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRswr(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERNWRswl(cls, ta=None, **kwargs):
        return cls.path_SERNWR()

    @classmethod
    def path_SERCNWR(cls, ta=None, **kwargs):
        #M 88.0806,131.376 C 94.235121,134.99505 103.63159,149.08445 97.058,152.529 94.267638,153.99114 89.9233,151.453 89.1319,147.382 88.5399,144.024 92.2461,147.729 93.3805,148.681 94.6485,149.708 96.1552,151.154 97.2625,152.301

        #z0 = P(0, -0)
        #c0 = P(2.17118, -1.27672)
        #c1 = P(5.48604, -6.24715)
        #z1 = P(3.16703, -7.46231)
        #c2 = P(2.18265, -7.97812)
        #c3 = P(0.650064, -7.08272)
        #z2 = P(0.370875, -5.64656)
        #c4 = P(0.162031, -4.46193)
        #c5 = P(1.4695, -5.76898)
        #z3 = P(1.86969, -6.10482)
        #c6 = P(2.31701, -6.46712)
        #c7 = P(2.84854, -6.97724)
        z4 = P(3.23917, -7.38187)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.17118, -1.27672)
        #z1 = z0 + P(3.16703, -7.46231)
        #c1 = z1 + P(2.31902, 1.21516)
        #c2 = z1 + P(-0.984378, -0.515811)
        #z2 = z1 + P(-2.79615, 1.81575)
        #c3 = z2 + P(0.279188, -1.43616)
        #c4 = z2 + P(-0.208844, 1.18463)
        #z3 = z2 + P(1.49881, -0.458258)
        #c5 = z3 + P(-0.400191, 0.335844)
        #c6 = z3 + P(0.447322, -0.362303)
        #z4 = z3 + P(1.36948, -1.27706)
        #c7 = z4 + P(-0.390631, 0.404636)

        z0 = P(0, -0)
        c0 = z0 + PP(2.51874, -30)
        z1 = z0 + PP(8.10655, -67)
        c1 = z1 + PP(2.6181, 27)
        c2 = z1 + PP(1.11133, -152)
        z2 = z1 + PP(3.33398, 147)
        c3 = z2 + PP(1.46304, -78)
        c4 = z2 + PP(1.2029, 99)
        z3 = z2 + PP(1.5673, -17)
        #z3 = z4 - PP(1.87253, ta + 5)
        c5 = z3 + PP(0.522441, 139)
        c6 = z3 + PP(0.575639, -39)
        z4 = z3 + PP(1.87253, -42)
        c7 = z4 + PP(0.562426, 133)

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
    def path_SERCNWRe(cls, ta=None, **kwargs):
        return cls.path_SERCNWR()

    @classmethod
    def path_SERCNWRer(cls, ta=None, **kwargs):
        return cls.path_SERCNWR()

    @classmethod
    def path_SERCNWRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRne(cls, ta=None, **kwargs):
        return cls.path_SERCNWR()

    @classmethod
    def path_SERCNWRner(cls, ta=None, **kwargs):
        return cls.path_SERCNWR()

    @classmethod
    def path_SERCNWRnel(cls, ta=None, **kwargs):
        return cls.path_SERCNWR()

    @classmethod
    def path_SERCNWRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRser(cls, ta=None, **kwargs):
        #M 92.3666,221.445 C 98.5498,225.015 107.94027,239.19442 101.345,242.598 98.545768,244.04258 93.616215,243.59789 92.754015,239.54189 92.220615,236.17389 95.777016,238.55442 97.097656,239.2252 98.367415,239.87014 100.36386,241.3094 101.612,242.301

        #z0 = P(0, -0)
        #c0 = P(2.1813, -1.25942)
        #c1 = P(5.49404, -6.2616)
        #z1 = P(3.16738, -7.46231)
        #c2 = P(2.17987, -7.97192)
        #c3 = P(0.440836, -7.81505)
        #z2 = P(0.136671, -6.38418)
        #c4 = P(-0.0515003, -5.19603)
        #c5 = P(1.20312, -6.03582)
        #z3 = P(1.66901, -6.27246)
        #c6 = P(2.11695, -6.49998)
        #c7 = P(2.82126, -7.00772)
        z4 = P(3.26157, -7.35753)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.1813, -1.25942)
        #z1 = z0 + P(3.16738, -7.46231)
        #c1 = z1 + P(2.32666, 1.20071)
        #c2 = z1 + P(-0.987507, -0.509616)
        #z2 = z1 + P(-3.03071, 1.07813)
        #c3 = z2 + P(0.304165, -1.43087)
        #c4 = z2 + P(-0.188172, 1.18816)
        #z3 = z2 + P(1.53234, 0.111721)
        #c5 = z3 + P(-0.465892, 0.236636)
        #c6 = z3 + P(0.447943, -0.22752)
        #z4 = z3 + P(1.59256, -1.08507)
        #c7 = z4 + P(-0.440316, 0.349814)

        z0 = P(0, -0)
        c0 = z0 + PP(2.51877, -30)
        z1 = z0 + PP(8.10669, -67)
        c1 = z1 + PP(2.61822, 27)
        c2 = z1 + PP(1.11125, -152)
        z2 = z1 + PP(3.21676, 160)
        c3 = z2 + PP(1.46284, -77)
        c4 = z2 + PP(1.20296, 98)
        #z3 = z2 + PP(1.53641, 4)
        z3 = z4 - PP(1.92708, ta + 5)
        c5 = z3 + PP(0.522544, 153)
        #c6 = z3 + PP(0.502412, -26)
        #z4 = z3 + PP(1.92708, -34)
        #c7 = z4 + PP(0.56236, 141)

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
    def path_SERCNWRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCNWRswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSERCNWRser(cls, ta=None, **kwargs):
        #M 92.3666,221.445 C 99.506408,221.445 107.94027,239.19442 101.345,242.598 98.545768,244.04258 93.616215,243.59789 92.754015,239.54189 92.220615,236.17389 95.777016,238.55442 97.097656,239.2252 98.367415,239.87014 100.36386,241.3094 101.612,242.301

        #z0 = P(0, -0)
        #c0 = P(2.51877, -0)
        #c1 = P(5.49404, -6.2616)
        #z1 = P(3.16738, -7.46231)
        #c2 = P(2.17987, -7.97192)
        #c3 = P(0.440836, -7.81505)
        #z2 = P(0.136671, -6.38418)
        #c4 = P(-0.0515003, -5.19603)
        #c5 = P(1.20312, -6.03582)
        #z3 = P(1.66901, -6.27246)
        #c6 = P(2.11695, -6.49998)
        #c7 = P(2.82126, -7.00772)
        z4 = P(3.26157, -7.35753)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.51877, 0)
        #z1 = z0 + P(3.16738, -7.46231)
        #c1 = z1 + P(2.32666, 1.20071)
        #c2 = z1 + P(-0.987507, -0.509616)
        #z2 = z1 + P(-3.03071, 1.07813)
        #c3 = z2 + P(0.304165, -1.43087)
        #c4 = z2 + P(-0.188172, 1.18816)
        #z3 = z2 + P(1.53234, 0.111721)
        #c5 = z3 + P(-0.465892, 0.236636)
        #c6 = z3 + P(0.447943, -0.22752)
        #z4 = z3 + P(1.59256, -1.08507)
        #c7 = z4 + P(-0.440316, 0.349814)

        z0 = P(0, -0)
        c0 = z0 + PP(2.51877, 0)
        z1 = z0 + PP(8.10669, -67)
        c1 = z1 + PP(2.61822, 27)
        c2 = z1 + PP(1.11125, -152)
        z2 = z1 + PP(3.21676, 160)
        c3 = z2 + PP(1.46284, -77)
        c4 = z2 + PP(1.20296, 98)
        #z3 = z2 + PP(1.53641, 4)
        z3 = z4 - PP(1.92708, ta + 5)
        c5 = z3 + PP(0.522544, 153)
        #c6 = z3 + PP(0.502412, -26)
        #z4 = z3 + PP(1.92708, -34)
        #c7 = z4 + PP(0.56236, 141)

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
    def path_nerSERNWR(cls, ta=None, **kwargs):
        #M 388.341,316.921 C 395.48028,316.921 403.8925,334.62918 397.319,338.075 394.52839,339.53783 390.879,336.799 389.393,332.927

        #z0 = P(0, -0)
        #c0 = P(2.51858, -0)
        #c1 = P(5.48622, -6.24705)
        #z1 = P(3.16724, -7.46266)
        #c2 = P(2.18277, -7.97872)
        #c3 = P(0.89535, -7.01252)
        z2 = P(0.371122, -5.64656)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.51858, 0)
        #z1 = z0 + P(3.16724, -7.46266)
        #c1 = z1 + P(2.31898, 1.21561)
        #c2 = z1 + P(-0.984465, -0.516054)
        #z2 = z1 + P(-2.79612, 1.8161)
        #c3 = z2 + P(0.524228, -1.36596)

        z0 = P(0, -0)
        c0 = z0 + PP(2.51858, 0)
        z1 = z0 + PP(8.10695, -67)
        #z1 = z2 - PP(3.33414, ta + 395)
        c1 = z1 + PP(2.61828, 27)
        c2 = z1 + PP(1.11152, -152)
        z2 = z1 + PP(3.33414, 146)
        c3 = z2 + PP(1.4631, -69)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_nerSERCNWR(cls, ta=None, **kwargs):
        #M 173.337,316.921 C 178.01547,316.921 181.906,323.283 183.367,328.061 184.404,331.253 185.356,336.656 182.314,338.075 179.483,339.456 175.179,336.999 174.388,332.927 173.796,329.57 177.502,333.274 178.637,334.226 179.905,335.253 181.411,336.7 182.519,337.846

        #z0 = P(0, -0)
        #c0 = P(1.65046, -0)
        #c1 = P(3.02295, -2.24437)
        #z1 = P(3.53836, -3.92994)
        #c2 = P(3.90419, -5.05601)
        #c3 = P(4.24004, -6.96207)
        #z2 = P(3.16689, -7.46266)
        #c4 = P(2.16817, -7.94985)
        #c5 = P(0.649817, -7.08307)
        #z3 = P(0.370769, -5.64656)
        #c6 = P(0.161925, -4.46229)
        #c7 = P(1.46932, -5.76898)
        #z4 = P(1.86972, -6.10482)
        #c8 = P(2.31704, -6.46712)
        #c9 = P(2.84833, -6.97759)
        z5 = P(3.23921, -7.38188)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.65046, 0)
        #z1 = z0 + P(3.53836, -3.92994)
        #c1 = z1 + P(-0.515408, 1.68557)
        #c2 = z1 + P(0.365831, -1.12607)
        #z2 = z1 + P(-0.371475, -3.53272)
        #c3 = z2 + P(1.07315, 0.500592)
        #c4 = z2 + P(-0.998714, -0.487186)
        #z3 = z2 + P(-2.79612, 1.8161)
        #c5 = z3 + P(0.279047, -1.43651)
        #c6 = z3 + P(-0.208844, 1.18428)
        #z4 = z3 + P(1.49895, -0.458258)
        #c7 = z4 + P(-0.400403, 0.335844)
        #c8 = z4 + P(0.447322, -0.362303)
        #z5 = z4 + P(1.36948, -1.27706)
        #c9 = z5 + P(-0.390878, 0.404283)

        z0 = P(0, -0)
        c0 = z0 + PP(1.65046, 0)
        z1 = z0 + PP(5.28814, -48)
        c1 = z1 + PP(1.76261, 107)
        c2 = z1 + PP(1.184, -72)
        z2 = z1 + PP(3.55219, -96)
        c3 = z2 + PP(1.18416, 25)
        c4 = z2 + PP(1.11121, -153)
        z3 = z2 + PP(3.33414, 146)
        c5 = z3 + PP(1.46336, -79)
        c6 = z3 + PP(1.20255, 100)
        z4 = z3 + PP(1.56744, -16)
        #z4 = z5 - PP(1.87253, ta + 4)
        c7 = z4 + PP(0.522603, 140)
        c8 = z4 + PP(0.575639, -39)
        z5 = z4 + PP(1.87253, -42)
        c9 = z5 + PP(0.562344, 134)

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
            #curve(),
            endknot(*z5)])

class CharRaku(CharRa):
    def __init__(self, name='raku', kana='らく',
                 model='BSER8', head_type='BSER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharRatsu(CharRa):
    def __init__(self, name='ratsu', kana='らつ',
                 model='CR1SER8', head_type='CR1SER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()

class CharKara(CharRa):
    def __init__(self, name='kara', kana='から',
                 model='SER4F', head_type='SER', tail_type='SERF'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SER(self, ta=None, **kwargs):
        #M 8206.8062 4.959407 C 8210.0162 7.2061154 8214.2112 11.776045 8212.4762 14.778895
        return [p.transformed(pyx.trafo.trafo().translated(-8206.8062, -4.959407).scaled(25.4 / 72, -25.4 / 72)) for p in [
            pyx.path.path(pyx.path.moveto(8206.8062, 4.959407),
            pyx.path.curveto(8210.0162, 7.2061154, 8214.2112, 11.776045, 8212.4762, 14.778895))]]

    def get_paths(self):
        return self.path_SER()
