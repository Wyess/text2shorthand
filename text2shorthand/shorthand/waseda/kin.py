from ..waseda.char import WasedaChar
from ..waseda.ki import CharKi

class CharKin(WasedaChar):
    def __init__(self, name='kin', kana='きん',
                 model='E8CL1E1F', head_type='E', tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [CharKi.path_ECLEF()]
