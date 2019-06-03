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


class CharMakar(ShugiinChar):
    def __init__(self, name='makar', kana='まかＲ',
                 model='HER18F', head_type='HER', tail_type='ERF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HERF(self, ta=None, **kwwargs):
        #M -86.992009,786.08802 C -90.431211,786.76479 -94.161643,784.40617 -91.870432,782.46494 -76.670568,769.58687 -49.216284,774.31704 -41.706483,782.47087
        z0 = P(0, -0)
        c0 = P(-1.21327, -0.238749)
        c1 = P(-2.52929, 0.593319)
        z1 = P(-1.721, 1.27814)
        c2 = P(3.64118, 5.82124)
        c3 = P(13.3264, 4.15254)
        z2 = P(15.9757, 1.27605)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HERFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HERFswl(self, ta=None, **kwwargs):
        pass


