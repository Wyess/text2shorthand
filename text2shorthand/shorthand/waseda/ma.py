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

class CharMa(WasedaChar):
    def __init__(self, name='ma', kana='ま', model='ER8', head_type='ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'EL', 'SW', 'SWR', 'E', 'N', 'NL', 'NW', 'SR',
                              'SE', 'SER', 'NE', 'NER'}

    @classmethod
    def path_template(cls, ta=-90, tn=1.5):
        return mpath([beginknot(0, 0, angle=23), tensioncurve(tn), endknot(8, 0, angle=ta)])

    @classmethod
    def path_ER(cls, ta=None, **kwargs):
        return cls.path_template()

    @classmethod
    def path_ERel(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta)

    @classmethod
    def path_ERsw(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta)

#    @classmethod
#    def path_ERswr(cls, ta=None, **kwargs):
#        pass

    @classmethod
    def path_ERe(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERn(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERnl(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERnw(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERsr(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERse(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERser(cls, ta=None, **kwargs):
        return cls.path_template(ta=ta-80)

    @classmethod
    def path_ERne(cls, ta=None, **kwargs):
        return cls.path_template(ta=-110)

    @classmethod
    def path_ERner(cls, ta=None, **kwargs):
        return cls.path_template(ta=-110)

    @classmethod
    def path_ERNE(cls, ta=None, **kwargs):
        #M 296.802,115.37 C 305.002,111.889 321.682,109.317 319.479,115.37 320.65983,114.3649 321.84066,113.30084 323.02148,112.61408

        #z0 = P(0, -0)
        #c0 = P(2.89278, 1.22802)
        #c1 = P(8.77711, 2.13536)
        #z1 = P(7.99994, -0)
        #c2 = P(8.41651, 0.354577)
        #c3 = P(8.83308, 0.729954)
        z2 = P(9.24965, 0.972227)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.89278, 1.22802)
        #z1 = z0 + P(7.99994, 0)
        #c1 = z1 + P(0.777169, 2.13536)
        #c2 = z1 + P(0.416571, 0.354577)
        #z2 = z1 + P(1.24971, 0.972227)
        #c3 = z2 + P(-0.416567, -0.242274)

        z0 = P(0, -0)
        c0 = z0 + PP(3.14264, 23)
        z1 = z0 + PP(7.99994, 0)
        #z1 = z2 - PP(1.58335, ta + 366)
        c1 = z1 + PP(2.27239, 70)
        c2 = z1 + PP(0.547043, 40)
        z2 = z1 + PP(1.58335, 37)
        c3 = z2 + PP(0.481897, -149)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

#    @classmethod
#    def path_ER_smooth(cls, ta=-90):
#        return cls.path_ER(ta, 1.0)

    @classmethod
    def path_ERswr(cls, ta=35, **kwargs):
        #M 317.468,54.1384 C 325.713,50.6385 334.24004,48.203792 339.06323,53.417218

        #z0 = P(0, -0)
        #c0 = P(2.90865, 1.23469)
        #c1 = P(5.9168, 2.0936)
        z1 = P(7.61832, 0.254417)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.90865, 1.23469)
        #z1 = z0 + P(7.61832, 0.254417)
        #c1 = z1 + P(-1.70151, 1.83918)

        z0 = P(0, -0)
        c0 = z0 + PP(3.15986, 23)
        z1 = z0 + PP(7.62256, 1)
        #c1 = z1 + PP(2.50554, 132)
        c1 = z1 + PP(2.50554, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

#    @classmethod
#    def path_ER_down(cls, ta=-110, deep=False):
#        return cls.path_ER(ta=ta)
#        
#    @classmethod
#    def path_ER_cr1(cls, ta=-90):
#        return mpath([beginknot(0, 0, angle=26), tensioncurve(2.05), endknot(*PP(8, 4), angle=ta)])
#    
#    def get_paths(self):
#        return [self.path_ER()]                             if self.after is None or self.tail_type.endswith('F') else \
#               [self.path_ER_smooth(self.after.head_angle)] if self.after.head_type in {'EL', 'SW', 'S'} else \
#               [self.path_ERswr(self.after.head_angle)]     if self.after.head_type in {'SWR'} else \
#               [self.path_ER_down()]                        if self.after.head_type in {'E', 'NER', 'NE', 'N', 'NL', 'NW', 'SR', 'SE', 'SER'} else \
#               [self.path_ER()]

class CharMata(CharMa):
    def __init__(self, name='mata', kana='また', model='ER8', head_type='ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharMatsu(CharMa):
    def __init__(self, name='matsu', kana='まつ', model='CR1ER8', head_type='CR1', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_CRER(cls, ta=-90):
        #M 47.3414,59.093941 C 47.3414,63.809841 42.7622,61.981771 44.4907,60.531371 49.2901,56.644971 67.1451,54.3801 67.1451,60.2828

        #z0 = P(0, -0)
        #c0 = P(0, -1.66366)
        #c1 = P(-1.61544, -1.01876)
        #z1 = P(-1.00566, -0.507093)
        #c2 = P(0.687458, 0.863942)
        #c3 = P(6.98631, 1.66294)
        z2 = P(6.98631, -0.419403)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -1.66366)
        #z1 = z0 + P(-1.00566, -0.507093)
        #c1 = z1 + P(-0.609776, -0.511669)
        #c2 = z1 + P(1.69312, 1.37104)
        #z2 = z1 + P(7.99197, 0.0876903)
        #c3 = z2 + P(0, 2.08234)

        z0 = P(0, -0)
        c0 = z0 + PP(1.66366, -90)
        z1 = z0 + PP(1.12628, -153)
        #z1 = z2 - PP(7.99245, ta + 90)
        c1 = z1 + PP(0.79601, -139)
        c2 = z1 + PP(2.17862, 38)
        #z2 = z1 + PP(7.99245, 0)
        #c3 = z2 + PP(2.08234, 90)
        c3 = z2 + PP(2.08234, ta-180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {''}:
            return [self.path_CRER()]                      if self.after is None or self.tail_type.endswith('F') else \
                   [self.path_CRER(self.after.head_angle)] if self.after.head_type in {'EL', 'SW', 'S'} else \
                   [self.path_CRER(self.after.head_angle)] if self.after.head_type in {'SWR'} else \
                   [self.path_CRER(ta=-110)]               if self.after.head_type in {'E', 'NER', 'NE', 'N', 'NL', 'NW', 'SR', 'SE', 'SER'} else \
                   [self.path_CRER()]
        else:
            return super(CharMa, self).get_paths()

class CharMan(CharMa):
    def __init__(self, name='man', kana='まん',
        model='ER8NE1F', head_type='ER', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_ERNE()]

class CharMaku(CharMa):
    def __init__(self, name='maku', kana='まく', model='BER8', head_type='BER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()
