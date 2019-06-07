import re
import math
import pyx
from text2shorthand.common.point import Point as P, PPoint as PP
from text2shorthand.common.char import Char

class ShugiinChar(Char):
    def __init__(self, name='', model='', kana='',
                 head_type='', tail_type='',
                 soundmark=''):
        super().__init__(name, model, kana, head_type, tail_type)
        self.soundmark = soundmark
        if self.soundmark != '':
            self.drawn_extra = False

        if self.head_type == 'SWL':
            self.head_ligature = {'E', 'EL', 'SEL', 'NER'}
            self.head_translation.update(
                dict.fromkeys(['SEL', 'NER', 'SWLSEL', 'ELF', 'NERF'], 'E'))

        self.tail_ligature = {'E', 'ER', 'EL', 'NE', 'NER', 'NEL', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SW', 'SWR', 'SWL'}

        if self.tail_type.endswith('F'):
            self.tail_ligature = set()
        elif self.tail_type == 'E':
            self.tail_ligature = {'E'}
        elif self.tail_type == 'EL':
            self.tail_translation.update(
                dict.fromkeys(['NEL'], 'NE'))
            self.tail_ligature -= {'E', 'SR', 'S', 'EL', 'SEL', 'ER', 'NER', 'SWL'}
        elif self.tail_type == 'ER':
            self.tail_ligature -= {'EL', 'SEL', 'NER', 'SWL', 'S', 'E', 'SW'}
        elif self.tail_type == 'NEL':
            self.tail_ligature -= {'SR', 'NER', 'S'}
        elif self.tail_type == 'SEL':
            self.tail_ligature -= {'SR', 'S', 'ER', 'NER', 'SWL'}
            self.tail_translation = {'EL': 'E'}
        elif self.tail_type == 'S':
            self.tail_ligature = {'S', 'SEL'}
        elif self.tail_type == 'SWLSEL':
            self.tail_ligature -= {'E', 'SR', 'S', 'EL', 'ER', 'SWL', 'NER',
                                   'SER', 'SEL'}
        elif self.tail_type == 'NER':
            self.tail_ligature -= {'SR', 'S', 'EL', 'SWL'}
        elif self.tail_type == 'SER':
            pass
            #self.tail_ligature -= {'NE'}
        elif self.tail_type == 'SR':
            self.tail_ligature -= {'E', 'S', 'EL', 'SEL', 'SWL', 'ER'}

        self.barbs = {'', 'P'}
        self.head_circles = {'', 'P'}

    def get_paths_extra(self, **kwargs):
        return []

    def set_next_head(self, flick_len=1.0, dz=P(0, 0)):
        super().set_next_head(flick_len, dz)

    @classmethod
    def jog(cls, paths, length=0.5, deg=90):
        return Char.jog(paths, length=length, deg=deg)
