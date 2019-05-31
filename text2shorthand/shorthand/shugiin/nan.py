from ..shugiin.char import ShugiinChar
from ..shugiin.na import CharNa
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


class CharNan(ShugiinChar):
    def __init__(self, name='na', kana='な',
                 model='EL9F', head_type='EL', tail_type='ELF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature -= {'S', 'SEL', 'ER', 'NER', 'SWL', 'E', 'SW'}

    #def set_next_head(self, flick_len=2.0, dz=P(1, 0)):
    #    if self.after.name == 'wa':
    #        dz = P(2, -0.5)
    #    super().set_next_head(flick_len, dz)
    
    @classmethod
    def path_ELF(cls, ta=None, **kwargs):
        return CharNa.path_EL()
