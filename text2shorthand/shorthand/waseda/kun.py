from ..waseda.char import WasedaChar
from ..waseda.ku import CharKu

class CharKun(WasedaChar):
    def __init__(self, name='kun', kana='くん',
                 model='E8CL4E1F', head_type='E', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [CharKu.path_ECLE()]

