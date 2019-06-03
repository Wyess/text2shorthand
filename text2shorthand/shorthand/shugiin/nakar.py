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


class CharNakar(ShugiinChar):
    def __init__(self, name='nakar', kana='なかＲ',
                 model='HEL18F', head_type='SWL', tail_type='ELF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HELF(self, ta=None, **kwwargs):
        #M -159.70879,830.07306 C -161.33716,828.98012 -166.49975,830.53053 -165.01411,832.3994 -155.0352,844.95244 -122.70691,843.16189 -114.27588,832.77396
        z0 = P(0, -0)
        c0 = P(-0.574453, 0.385565)
        c1 = P(-2.3957, -0.161385)
        z1 = P(-1.8716, -0.820681)
        c2 = P(1.64874, -5.24911)
        c3 = P(13.0534, -4.61745)
        z2 = P(16.0277, -0.952817)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HELFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HELFswl(self, ta=None, **kwwargs):
        pass


