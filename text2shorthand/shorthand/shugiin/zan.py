from ..shugiin.char import ShugiinChar
from ..shugiin.sa import CharSa
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


class CharZan(ShugiinChar):
    def __init__(self, name='san', kana='さん',
                 model='SR9F', head_type='SR', tail_type='SRF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature -= {'E', 'S', 'EL', 'SEL', 'SWL'}


    def set_next_head(self, flick_len=2.0, dz=P(2.5, 1)):
        if self.after.head_type == 'NER':
            dz = P(2, -0.3)
        elif self.after.name == 'wa':
            dz = P(4, 0.7)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_SRF(cls, ta=None, **kwargs):
        return CharSa.path_SR()
