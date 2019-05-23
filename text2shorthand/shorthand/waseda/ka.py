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


class CharKa(WasedaChar):
    def __init__(self, name='ka', kana='か', 
                 model='E8', head_type='E', tail_type='E', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)

    def get_pos_dakuon(self):
        return P(4.5, -1.0)

    @classmethod
    def path_E(cls):
        return pyx.path.line(0, 0, 8, 0)

    def get_paths(self, **kwargs):
        return [self.path_E()]                         if self.after is None or self.tail_type.endswith('F') else \
               self.jog([self.path_E()])               if self.after.head_type in {'E', 'NEL'} else \
               self.jog([self.path_E()], length = 0.1) if self.after.head_type in {'SER'} else \
               [self.path_E()]

class CharKaku(CharKa):
    def __init__(self, name='kaku', kana='かく',
                 model='BE8', head_type='B', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.before is None or self.before.tail_type in {'E', 'P', ''}:
            path = self.barb([self.path_E()])[0]
        else:
            path = self.path_E()

        if self.before and self.before.tail_type.endswith('F'):
            return [path]

        if self.after is None:
            return [path]

        if self.after.head_type in {'E', 'NEL'}:
            return self.jog([path])

        if self.after.head_type in {'SER'}:
            return self.jog([path], length = 0.1)

        return [path]

    def set_next_head(self):
        if self.before and self.before.tail_type != 'E':
            self.head = self.before.tail - self.get_pos_xku()

        super().set_next_head()

class CharKatsu(CharKa):
    def __init__(self, name='katsu', kana='かつ', 
                 model='CL1E8', head_type='CL1', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'E', 'NEL', 'SER'}
        self.head_circles = ('', 'P', 'E')


    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return super(WasedaChar, self).get_paths()
        else:
            return super().get_paths()

    @classmethod
    def path_CLE(cls, ta=None, **kwargs):
        #M 51.745803,57.564901 C 52.047123,56.505618 52.284213,54.900984 49.77316,55.093299 48.200828,55.21372 46.835601,57.564901 49.198615,57.564901 56.39782,57.564901 63.597026,57.564901 70.796231,57.564901

        #z0 = P(0, -0)
        #c0 = P(0.106299, 0.373692)
        #c1 = P(0.189939, 0.939771)
        #z1 = P(-0.695905, 0.871926)
        #c2 = P(-1.25059, 0.829444)
        #c3 = P(-1.73221, -0)
        #z2 = P(-0.898591, -0)
        #c4 = P(1.64113, -0)
        #c5 = P(4.18085, -0)
        z3 = P(6.72057, -0)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.106299, 0.373692)
        #z1 = z0 + P(-0.695905, 0.871926)
        #c1 = z1 + P(0.885844, 0.0678445)
        #c2 = z1 + P(-0.554684, -0.0424819)
        #z2 = z1 + P(-0.202687, -0.871926)
        #c3 = z2 + P(-0.833619, 0)
        #c4 = z2 + P(2.53972, 0)
        #z3 = z2 + P(7.61916, 0)
        #c5 = z3 + P(-2.53972, 0)

        z0 = P(1.45, 0)
        c0 = z0 + PP(0.388516, 74)
        z1 = z0 + PP(1.11559, 128)
        c1 = z1 + PP(0.888438, 4)
        c2 = z1 + PP(0.556308, -175)
        z2 = z1 + PP(0.895174, -103)
        #z2 = z3 - PP(7.61916, ta + 0)
        c3 = z2 + PP(0.833619, 180)
        c4 = z2 + PP(2.53972, 0)
        z3 = z2 + PP(7.61916, 0)
        c5 = z3 + PP(2.53972, 180)

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

class CharGa(CharKa):
    def __init__(self, name='ka', kana='か', 
                 model='E8', head_type='E', tail_type='E', soundmark='VOICED'):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)

class CharKah(CharKa):
    def __init__(self, name='kah', kana='かー', 
                 model='E8', head_type='E', tail_type='E', soundmark='LONG'):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)

class CharGah(CharKa):
    def __init__(self, name='gah', kana='がー', 
                 model='E8', head_type='E', tail_type='E', soundmark='VOICED_LONG'):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)

class CharKaru(WasedaChar):
    def __init__(self, name='karu', kana='かる', 
                 model='E8S1F', head_type='E', tail_type='SF', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.tail_ligature ={''}


    @classmethod
    def path_ESF(cls, ta=None, **kwargs):
        #M 47.243566,57.082175 C 54.90888,57.082175 62.514541,57.082175 69.920766,57.082175 69.920766,58.027057 69.920766,58.971939 69.920766,59.916821

        #z0 = P(0, -0)
        #c0 = P(2.70415, -0)
        #c1 = P(5.38726, -0)
        #z1 = P(8.00001, -0)
        #c2 = P(8.00001, -0.333333)
        #c3 = P(8.00001, -0.666667)
        z2 = P(8.00001, -1)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.70415, 0)
        #z1 = z0 + P(8.00001, 0)
        #c1 = z1 + P(-2.61275, 0)
        #c2 = z1 + P(0, -0.333333)
        #z2 = z1 + P(0, -1)
        #c3 = z2 + P(0, 0.333333)

        z0 = P(0, -0)
        c0 = z0 + PP(2.70415, 0)
        z1 = z0 + PP(8.00001, 0)
        #z1 = z2 - PP(1, ta + 0)
        c1 = z1 + PP(2.61275, 180)
        c2 = z1 + PP(0.333333, -90)
        z2 = z1 + PP(1, -90)
        c3 = z2 + PP(0.333333, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_ESFe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFswl(cls, ta=None, **kwargs):
        pass

class CharKangami(WasedaChar):
    def __init__(self, name='kangami', kana='かんがみ', 
                 model='E8S1FP', head_type='E', tail_type='P'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature ={}

    @classmethod
    def path_ESFP(cls, ta=None, **kwargs):
        #M 47.3414,58.6772 70.0186,58.6772 73.5016,56.2383 M 68.942657,57.166339 C 68.924359,57.184637 69.064603,57.239914 68.982121,57.213779
        return [p.transformed(pyx.trafo.trafo().translated(-47.3414, -58.6772).scaled(25.4 / 72, -25.4 / 72)) for p in [
            pyx.path.path(pyx.path.moveto(47.3414, 58.6772),
            pyx.path.lineto(70.0186, 58.6772),
            pyx.path.lineto(73.5016, 56.2383)),
            pyx.path.path(pyx.path.moveto(68.942657, 57.166339),
            pyx.path.curveto(68.924359, 57.184637, 69.064603, 57.239914, 68.982121, 57.213779))]]

    @classmethod
    def path_ESFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESFPswl(cls, ta=None, **kwargs):
        pass
