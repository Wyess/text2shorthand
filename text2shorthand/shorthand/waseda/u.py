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

class CharU(WasedaChar):
    def __init__(self, name='u', kana='う', 
                 model='S4', head_type='S', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 2

    def get_pos_you(self):
        return P(0, 2)

    @classmethod
    def path_S(cls):
        return pyx.path.line(0, 0, 0, -4)

    @classmethod
    def path_SNE(cls):
        #M 47.333858,183.4622 C 47.333858,187.24153 47.333858,191.02087 47.333858,194.8002 48.075458,194.16213 48.84201,193.52406 49.733858,192.88599

        #z0 = P(0, -0)
        #c0 = P(0, -1.32828)
        #c1 = P(0, -2.65657)
        #z1 = P(0, -3.98485)
        #c2 = P(0.260643, -3.7606)
        #c3 = P(0.530055, -3.53634)
        #z2 = P(0.843504, -3.31208)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -1.32828)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(0, 1.32828)
        #c2 = z1 + P(0.260643, 0.224256)
        #z2 = z1 + P(0.843504, 0.672768)
        #c3 = z2 + P(-0.313449, -0.224256)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32828, -90)
        z1 = z0 + PP(3.98485, -90)
        #z1 = z2 - PP(1.07894, ta + 362)
        c1 = z1 + PP(1.32828, 90)
        c2 = z1 + PP(0.343839, 40)
        z2 = z1 + PP(1.07894, 38)
        c3 = z2 + PP(0.38541, -144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])
        
    def get_paths(self):
        return [self.path_SNE()]                       if self.tail_type.endswith('NEF')  else \
               [self.path_S()]                         if self.after is None or self.tail_type.endswith('F') else \
               self.jog([self.path_S()])               if self.after.head_type in {'S', 'SEL'} else \
               self.jog([self.path_S()], length=0.1)   if self.after.head_type == 'EL' else \
               [self.path_S()]

class CharUku(CharU):
    def __init__(self, name='uku', kana='うく', 
                 model='BS4', head_type='B', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)

    def path_S(cls):
        return cls.barb([super().path_S()])[0]

