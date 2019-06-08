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


class CharNaru(ShugiinChar):
    def __init__(self, name='naru', kana='なる',
                 model='EL9NWL3F', head_type='EL', tail_type='NWLF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}

    def set_next_head(self, flick_len=1.0, dz=P(0, -3)):
        if self.after.head_type == 'SEL':
            dz = P(0, -1.5)
        elif self.after.head_type == 'NEL':
            dz = P(1, -3)
        super().set_next_head(flick_len, dz)
    
    @classmethod
    def path_ELNWLF(self, ta=None, **kwwargs):
        #M 170.16545,528.14588 C 175.16902,534.2793 190.64972,533.64214 194.69916,529.75994 196.69679,527.8448 194.22097,523.42588 187.7587,527.01603
        z0 = P(0, -0)
        c0 = P(1.76515, -2.16373)
        c1 = P(7.2264, -1.93896)
        z1 = P(8.65495, -0.569404)
        c2 = P(9.35967, 0.106214)
        c3 = P(8.48625, 1.66511)
        z2 = P(6.20651, 0.398586)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_ELNWLFe(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFer(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFne(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFner(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFnel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFse(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFser(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFsel(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFs(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFsr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFsl(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFsw(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFswr(self, ta=None, **kwwargs):
        pass

    @classmethod
    def path_ELNWLFswl(self, ta=None, **kwwargs):
        pass


