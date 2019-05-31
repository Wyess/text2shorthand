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


class CharDan(ShugiinChar):
    def __init__(self, name='dan', kana='だん',
                 model='S9F', head_type='S', tail_type='SF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature = {'S', 'SEL'}

    def set_next_head(self, flick_len=2.0, dz=P(1, 1.5)):
        if self.after.head_type == 'SW':
            dz = P(2, 2)
        elif self.after.name == 'wa':
            dz = P(3.5, 1.2)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_SF(cls, ta=None, **kwargs):
        return CharTa.path_S()
