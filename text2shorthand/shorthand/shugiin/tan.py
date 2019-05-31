from ..shugiin.char import ShugiinChar
from ..shugiin.ta import CharTa
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


class CharTan(ShugiinChar):
    def __init__(self, name='tan', kana='たん',
                 model='S9F', head_type='S', tail_type='SF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature = {'S', 'SEL'}

    def set_next_head(self, flick_len=2.0, dz=P(1, 0)):
        if self.after.tail_type == 'S':
            dz = P(0.5, -1)
        elif self.after.name == 'wa':
            dz = P(0, -1)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_SF(cls, ta=None, **kwargs):
        return CharTa.path_S()
