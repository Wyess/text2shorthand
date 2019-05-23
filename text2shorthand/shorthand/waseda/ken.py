from ..waseda.char import WasedaChar
from ..waseda.ke import CharKe

class CharKen(WasedaChar):
    def __init__(self, name='ken', kana='けん',
                 model='E16CL1E1F', head_type='E', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [CharKe.path_ECLE()]
