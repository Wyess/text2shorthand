from ..waseda.i import CharI
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

class CharMo(CharI):
    def __init__(self, name='mo', kana='も', model='ER16',
                 head_type='ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_ER(cls, ha=20, ta=-80, tn=1.6):
        return pyx.metapost.path.path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(16, 0, angle=ta)])

    @classmethod
    def path_ER_smooth(cls, ta=-80):
        return cls.path_ER(ta=ta, tn=1.5)

    @classmethod
    def path_ERswr(cls, ta=-90, tn=1.6):
        return cls.path_ER(ta=ta, tn=tn)

    @classmethod
    def path_ER_down(cls, ta=-120, tn=2.0, deep=False):
        return cls.path_ER(ta=-100)

    @classmethod
    def path_ERNE(cls, ta=None, **kwargs):
        #M 387.51,115.37 C 401.73,110.194 434.929,103.664 432.865,115.37 433.62919,114.73181 434.42045,113.98204 435.48488,113.28297

        #z0 = P(0, -0)
        #c0 = P(5.0165, 1.82598)
        #c1 = P(16.7284, 4.12962)
        #z1 = P(16.0002, -0)
        #c2 = P(16.2698, 0.225139)
        #c3 = P(16.549, 0.489641)
        #z2 = P(16.9245, 0.736258)

        #z0 = P(0, -0)
        #c0 = z0 + P(5.0165, 1.82598)
        #z1 = z0 + P(16.0002, 0)
        #c1 = z1 + P(0.728133, 4.12962)
        #c2 = z1 + P(0.269589, 0.225139)
        #z2 = z1 + P(0.924235, 0.736258)
        #c3 = z2 + P(-0.375507, -0.246616)

        z0 = P(0, -0)
        c0 = z0 + PP(5.33849, 20)
        z1 = z0 + PP(16.0002, 0)
        #z1 = z2 - PP(1.18165, ta + 364)
        c1 = z1 + PP(4.19332, 80)
        c2 = z1 + PP(0.351235, 39)
        z2 = z1 + PP(1.18165, 38)
        c3 = z2 + PP(0.44925, -146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

        
    @classmethod
    def path_ER_cr1(cls, ha=23, ta=-90):
        return mpath([
            beginknot(0, 0, angle = ta),
            tensioncurve(2.05),
            endknot(*PP(16, 4), angle = ta)])
    
    def get_paths(self):
        return [self.path_ER()]                             if self.after is None else \
               [self.path_ER_smooth(self.after.head_angle)] if self.after.head_type in {'EL', 'SW', 'S'} else \
               [self.path_ERswr(self.after.head_angle)]     if self.after.head_type in {'SWR'} else \
               [self.path_ER_down()]                        if self.after.head_type in {'E', 'NER', 'NE', 'N', 'NL', 'NW', 'SR', 'SE', 'SER'} else \
               [self.path_ER()]

class CharMon(CharMo):
    def __init__(self, name='mon', kana='もん', model='ER16NE1F',
                 head_type='ER', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_ERNE()]

class CharMoku(CharMo):
    def __init__(self, name='moku', kana='もく', model='ER16F',
                 head_type='ER', tail_type='ERF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_ER_smooth(-60)]

class CharMora(CharMoku):
    def __init__(self, name='mora', kana='もら', model='ER16F',
                 head_type='ER', tail_type='ERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharMori(CharMoku):
    def __init__(self, name='mori', kana='もり', model='ER16F',
                 head_type='ER', tail_type='ERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharMoku(CharMo):
    def __init__(self, name='moku', kana='もく', model='BER16',
                 head_type='BER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharMotsu(CharMo):
    def __init__(self, name='motsu', kana='もつ', model='CR1ER16',
                 head_type='CRER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()

class CharMochi(CharMotsu):
    def __init__(self, name='mochi', kana='もち', model='CR1ER16',
                 head_type='CRER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
