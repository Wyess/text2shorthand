from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx

class CharOn(WasedaChar):
    def __init__(self, name='on', kana='おん', model='SW4NE1F', head_type='SW', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = 1.5

    @classmethod
    def path_SWNE(cls, ta = -110):
        return pyx.path.path(
            pyx.path.moveto(0, 0),
            pyx.path.rlineto(*PP(4, ta)),
            pyx.path.rlineto(*PP(1, 45)))

    @classmethod
    def path_SWNE_tan(cls, a):
        return cls.path_SWNE(a + 180)

    def get_paths(self):
        paths = [self.path_SWNE()]                           if self.before is None else \
                [self.path_SWNE(self.before.head_angle)]     if self.before.tail_type in {'SW'} else \
                [self.path_SWNE(self.before.tail_angle)]     if self.before.tail_type in {'ECL4'} else \
                [self.path_SWNE_tan(self.before.tail_angle)] if self.before.tail_type in {'SERCR1'} else \
                [self.path_SWNE()]

        return paths