class CharUn(CharU):
    def __init__(self, name='un', kana='うん', 
                 model='S4F', head_type='S', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharKun(CharUn):
    def __init__(self, name='kun', kana='くん', 
                 model='S4F', head_type='S', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharUki(WasedaChar):
    def __init__(self, name='uki', kana='うき', 
                 model='CL1S4', head_type='CL1', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 2

    def get_paths(self):
        if self.after.head_type in {'S', 'SEL'}:
            return self.jog([self.path_CLS()])
        elif self.after.head_type == 'EL':
            return self.jog([self.path_CLS()], length=0.1)
        else:
            return [self.path_CLS()]

    @classmethod
    def path_CLS(cls, ta=None, **kwawrgs):
        #M 43.795945,140.09579 C 45.470302,140.6469 46.714517,138.11422 45.755053,136.83728 44.456076,135.10849 43.643102,135.9591 43.755612,139.06533 43.802345,140.35556 43.680184,145.16142 43.660745,146.44297

        #z0 = P(0, -0)
        #c0 = P(0.590676, -0.194419)
        #c1 = P(1.02961, 0.699054)
        #z1 = P(0.69113, 1.14953)
        #c2 = P(0.23288, 1.75941)
        #c3 = P(-0.0539196, 1.45933)
        #z2 = P(-0.0142286, 0.363523)
        #c4 = P(0.00225778, -0.0916411)
        #c5 = P(-0.0408379, -1.78704)
        z3 = P(-0.0476956, -2.23914)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.590676, -0.194419)
        #z1 = z0 + P(0.69113, 1.14953)
        #c1 = z1 + P(0.338478, -0.450476)
        #c2 = z1 + P(-0.45825, 0.609879)
        #z2 = z1 + P(-0.705358, -0.786007)
        #c3 = z2 + P(-0.039691, 1.09581)
        #c4 = z2 + P(0.0164864, -0.455164)
        #z3 = z2 + P(-0.033467, -2.60267)
        #c5 = z3 + P(0.00685765, 0.452102)

        z0 = P(0, -0)
        c0 = z0 + PP(0.62185, -18)
        z1 = z0 + PP(1.3413, 58)
        c1 = z1 + PP(0.563468, -53)
        c2 = z1 + PP(0.762853, 126)
        z2 = z1 + PP(1.0561, -131)
        #z2 = z3 - PP(2.60288, ta + 1)
        c3 = z2 + PP(1.09653, 92)
        c4 = z2 + PP(0.455463, -87)
        z3 = z2 + PP(2.60288, -90)
        c5 = z3 + PP(0.452154, 89)

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
    def path_XCLS(cls, ta=None, **kwargs):
        #M 42.553308,140.0002 C 43.390487,140.27575 45.089496,140.03005 45.763182,139.15205 46.232887,138.53989 46.234785,137.47575 45.755053,136.83728 44.456078,135.10849 43.643102,135.9591 43.755612,139.06533 43.802345,140.35556 43.680184,145.16142 43.660745,146.44297

        #z0 = P(0, -0)
        #c0 = P(0.295338, -0.0972079)
        #c1 = P(0.894711, -0.0105304)
        #z1 = P(1.13237, 0.299208)
        #c2 = P(1.29807, 0.515165)
        #c3 = P(1.29874, 0.89057)
        #z2 = P(1.1295, 1.11581)
        #c4 = P(0.671255, 1.72569)
        #c5 = P(0.384455, 1.42561)
        #z3 = P(0.424146, 0.329801)
        #c6 = P(0.440632, -0.125363)
        #c7 = P(0.397537, -1.82076)
        z4 = P(0.390679, -2.27287)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.295338, -0.0972079)
        #z1 = z0 + P(1.13237, 0.299208)
        #c1 = z1 + P(-0.237661, -0.309739)
        #c2 = z1 + P(0.165701, 0.215956)
        #z2 = z1 + P(-0.00286773, 0.816599)
        #c3 = z2 + P(0.169239, -0.225238)
        #c4 = z2 + P(-0.45825, 0.609879)
        #z3 = z2 + P(-0.705358, -0.786007)
        #c5 = z3 + P(-0.039691, 1.09581)
        #c6 = z3 + P(0.0164864, -0.455164)
        #z4 = z3 + P(-0.033467, -2.60267)
        #c7 = z4 + P(0.00685765, 0.452102)

        z0 = P(0, -0)
        c0 = z0 + PP(0.310924, -18)
        z1 = z0 + PP(1.17124, 14)
        c1 = z1 + PP(0.390412, -127)
        c2 = z1 + PP(0.272202, 52)
        z2 = z1 + PP(0.816604, 90)
        c3 = z2 + PP(0.281734, -53)
        c4 = z2 + PP(0.762853, 126)
        z3 = z2 + PP(1.0561, -131)
        #z3 = z4 - PP(2.60288, ta + 1)
        c5 = z3 + PP(1.09653, 92)
        c6 = z3 + PP(0.455463, -87)
        z4 = z3 + PP(2.60288, -90)
        c7 = z4 + PP(0.452154, 89)

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

class CharUtsu(CharU):
    def __init__(self, name='utsu', kana='うつ', 
                 model='CR1S4', head_type='CR1S', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'S', 'SEL', 'EL', 'SWR'}

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()


    @classmethod
    def path_CRS(cls, ta=None, **kwargs):
        #M 206.577,112.48 C 203.708,113.412 204.09,109.93739 205.314,109.44339 205.771,109.26839 206.674,109.37039 206.637,110.44039 206.7,114.05039 206.637,117.065 206.637,120.928

        #z0 = P(0, -0)
        #c0 = P(-1.01212, -0.328789)
        #c1 = P(-0.877358, 0.896976)
        #z1 = P(-0.445558, 1.07125)
        #c2 = P(-0.284339, 1.13298)
        #c3 = P(0.0342194, 1.097)
        #z2 = P(0.0211667, 0.719529)
        #c4 = P(0.0433917, -0.553999)
        #c5 = P(0.0211667, -1.61749)
        z3 = P(0.0211667, -2.98027)

        #z0 = P(0, -0)
        #c0 = z0 + P(-1.01212, -0.328789)
        #z1 = z0 + P(-0.445558, 1.07125)
        #c1 = z1 + P(-0.4318, -0.174272)
        #c2 = z1 + P(0.161219, 0.0617361)
        #z2 = z1 + P(0.466725, -0.351719)
        #c3 = z2 + P(0.0130528, 0.377472)
        #c4 = z2 + P(0.022225, -1.27353)
        #z3 = z2 + P(0, -3.6998)
        #c5 = z3 + P(0, 1.36278)

        z0 = P(0, -0)
        c0 = z0 + PP(1.06418, -162)
        z1 = z0 + PP(1.16021, 112)
        c1 = z1 + PP(0.465642, -158)
        c2 = z1 + PP(0.172636, 20)
        z2 = z1 + PP(0.584413, -37)
        #z2 = z3 - PP(3.6998, ta + 0)
        c3 = z2 + PP(0.377698, 88)
        c4 = z2 + PP(1.27372, -89)
        z3 = z2 + PP(3.6998, -90)
        c5 = z3 + PP(1.36278, 90)

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
    def path_CRSe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSel(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRS()], length=0.1)[0]

    @classmethod
    def path_CRSne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSs(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRS()])[0]

    @classmethod
    def path_CRSsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSsel(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRS()])[0]

    @classmethod
    def path_CRSsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CRSswr(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CRS()])[0]

    @classmethod
    def path_CRSswl(cls, ta=None, **kwargs):
        pass
