from ..waseda.a import CharA

class CharAn(CharA):
    def __init__(self, name='an', kana='あん',
                 model='EL4F', head_type='EL', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)
