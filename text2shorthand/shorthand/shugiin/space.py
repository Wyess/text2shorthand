from ..shugiin.char import ShugiinChar
from text2shorthand.common.point import Point as P
import pyx

class CharSpace(ShugiinChar):
    def __init__(self, pos=P(10, 0), abs_=True,
                 to_centerline=True, set_centerline=False,
                 to_leftside=False, set_leftside=False,
                 name='space', kana='スペース',
                 model='', head_type='', tail_type=''):
        super().__init__(name, kana, model, head_type, tail_type)
        self.pos = pos
        self.abs = abs_
        self.to_centerline = to_centerline
        self.to_leftside = to_leftside
        self.set_centerline = set_centerline
        self.set_leftside = set_leftside

    def get_paths(self):
        return []

    def set_next_head(self):
        if self.after is not None:
            if (self.abs):
                self.head = self.pos
                self.tail = self.pos
            else:
                self.head += self.tail + self.pos
        super().set_next_head()

    def draw(self, canvas):
        return self.tail.x

