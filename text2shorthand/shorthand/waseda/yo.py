from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    endknot,
    smoothknot,
    tensioncurve,
    path)

class CharYo(WasedaChar):
    def __init__(self, name='yo', kana='よ',
                 model='NER16', head_type='NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_NER(cls, ha=70, tn=1.7, ta=0, d=45, dz=P(0, 0),
                 before=None, after=None):
        if before:
            if before.tail_type == 'SWR':
                ha = 50
                d = 35
            #elif before.tail_type == 'NW|SWCR1':
            #    ha = 40
            #    d = 30
            #elif before.tail_type == 'SW':
            #    ha = before_tail_angle + 170
            #    d = 30
            elif before.tail_type in {'SR'}:
                ha = 50
                d = 30
                dz = P(1, 0)
            #else:
            #    ha = 70
            #    d = 40

        if after:
            if after.head_type in {'E', 'ER', 'NE', 'NER'}:
                ta = -80
                d = 35
            elif after.head_type in {'S', 'SW', 'SWR', 'SR', 'NEL'}:
                ta = after.head_angle
            elif after.head_type in {'SER'}:
                ha = 90
                ta = 0
                tn = 1.5
                d = 60
            elif after.head_type in {'NEL|SWR'}:
                tn = 1.5
                td = -40
            #else:
            #    tn = 1.1
            #    td = 0

        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn), 
            endknot(*(PP(16, d) + dz), angle=ta)])

    def get_paths(self):
        return [self.path_NER(before=self.before, after=self.after)]

class CharYon(CharYo):
    def __init__(self, name='yon', kana='よん',
                 model='NER16F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_NER(before=self.before, after=None)]

class CharYoku(CharYon):
    def __init__(self, name='yon', kana='よん',
                 model='NER16F', head_type='NER', tail_type='NERF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharYoku(CharYo):
    def __init__(self, name='yoku', kana='よく',
                 model='BNER16', head_type='BNER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharYotsu(CharYo):
    def __init__(self, name='yotsu', kana='よつ',
                 model='CR1NER16', head_type='CR1NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()
