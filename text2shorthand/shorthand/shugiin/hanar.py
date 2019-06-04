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


class CharHanar(ShugiinChar):
    def __init__(self, name='hanar', kana='はなＲ',
                 model='HSEL18F', head_type='NWL', tail_type='SELF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_HSELF(self, ta=None, **kwwargs):
        #M 238.79262,800.29103 C 236.23592,797.79648 232.92187,795.96335 231.76951,799.69051 227.36758,813.92802 257.21226,836.26674 274.33137,831.15964
        z0 = P(0, -0)
        c0 = P(-0.901947, 0.880022)
        c1 = P(-2.07107, 1.52671)
        z1 = P(-2.4776, 0.21185)
        c2 = P(-4.0305, -4.81083)
        c3 = P(6.49804, -12.6914)
        z2 = P(12.5373, -10.8898)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_HSELFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_HSELFswl(self, ta=None, **kwwargs):
        pass


