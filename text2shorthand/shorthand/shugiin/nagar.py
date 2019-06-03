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


class CharNagar(ShugiinChar):
    def __init__(self, name='nagar', kana='ながＲ',
                 model='HNEL18F', head_type='SWL', tail_type='NELF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HNELF(self, ta=None, **kwwargs):
        #M -179.81402,903.40539 C -183.002,903.48688 -184.56,908.44857 -181.97502,909.11664 -167.5726,912.83885 -145.60668,898.87455 -141.53336,882.41279
        z0 = P(0, -0)
        c0 = P(-1.12465, -0.0287479)
        c1 = P(-1.67428, -1.77912)
        z1 = P(-0.762353, -2.0148)
        c2 = P(4.3185, -3.32792)
        c3 = P(12.0676, 1.59838)
        z2 = P(13.5046, 7.40572)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HNELFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HNELFswl(self, ta=None, **kwwargs):
        pass


