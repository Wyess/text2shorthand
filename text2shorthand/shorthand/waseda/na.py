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
    curve,
    path)

class CharNa(WasedaChar):
    def __init__(self, name='na', kana='な', model='EL8', head_type='EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'SEL', 'XNE', 'ER', 'SW', 'SWL', 'E', 'SE', 'NEL', 'SWR', 'NE'}
        
    @classmethod
    def path_template(cls, ta=80, tn=1.7):
        return path([beginknot(0, 0, angle=-18), tensioncurve(tn), endknot(8, 0, angle=ta)])

    @classmethod
    def path_fusion(cls, ta=80, tn=1.0):
        return cls.path_template(ta, tn)

    @classmethod
    def path_tan(cls, ta=80):
        return cls.path_template(ta+180)

    @classmethod
    def path_flat(cls):
        return cls.path_template(ta=60)

    @classmethod
    def path_up(cls):
        return cls.path_template(ta=90)

    @classmethod
    def path_EL(cls, ta=None, **kwargs):
        return cls.path_template()

    @classmethod
    def path_ELsel(cls, ta=None, **kwargs):
        return cls.path_flat()

    @classmethod
    def path_ELxne(cls, ta=None, **kwargs):
        return cls.path_flat()

    @classmethod
    def path_ELer(cls, ta=None, **kwargs):
        return cls.path_fusion(ta)

    @classmethod
    def path_ELsw(cls, ta=None, **kwargs):
        return cls.path_tan(ta)

    @classmethod
    def path_ELswl(cls, ta=None, **kwargs):
        return cls.path_tan(ta)

    @classmethod
    def path_ELe(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELse(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELnel(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELswr(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELne(cls, ta=None, **kwargs):
        return cls.path_up()

class CharNan(CharNa):
    def __init__(self, name='nan', kana='なん', model='EL8F', head_type='EL', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharNani(CharNan):
    def __init__(self):
        super().__init__(name='nani', kana='なに')

class CharNai(WasedaChar):
    def __init__(self, name='nai', kana='ない',
        model='USL4', head_type='SEL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_USL(cls, ta=None, **kwargs):
        return pyx.path.path(
        pyx.path.moveto(153.30702, 251.64711),
        pyx.path.curveto(153.30702, 256.21851, 155.72034, 260.09813, 158.69268, 260.08697),
        pyx.path.curveto(161.82948, 260.07518, 164.59389, 256.32137, 164.59389, 251.64711)).transformed(pyx.trafo.trafo().translated(-153.30702, -251.64711).scaled(25.4 / 72, -25.4 / 72))

    @classmethod
    def path_USLe(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLer(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLel(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLne(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLner(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLnel(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLs(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLsl(cls, ta=None, **kwargs):
        return cls.path_USLsw(ta=ta, **kwargs)

    @classmethod
    def path_USLsr(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLse(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLser(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLsel(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLsw(cls, ta=None, **kwargs):
        #M 47.3414,189.435 C 47.3414,194.006 49.7547,197.886 52.7271,197.875 55.8639,197.863 58.189139,193.96261 59.848192,189.53259

        #z0 = P(0, -0)
        #c0 = P(0, -1.61255)
        #c1 = P(0.851359, -2.98132)
        #z1 = P(1.89996, -2.97744)
        #c2 = P(3.00655, -2.97321)
        #c3 = P(3.82684, -1.59724)
        z2 = P(4.41212, -0.0344276)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -1.61255)
        #z1 = z0 + P(1.89996, -2.97744)
        #c1 = z1 + P(-1.0486, -0.00388056)
        #c2 = z1 + P(1.10659, 0.00423333)
        #z2 = z1 + P(2.51216, 2.94302)
        #c3 = z2 + P(-0.585277, -1.56281)

        z0 = P(0, -0)
        c0 = z0 + PP(1.61255, -90)
        z1 = z0 + PP(3.532, -57)
        #z1 = z2 - PP(3.86941, ta + 339)
        c1 = z1 + PP(1.0486, -179)
        #c2 = z1 + PP(1.1066, 0)
        #z2 = z1 + PP(3.86941, 49)
        #c3 = z2 + PP(1.66881, -110)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta+180)])

    @classmethod
    def path_USLswr(cls, ta=None, **kwargs):
        return cls.path_USL()

    @classmethod
    def path_USLswl(cls, ta=None, **kwargs):
        return cls.path_USLsw(ta=ta, **kwargs)

class CharNaikaku(CharNai):
    def __init__(self, name='naikaku', kana='ないかく',
        model='USL4P', head_type='SEL', tail_type='P'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [pyx.path.path(
        pyx.path.moveto(47.614146, 58.695383),
        pyx.path.curveto(47.614146, 63.266783, 50.027446, 67.146383, 52.999846, 67.135183),
        pyx.path.curveto(56.136646, 67.123383, 58.901046, 63.369583, 58.901046, 58.695383),
        pyx.path.moveto(53.0679, 70.20477),
        pyx.path.lineto(53.100343, 70.24372)).transformed(pyx.trafo.trafo().translated(-47.614146, -58.695383).scaled(25.4 / 72, -25.4 / 72))]

class CharNaku(CharNa):
    def __init__(self, name='naku', kana='なく', model='BEL8', head_type='BEL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharNatsu(CharNa):
    def __init__(self, name='natsu', kana='なつ', model='CL1EL8', head_type='CL1EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'ER', 'NEL', 'NE', 'SE'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()

    @classmethod
    def path_CLEL_fusion(cls, ta=None, **kwargs):
        #M 51.203993,59.690008 C 51.036726,58.000756 50.850768,57.244589 49.768021,56.901977 48.08098,56.368149 45.926543,58.177645 48.928013,59.130518 54.725257,60.970962 69.1064,63.8503 70.0186,58.6772

        #z0 = P(0, -0)
        #c0 = P(-0.0590081, 0.595931)
        #c1 = P(-0.12461, 0.862689)
        #z1 = P(-0.506579, 0.983555)
        #c2 = P(-1.10173, 1.17188)
        #c3 = P(-1.86177, 0.533528)
        #z2 = P(-0.802915, 0.197376)
        #c4 = P(1.24222, -0.451892)
        #c5 = P(6.31557, -1.46766)
        z3 = P(6.63738, 0.357296)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0590081, 0.595931)
        #z1 = z0 + P(-0.506579, 0.983555)
        #c1 = z1 + P(0.381969, -0.120866)
        #c2 = z1 + P(-0.595151, 0.188323)
        #z2 = z1 + P(-0.296336, -0.78618)
        #c3 = z2 + P(-1.05885, 0.336152)
        #c4 = z2 + P(2.04514, -0.649268)
        #z3 = z2 + P(7.44029, 0.159921)
        #c5 = z3 + P(-0.321804, -1.82495)

        z0 = P(0, -0)
        c0 = z0 + PP(0.598845, 95)
        z1 = z0 + PP(1.10635, 117)
        c1 = z1 + PP(0.400636, -17)
        c2 = z1 + PP(0.624235, 162)
        z2 = z1 + PP(0.840175, -110)
        #z2 = z3 - PP(7.44201, ta + 281)
        c3 = z2 + PP(1.11093, 162)
        c4 = z2 + PP(2.14573, -17)
        z3 = z2 + PP(7.44201, 1)
        c5 = z3 + PP(1.85311, -100)

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
    def path_CLEL(cls, ta=None, **kwargs):
        #M 51.203993,59.690008 C 51.036726,58.000756 50.850768,57.244589 49.768021,56.901977 48.08098,56.368149 45.926543,58.177645 48.928013,59.130518 54.725257,60.970962 69.1064,63.8503 70.0186,58.6772

        #z0 = P(0, -0)
        #c0 = P(-0.0590081, 0.595931)
        #c1 = P(-0.12461, 0.862689)
        #z1 = P(-0.506579, 0.983555)
        #c2 = P(-1.10173, 1.17188)
        #c3 = P(-1.86177, 0.533528)
        #z2 = P(-0.802915, 0.197376)
        #c4 = P(1.24222, -0.451892)
        #c5 = P(6.31557, -1.46766)
        z3 = P(6.63738, 0.357296)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0590081, 0.595931)
        #z1 = z0 + P(-0.506579, 0.983555)
        #c1 = z1 + P(0.381969, -0.120866)
        #c2 = z1 + P(-0.595151, 0.188323)
        #z2 = z1 + P(-0.296336, -0.78618)
        #c3 = z2 + P(-1.05885, 0.336152)
        #c4 = z2 + P(2.04514, -0.649268)
        #z3 = z2 + P(7.44029, 0.159921)
        #c5 = z3 + P(-0.321804, -1.82495)

        z0 = P(0, -0)
        c0 = z0 + PP(0.598845, 95)
        z1 = z0 + PP(1.10635, 117)
        c1 = z1 + PP(0.400636, -17)
        c2 = z1 + PP(0.624235, 162)
        z2 = z1 + PP(0.840175, -110)
        #z2 = z3 - PP(7.44201, ta + 281)
        c3 = z2 + PP(1.11093, 162)
        c4 = z2 + PP(2.14573, -17)
        z3 = z2 + PP(7.44201, 1)
        c5 = z3 + PP(1.85311, -100)

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
    def path_CLEL_acute(cls, ta=None, **kwawrgs):
        #M 419.24,114.446 C 419.092,112.755 418.903,111.983 417.817,111.651 416.134,111.104 414.007,112.916 417.002,113.889 422.819,115.668 439.45352,118.59479 438.094,113.521

        #z0 = P(0, -0)
        #c0 = P(-0.0522111, 0.596547)
        #c1 = P(-0.118886, 0.868892)
        #z1 = P(-0.502003, 0.986014)
        #c2 = P(-1.09573, 1.17898)
        #c3 = P(-1.84609, 0.53975)
        #z2 = P(-0.789517, 0.196497)
        #c4 = P(1.26259, -0.431094)
        #c5 = P(7.13088, -1.4636)
        z3 = P(6.65127, 0.326319)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0522111, 0.596547)
        #z1 = z0 + P(-0.502003, 0.986014)
        #c1 = z1 + P(0.383117, -0.117122)
        #c2 = z1 + P(-0.593725, 0.192969)
        #z2 = z1 + P(-0.287514, -0.789517)
        #c3 = z2 + P(-1.05657, 0.343253)
        #c4 = z2 + P(2.05211, -0.627592)
        #z3 = z2 + P(7.44079, 0.129822)
        #c5 = z3 + P(0.479608, -1.78992)

        z0 = P(0, -0)
        c0 = z0 + PP(0.598828, 95)
        z1 = z0 + PP(1.10645, 116)
        c1 = z1 + PP(0.40062, -16)
        c2 = z1 + PP(0.624297, 161)
        z2 = z1 + PP(0.840239, -110)
        #z2 = z3 - PP(7.44192, ta + 254)
        c3 = z2 + PP(1.11093, 162)
        c4 = z2 + PP(2.14593, -17)
        z3 = z2 + PP(7.44192, 0)
        c5 = z3 + PP(1.85306, -74)

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
    def path_CLELe(cls, ta=None, **kwargs):
        return cls.path_CLEL_acute()

    @classmethod
    def path_CLELer(cls, ta=None, **kwargs):
        return cls.path_CLEL_fusion(ta=ta)

    @classmethod
    def path_CLELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELne(cls, ta=None, **kwargs):
        return cls.path_CLEL_acute()

    @classmethod
    def path_CLELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELnel(cls, ta=None, **kwargs):
        return cls.path_CLEL_acute()

    @classmethod
    def path_CLELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELse(cls, ta=None, **kwargs):
        return cls.path_CLEL_acute()

    @classmethod
    def path_CLELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLELswl(cls, ta=None, **kwargs):
        pass
