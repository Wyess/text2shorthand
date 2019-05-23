from ..waseda.char import WasedaChar
from ..waseda.ka import CharKa
from ..waseda.kan import CharKan
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

class CharKo(WasedaChar):
    def __init__(self, name='ko', kana='こ', model='E16', head_type='E', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'NEL', 'SER'}

    @classmethod
    def path_E(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, 16, 0)

    @classmethod
    def path_Ee(cls, ta=None, **kwargs):
        return cls.jog(cls.path_E())

    @classmethod
    def path_Enel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_E())

    @classmethod
    def path_Eser(cls, ta=None, **kwargs):
        return cls.jog(cls.path_E(), 0.1)

class CharKon(CharKo, CharKan):
    def __init__(self, name='kon', kana='こん', model='E16', head_type='E', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharKoku(CharKo):
    def __init__(self, name='koku', kana='こく', model='E16', head_type='BE', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharKotsu(CharKo):
    def __init__(self, name='kotsu', kana='こつ', model='CL1E16', head_type='CL1E', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'SER', 'NEL'}
        self.head_circles = {'E', '', 'P'}
    
    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super(CharKo, self).get_paths()

    @classmethod
    def path_CLE(cls, ta=None, **kwargs):
        #M 131.7682,104.83671 C 132.1981,104.13513 131.20453,102.24132 130.02357,102.62658 129.01934,102.95418 127.97218,104.99017 129.07753,104.99836 139.50785,105.07567 173.91687,104.99836 173.91687,104.99836

        #z0 = P(0, -0)
        #c0 = P(0.151659, 0.247502)
        #c1 = P(-0.19885, 0.915596)
        #z1 = P(-0.615467, 0.779685)
        #c2 = P(-0.969737, 0.664115)
        #c3 = P(-1.33915, -0.0541373)
        #z2 = P(-0.949209, -0.0570265)
        #c4 = P(2.73038, -0.0842998)
        #c5 = P(14.8691, -0.0570265)
        z3 = P(14.8691, -0.0570265)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.151659, 0.247502)
        #z1 = z0 + P(-0.615467, 0.779685)
        #c1 = z1 + P(0.416616, 0.135911)
        #c2 = z1 + P(-0.35427, -0.11557)
        #z2 = z1 + P(-0.333742, -0.836711)
        #c3 = z2 + P(-0.389943, 0.00288925)
        #c4 = z2 + P(3.67959, -0.0272732)
        #z3 = z2 + P(15.8183, 0)
        #c5 = z3 + P(0, 0)

        z0 = P(-1.3, 0)
        c0 = z0 + PP(0.290272, 58)
        z1 = z0 + PP(0.993332, 128)
        c1 = z1 + PP(0.438225, 18)
        c2 = z1 + PP(0.372644, -161)
        z2 = z1 + PP(0.900816, -111)
        #z2 = z3 - PP(15.8183, ta + 180)
        c3 = z2 + PP(0.389954, 179)
        c4 = z2 + PP(3.67969, 0)
        z3 = z2 + PP(15.8183, 0)
        c5 = z3 + PP(0, 0)

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
    def path_CLEe(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CLE()])[0]
    
    @classmethod
    def path_CLEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEnel(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CLE()])[0]

    @classmethod
    def path_CLEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEser(cls, ta=None, **kwargs):
        return cls.jog([cls.path_CLE()], length=0.1)[0]

    @classmethod
    def path_CLEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_CLEswl(cls, ta=None, **kwargs):
        pass
