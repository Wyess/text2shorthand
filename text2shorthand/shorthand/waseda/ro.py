from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    endknot,
    knot,
    controlcurve,
    smoothknot,
    tensioncurve,
    path)

class CharRo(WasedaChar):
    def __init__(self, name='ro', kana='ろ',
                 model='SER16', head_type='SER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SER(cls, ha=-30, tn=1.5, ta=-140, d=-60, dz=P(0, 0), before=None, after=None):
        if before:
            if before.tail_type == 'NER':
                ha = 0
                tn = 1.5
                d = -60

        if after:
            if after.head_type in {'SWR', 'S', 'SR', 'SE'}:
                ta = 160
            elif after.head_type == 'SW':
                ta = after.head_angle
            elif after.head_type in {'NER'}:
                ta = -120
            elif after.head_type in {'SEL', 'N'}:
                ta = -90
            elif before and before.tail_type == 'NER':
                ta = -90

        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn), 
            endknot(*(PP(16, d) + dz), angle=ta)])

    @classmethod
    def path_SERNE(cls, ta=None, **kwargs):
        #M 296.802,154.648 C 309.933,162.229 328.018,186.761 319.479,193.926 320.55724,193.01494 321.62645,192.19505 323.14639,191.29498

        #z0 = P(0, -0)
        #c0 = P(4.63232, -2.67441)
        #c1 = P(11.0123, -11.3288)
        #z1 = P(7.99994, -13.8564)
        #c2 = P(8.38032, -13.535)
        #c3 = P(8.75751, -13.2458)
        z2 = P(9.29372, -12.9282)

        #z0 = P(0, -0)
        #c0 = z0 + P(4.63232, -2.67441)
        #z1 = z0 + P(7.99994, -13.8564)
        #c1 = z1 + P(3.01237, 2.52765)
        #c2 = z1 + P(0.380379, 0.321402)
        #z2 = z1 + P(1.29377, 0.928165)
        #c3 = z2 + P(-0.536201, -0.317525)

        z0 = P(0, -0)
        c0 = z0 + PP(5.34892, -29)
        z1 = z0 + PP(16, -60)
        #z1 = z2 - PP(1.59228, ta + 364)
        c1 = z1 + PP(3.93235, 39)
        c2 = z1 + PP(0.497983, 40)
        z2 = z1 + PP(1.59228, 35)
        c3 = z2 + PP(0.623164, -149)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_nerSERNE(cls, ta=None, **kwargs):
        #M 58.68,317.131 C 69.7884,317.131 81.3572,343.607 81.3572,356.409 82.119975,355.61526 82.933333,354.82152 84.025366,354.02778

        #z0 = P(0, -0)
        #c0 = P(3.9188, -0)
        #c1 = P(8.00001, -9.34014)
        #z1 = P(8.00001, -13.8564)
        #c2 = P(8.2691, -13.5764)
        #c3 = P(8.55604, -13.2964)
        #z2 = P(8.94128, -13.0164)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.9188, 0)
        #z1 = z0 + P(8.00001, -13.8564)
        #c1 = z1 + P(0, 4.51626)
        #c2 = z1 + P(0.26909, 0.280014)
        #z2 = z1 + P(0.94127, 0.840041)
        #c3 = z2 + P(-0.385245, -0.280014)

        z0 = P(0, -0)
        c0 = z0 + PP(3.9188, 0)
        z1 = z0 + PP(16, -59)
        #z1 = z2 - PP(1.26161, ta + 364)
        c1 = z1 + PP(4.51626, 90)
        c2 = z1 + PP(0.388352, 46)
        z2 = z1 + PP(1.26161, 41)
        c3 = z2 + PP(0.476258, -143)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def get_paths(self):
        return [self.path_SER(before=self.before, after=self.after)]

class CharRon(CharRo):
    def __init__(self, name='ron', kana='ろん',
                 model='SER8NE1F', head_type='SER', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type') == 'NER':
            return [self.path_nerSERNE()]
        else:
            return [self.path_SERNE()]

class CharRotsu(CharRo):
    def __init__(self, name='rotsu', kana='ろつ',
                 model='CR1SER8', head_type='CR1SER', tail_type='SER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()
