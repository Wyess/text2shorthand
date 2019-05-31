from ..shugiin.char import ShugiinChar
from ..shugiin.ha import CharHa
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


class CharBan(ShugiinChar):
    def __init__(self, name='ban', kana='ばん',
                 model='SEL9F', head_type='SEL', tail_type='SELF'):
        super().__init__(name, kana, model, head_type, tail_type)
#        self.tail_ligature -= {'SR', 'S', 'ER', 'NER', 'SWL'}

    def set_next_head(self, flick_len=2.0, dz=PP(2, 135)):
        if self.after.head_type in {'NE', 'E'}:
            dz = PP(2, 135)
        elif self.after.head_type == 'SW':
            dz = PP(4, 90)
        elif self.after.head_type == 'S':
            dz = P(1.5, 1.5)
        elif self.after.name == 'wa':
            dz = P(0, 3)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_SELF(cls, ta=None, **kwargs):
        return CharHa.path_SEL()
