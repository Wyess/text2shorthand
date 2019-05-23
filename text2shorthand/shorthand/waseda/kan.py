from ..waseda.char import WasedaChar
from ..waseda.ka import CharKa
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx

class CharKan(WasedaChar):
    def __init__(self, name='kan', kana='かん',
                 model='E8NE1F', head_type='E', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_ENE1p5(cls):
        path = CharKa.path_E()
        path.append(pyx.path.rlineto(*PP(1.5, 35)))
        return path

    def get_paths(self):
        return [self.path_ENE1p5()]


