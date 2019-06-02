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


class CharKakar(ShugiinChar):
    def __init__(self, name='kakar', kana='かかＲ',
                 model='HE18F', head_type='HE', tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HEF(self, ta=None, **kwwargs):
        #M -52.61608,683.83749 C -55.179261,684.72029 -56.033878,681.25612 -54.427995,681.16729 -48.023468,680.81307 -4.1711966,680.69047 -4.1711966,680.69047
        z0 = P(0, -0)
        c0 = P(-0.904233, -0.311432)
        c1 = P(-1.20572, 0.91065)
        z1 = P(-0.639203, 0.941987)
        c2 = P(1.62017, 1.06695)
        c3 = P(17.0903, 1.1102)
        z2 = P(17.0903, 1.1102)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HEFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HEFswl(self, ta=None, **kwwargs):
        pass


