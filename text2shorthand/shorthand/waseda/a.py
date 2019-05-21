from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P
import pyx
from pyx.metapost.path import (
    beginknot,
    endknot,
    smoothknot,
    tensioncurve,
    path)

class CharA(WasedaChar):
    def __init__(self, name='a', kana='あ',
                 model='EL4', head_type='EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_EL(cls, ta=80):
        return path([
            beginknot(0, 0, angle=-28),
            tensioncurve(1.2), 
            endknot(4, 0, angle=ta)])

    @classmethod
    def path_EL_smooth(cls, ta=80):
        return cls.path_EL(ta)

    @classmethod
    def path_EL_tan(cls, ta):
        return cls.path_EL(ta + 180)

    @classmethod
    def path_EL_flat(cls, ta=60):
        return cls.path_EL(ta)

    @classmethod
    def path_EL_up(cls, ta=90):
        return cls.path_EL(ta)

    def get_paths(self):
        if self.tail_type.endswith('F'):
            return [self.path_EL_flat()]

        if self.after is None:
            return [self.path_EL()]
        
        if self.after.name == "hitei_nai":
            return [self.path_EL_flat()]

        if self.after.head_type in {'SEL', 'F', 'XNE'}:
            return [self.path_EL_flat()]
        
        if self.after.head_type == 'ER':
            return [self.path_EL_smooth(self.after.head_angle)] 
        
        if self.after.head_type in {'SW', 'SWL'}:
            return [self.path_EL_tan(self.after.head_angle)]    

        if self.after.head_type in {'E', 'SE', 'NEL|SWR', 'NE'}:
            return [self.path_EL_up()]                          
               
        return [self.path_EL()]
        
class CharAku(CharA):
    def __init__(self, name='aku', kana='あく',
                 model='BEL4', head_type='BEL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_pos_you(self):
        return super().get_pos_you() + P(1, 0)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()
