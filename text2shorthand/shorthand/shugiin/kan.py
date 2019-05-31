from ..shugiin.char import ShugiinChar
from ..shugiin.ka import CharKa
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


class CharKan(ShugiinChar):
    def __init__(self, name='kan', kana='かん',
                 model='E9F', head_type='E', tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature = {'E'}

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.after.head_type == 'E':
            dz = P(1, -0.5)
        super().set_next_head(flick_len, dz)
    
    @classmethod
    def path_EF(cls, ta=None, **kwargs):
        return CharKa.path_E()
