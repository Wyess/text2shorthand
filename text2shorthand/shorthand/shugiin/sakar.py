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


class CharSakar(ShugiinChar):
    def __init__(self, name='sakar', kana='さかＲ',
                 model='HSR18F', head_type='HSR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HSRF(self, ta=None, **kwwargs):
        #M -54.664959,716.30018 C -56.41752,713.42583 -54.160919,709.64473 -52.628952,710.79099 -41.894577,718.8227 -37.601493,748.04969 -49.781868,761.62708
        z0 = P(0, -0)
        c0 = P(-0.618265, 1.01401)
        c1 = P(0.177814, 2.34789)
        z1 = P(0.718258, 1.94352)
        c2 = P(4.50511, -0.889889)
        c3 = P(6.01961, -11.2005)
        z2 = P(1.72265, -15.9903)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HSRFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSRFswl(self, ta=None, **kwwargs):
        pass


