from ..shugiin.char import ShugiinChar
from ..shugiin.saka import CharSaka
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


class CharSakan(ShugiinChar):
    def __init__(self, name='sakan', kana='さかん',
                 model='HSR9F', head_type='NER', tail_type='SRF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def set_next_head(self, flick_len=2.0, dz=P(0, -1)):
        #if self.after.name == 'wa':
        #    dz = P(0.5, -1)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_HSRF(cls, ta=None, **kwargs):
        return CharSaka.path_HSR()
