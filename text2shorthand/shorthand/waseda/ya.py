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


class CharYa(WasedaChar):
    def __init__(self, name='ya', kana='や',
                 model='NER8', head_type='NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_pos_huu(self):
        return super().get_pos_huu() + P(1, 0)

    def get_pos_you(self):
        return super().get_pos_you() + P(0, 1)

    def get_pos_x_kitsuon(self):
        if self.paths:
            return P(*self.paths[0].at(5))
        else:
            return P(0, 0)

    @classmethod
    def path_NER(cls, ha=70, tn=1.1, ta=0, d=40, dz=P(0, 0),
                 before=None, after=None):
        if before:
            if before.tail_type == 'SWR':
                ha = 55
                d = 40
            elif before.tail_type in {'NW|SWCR1', 'NEROR4'}:
                ha = 40
                d = 30
            elif before.tail_type == 'SW':
                ha = before.tail_angle + 170
                d = 36
            elif before.tail_type == 'SR':
                ha = 50
                d = 30
                dz = P(1, 0)
            elif before.tail_type in {
                'SRCR1', 'SWLCL1', 'SWLCL4', 'SWLCL8', 'SWCR1', 'SWCL1',
                'SERCR1', 'CNL', 'CNR', 'SWRCL1'}:
                ha = 45
                d = 30
                dz = P(1, 0)
            elif before.tail_type in {'SWRCR1'}:
                ha = 35
                d = 25
                dz = P(1, 0)
            else:
                ha = 70
                d = 40

        if after:
            if after.head_type in {'E', 'ER', 'NE', 'NER', 'SE', 'BE', 'BER'}:
                tn = 1.1
                ta = -70
                d = 35
            elif after.head_type in {'S', 'SR'}:
            #elif after.head_type in {'S', 'SW', 'SR'}:
            #elif after.head_type in {'S', 'SW', 'SWR', 'SR'}:
                ta = after.head_angle
            elif after.head_type == 'SER':
                ha = 90
                d = 60
                tn = 1.5
                ta = 0
            #elif after.head_type in {'SWR', 'NEL|SWR'}:
            elif after.head_type in {'NEL|SWR', 'SWR', 'SWR|NEL'}:
                tn = 1.5
                ta = -40
            else:
                tn = 1.1
                ta = 0

        return mpath([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn), 
            endknot(*(PP(8, d) + dz), angle=ta)])

    def get_paths(self):
        return [self.path_NER(before=self.before, after=self.after)]

    def get_pos_xtsu(self):
        if self.paths:
            return P(*self.paths[0].at(2.0))
        else:
            return P(0, 0)

class CharYan(CharYa):
    def __init__(self, name='yan', kana='やん',
                 model='NER8F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_NER(before=self.before, after=None)]

class CharYaku(CharYan):
    def __init__(self, name='yaku', kana='やく',
                 model='NER8F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharYara(CharYan):
    def __init__(self, name='yara', kana='やら',
                 model='NER8F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharYari(CharYan):
    def __init__(self, name='yari', kana='やり',
                 model='NER8F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharYai(CharYa):
    def __init__(self, name='yai', kana='やい',
                 model='NER4', head_type='NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [p.transformed(pyx.trafo.scale(0.5)) for p in super().get_paths()]

class CharYaku(CharYa):
    def __init__(self, name='yaku', kana='やく',
                 model='BNER8', head_type='BNER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharYatsu(CharYa):
    def __init__(self, name='yatsu', kana='やつ',
                 model='CR1NER8', head_type='CR1NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()

class CharToiu(WasedaChar):
    def __init__(self, name='toiu', kana='という',
                 model='SW4NER8', head_type='SW|NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_pos_x_kitsuon(self):
        if self.paths:
            return P(*self.paths[-1].at(6))
        else:
            return P(0, 0)
    def get_pos_you(self):
        return super().get_pos_you() + P(0, 1)

    def get_pos_huu(self):
        return super().get_pos_huu() + P(1, 1)

    def get_paths(self):
        if self.before.kana[-1] in {'と', 'ど', 'た', 'だ'}:
            return self.path_NER()
        elif self.before.kana in {'たい'}:
            return self.path_NER()
        else:
            return super(WasedaChar, self).get_paths(e='SWNER')

    @classmethod
    def path_SWNER(self, ta=None, **kwargs):
        #M 1013.36,-4.80571 C 1011.7633,-1.255503 1010.1667,2.1362823 1008.57,5.47059 1012.8,-0.569615 1019.65,-7.85871 1026.92,-7.85871

        #z0 = P(0, -0)
        #c0 = P(-0.56328, -1.25243)
        #c1 = P(-1.12653, -2.44898)
        #z1 = P(-1.68981, -3.62525)
        #c2 = P(-0.197556, -1.4944)
        #c3 = P(2.21897, 1.07703)
        z2 = P(4.78367, 1.07703)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.56328, -1.25243)
        #z1 = z0 + P(-1.68981, -3.62525)
        #c1 = z1 + P(0.56328, 1.17627)
        #c2 = z1 + P(1.49225, 2.13085)
        #z2 = z1 + P(6.47347, 4.70228)
        #c3 = z2 + P(-2.56469, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(1.37327, -114)
        z1 = z0 + PP(3.99974, -114)
        #z1 = z2 - PP(8.00108, ta + 35)
        c1 = z1 + PP(1.30418, 64)
        c2 = z1 + PP(2.60141, 54)
        z2 = z1 + PP(8.00108, 35)
        c3 = z2 + PP(2.56469, 180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_SWNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERs(cls, ta=None, **kwargs):
        #M 1013.36,-4.80571 C 1011.7633,-1.255503 1010.1667,2.1362823 1008.57,5.47059 1012.8,-0.569615 1019.65,-7.85871 1026.92,-7.85871

        #z0 = P(0, -0)
        #c0 = P(-0.56328, -1.25243)
        #c1 = P(-1.12653, -2.44898)
        #z1 = P(-1.68981, -3.62525)
        #c2 = P(-0.197556, -1.4944)
        #c3 = P(2.21897, 1.07703)
        z2 = P(4.78367, 1.07703)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.56328, -1.25243)
        #z1 = z0 + P(-1.68981, -3.62525)
        #c1 = z1 + P(0.56328, 1.17627)
        #c2 = z1 + P(1.49225, 2.13085)
        #z2 = z1 + P(6.47347, 4.70228)
        #c3 = z2 + P(-2.56469, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(1.37327, -114)
        z1 = z0 + PP(3.99974, -114)
        #z1 = z2 - PP(8.00108, ta + 35)
        c1 = z1 + PP(1.30418, 64)
        c2 = z1 + PP(2.60141, 54)
        z2 = z1 + PP(8.00108, 35)
        #c3 = z2 + PP(2.56469, 180)
        c3 = z2 + PP(2.56469, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_SWNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWNERswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NER(self, ta=None, **kwargs):
        #M 5482.19 69.3841 C 5486.42 63.3439 5493.27 56.0548 5500.54 56.0548
        return [p.transformed(pyx.trafo.trafo().translated(-5482.19, -69.3841).scaled(25.4 / 72, -25.4 / 72)) for p in [
            pyx.path.path(pyx.path.moveto(5482.19, 69.3841),
            pyx.path.curveto(5486.42, 63.3439, 5493.27, 56.0548, 5500.54, 56.0548))]]
