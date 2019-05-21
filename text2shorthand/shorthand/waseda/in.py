from ..waseda.i import CharI

class CharIn(CharI):
    def __init__(self, name='in', kana='いん',
                 model='ER4F', head_type='ER', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)
