from ..shugiin.char import ShugiinChar
from ..shugiin.ra import CharRa
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


class CharRan(ShugiinChar):
    def __init__(self, name='ran', kana='らん',
                 model='SER9F', head_type='SER', tail_type='SERF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature -= {'SR', 'S', 'EL', 'ER', 'SWL'}

    def set_next_head(self, flick_len=2.0, dz=P(1, 0)):
        if self.after.tail_type == 'SW':
            dz = P(0, -1)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_SERF(cls, ta=None, **kwargs):
        #M 0,173.055 C 7.1567541,174.09526 13.489981,179.21199 15.054283,188.2579
        z0 = P(0, -0)
        c0 = P(2.52474, -0.366981)
        c1 = P(4.75897, -2.17205)
        z1 = P(5.31082, -5.36325)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])
