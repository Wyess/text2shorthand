from ..waseda.shi import CharShi

class CharShin(CharShi):
    def __init__(self, name='shin', kana='しん',
                 model='NEL8CL1|SWR8CR1', head_type='NEL|SWR',
                 tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.head_type = 'SWR'
            self.tail_type = 'NEF' 

            return [self.path_SWRCRNE()]

        else:
            self.head_type = 'NEL'
            self.tail_type = 'NEF'

            return [self.path_NELCLNE()]
