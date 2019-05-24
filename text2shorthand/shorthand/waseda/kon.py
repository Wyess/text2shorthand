from ..waseda.char import WasedaChar
from ..waseda.ko import CharKo
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx

class CharKon(WasedaChar):
    def __init__(self, name='kon', kana='こん', model='E16NE1F', head_type='E', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {}

    @classmethod
    def path_ENEF(cls, ta=None, **kwargs):
        path = CharKo.path_E()
        path.append(pyx.path.rlineto(*PP(1.5, 35)))
        return path
