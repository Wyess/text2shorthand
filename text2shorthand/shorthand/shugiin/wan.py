from ..shugiin.char import ShugiinChar
from ..shugiin.wa import CharWa
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


class CharWan(ShugiinChar):
    def __init__(self, name='wan', kana='わん',
                 model='UWL3F', head_type='SWL', tail_type='SWLSELF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.head_ligature = {'E', 'EL', 'SEL', 'NER'}
        #self.head_translation.update(dict.fromkeys(['SEL', 'NER', 'SWLSEL'], 'E'))
        #self.tail_ligature -= {'E', 'SR', 'S', 'EL', 'ER', 'SWL', 'NER', 'SER'}

    @classmethod
    def path_UWLF(cls, ta=None, **kwargs):
        return CharWa.path_UWL()
