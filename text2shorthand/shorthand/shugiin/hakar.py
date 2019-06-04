from ..shugiin.char import ShugiinChar
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


class CharHakar(ShugiinChar):
    def __init__(self, name='hakar', kana='はかＲ',
                 model='SEL9E18F', head_type='SEL', tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_SELEF(self, ta=None, **kwwargs):
        #M 192.72117,858.05473 C 192.55657,864.26793 197.90319,875.10232 205.23117,875.83208 208.82987,876.19045 256.25877,876.16131 256.25877,876.16131
        z0 = P(0, -0)
        c0 = P(-0.0580672, -2.19188)
        c1 = P(1.8281, -6.01401)
        z1 = P(4.41325, -6.27145)
        c2 = P(5.68279, -6.39788)
        c3 = P(22.4147, -6.3876)
        z2 = P(22.4147, -6.3876)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_SELEFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_SELEFswl(self, ta=None, **kwwargs):
        pass


