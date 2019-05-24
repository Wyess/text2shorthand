from ..waseda.sa import CharSa

class CharSan(CharSa):
    def __init__(self, name='san', kana='さん',
                 model='NEL8F|SWR8F', head_type='NEL|SWR', tail_type='NELF|SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)

