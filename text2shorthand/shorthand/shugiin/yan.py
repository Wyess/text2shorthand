from ..shugiin.char import ShugiinChar
from ..shugiin.ya import CharYa
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


class CharYan(ShugiinChar):
    def __init__(self, name='yan', kana='やん',
                 model='NER9F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'SR'}
        self.head_translation = {'SWLSEL': 'SR'}
        self.tail_ligature -= {'SR', 'S', 'EL', 'SEL', 'SWL'}

    def set_next_head(self, flick_len=2.0, dz=P(1, 0)):
        if self.after.name == 'wa':
            dz = P(0.5, -1)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_NERF(cls, ta=None, **kwargs):
        return CharYa.path_NER()
