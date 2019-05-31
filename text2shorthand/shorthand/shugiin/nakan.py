from ..shugiin.char import ShugiinChar
from ..shugiin.naka import CharNaka
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


class CharNakan(ShugiinChar):
    def __init__(self, name='nakan', kana='なかん',
                 model='HEL9F', head_type='HEL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)
    
    @classmethod
    def path_HELF(self, ta=None, **kwwargs):
        return CharNaka.path_HEL()
