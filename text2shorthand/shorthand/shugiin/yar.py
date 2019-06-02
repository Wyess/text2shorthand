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


class CharYar(ShugiinChar):
    def __init__(self, name='yar', kana='やＲ',
                 model='NER19F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_NERF(self, ta=None, **kwwargs):
        #M 28.780832,504.96685 C 30.026406,490.32915 47.557577,469.44785 65.305525,469.34623
        z0 = P(0, -0)
        c0 = P(0.439411, 5.16386)
        c1 = P(6.62402, 12.5303)
        z1 = P(12.8851, 12.5662)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NERFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_NERFswl(self, ta=None, **kwwargs):
        pass


