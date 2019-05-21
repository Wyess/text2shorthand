from ..waseda.u import CharU

class CharUn(CharU):
    def __init__(self, name='un', kana='うん', 
                 model='S4F', head_type='S', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)
