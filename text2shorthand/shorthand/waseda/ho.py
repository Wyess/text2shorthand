import math
from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
from pyx.metapost.path import (
    beginknot, endknot, smoothknot, 
    tensioncurve, path)

class CharHo(WasedaChar):
    def __init__(self, name='ho', kana='ほ',
                 model='SEL16', head_type='SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 6

    @classmethod
    def path_SEL(cls, ha=-90, tn=0.88, ta=0, d=-60,
                 sellen=16, dz=P(0, 0)):
        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(*(PP(sellen, d) + dz), angle=ta)])

    @classmethod
    def path_SEL_smooth(cls, ta=0):
        return cls.path_SEL(ta=ta)

    @classmethod
    def path_SEL_up(cls, ta=60, dz=P(0, 2.7)):
        return cls.path_SEL(ta=ta, dz=dz)

    @classmethod
    def path_SELf(cls, ta=30, dz=P(0, 0.4)):
        return cls.path_SEL(ta=ta, dz=dz)

    @classmethod
    def path_SELnw(cls, ta=0):
        return cls.path_SEL(ta=ta)

    @classmethod
    def path_SELnel(cls, ha=-90, tn=1.5, ta=0):
        return path([
            beginknot(0, 0, angle=ha),
            tensioncurve(tn),
            endknot(*PP(16, -60), angle=ta)])
        
    def get_paths(self):
        if self.after is None:
            return [self.path_SEL()]
        
        if self.tail_type.endswith('F'):
            return [self.path_SELf()]

        if self.after.head_type in {'E','EL', 'NE', 'NL', 'SW', 'SR', 'SE', 'SEL'}:
            return [self.path_SEL_up()]

        if self.after.head_type == 'NEL':
            return [self.path_SELnel()]

        if self.after.head_type == 'SER':
            return [self.path_SEL_smooth(self.after.head_angle)]
        
        return [self.path_SEL()]


class CharHon(CharHo):
    def __init__(self, name='hon', kana='ほん',
                 model='SEL16F', head_type='SEL', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)
        
class CharHoku(CharHo):
    def __init__(self, name='hoku', kana='ほく',
                 model='BSEL16', head_type='BSEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharHotsu(CharHo):
    def __init__(self, name='hotsu', kana='ほつ',
                 model='CL1SEL16', head_type='CL1SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()
