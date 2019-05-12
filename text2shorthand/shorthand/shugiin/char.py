import re
import math
import pyx
from text2shorthand.common.point import Point as P, PPoint as PP
from text2shorthand.common.char import Char

class ShugiinChar(Char):
    def __init__(self, name='', model='', kana='', head_type='', tail_type='', soundmark=''):
        super().__init__(name, model, kana, head_type, tail_type)
        self.soundmark = soundmark
        if self.soundmark != '':
            self.drawn_extra = False

        self.tail_ligature = {'E', 'ER', 'EL', 'NE', 'NER', 'NEL', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SW', 'SWR', 'SWL'}
        self.barbs = {'', 'P'}
        self.head_circles = {'', 'P'}

    def get_paths_extra(self, **kwargs):
        return []

    @classmethod
    def jog(cls, paths, length=0.5, deg=90):
        return Char.jog(paths, length=length, deg=deg)
