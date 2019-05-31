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


class CharGan(ShugiinChar):
    def __init__(self, name='gan', kana='がん',
                 model='E9F', head_type='E', tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature = {'E'}

    def set_next_head(self, flick_len=2.0, dz=P(-2, 1)):
        if self.after.head_type in {'S', 'SEL'}:
            dz = P(1.5, 1.5)
        elif self.after.model == 'SW3':
            dz = P(-0.5, 4)
        super().set_next_head(flick_len, dz)
    
    @classmethod
    def path_EF(cls, ta=None, **kwargs):
        return CharKa.path_E()
