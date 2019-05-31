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


class CharHan(ShugiinChar):
    def __init__(self, name='han', kana='はん',
                 model='SEL9F', head_type='SEL', tail_type='SELF'):
        super().__init__(name, kana, model, head_type, tail_type)
#        self.tail_ligature -= {'SR', 'S', 'ER', 'NER', 'SWL'}

    @classmethod
    def path_SELF(cls, ta=None, **kwargs):
        return CharHa.path_SEL()
