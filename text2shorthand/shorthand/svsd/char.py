import re
import pyx
from text2shorthand.common.point import Point as P, PPoint as PP
from text2shorthand.common.char import Char

class SvsdChar(Char):
    def __init__(self, name='', model='', kana='', head_type='', tail_type='', soundmark=''):
        super().__init__(name, model, kana, head_type, tail_type)
        self.soundmark = soundmark
        if self.soundmark != '':
            self.drawn_extra = False

        self.tail_ligature = {'E', 'ER', 'EL', 'NE', 'NER', 'NEL', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SW', 'SWR', 'SWL'}

    def draw_exclamation_dot(self, canvas, linewidth=0.5, color=None):
        if color is None:
            color = self.color

        z0 = P(*self.flick_atend(self.paths[0].reversed(), flick_len=1.0))
        p = pyx.path.line(*z0, *(P(0.01, -0.01) + z0))
        canvas.stroke(p.transformed(pyx.trafo.translate(*self.head)),
                      [pyx.style.linecap.round,
                      pyx.style.linewidth(linewidth),
                      pyx.style.linejoin.round,
                      color])

    def add_exclamation_dot(self):
        z0 = P(*self.flick_atend(self.paths[0].reversed(), flick_len=1.0))
        p = pyx.path.line(*z0, *(P(0.01, -0.01) + z0))
        self.paths_extra.append(p)


    def draw(self, canvas, linewidth=0.3, color=None):
        if self.tail_type.endswith('F'):
            linewidth = linewidth * 0.9
        elif self.model == 'P':
            linewidth = linewidth * 2.0
            
        super().draw(canvas, linewidth)
        
    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.head_type.startswith('B') and getattr(self.before, 'tail_type','-') not in self.barbs:
            self.head = self.before.tail - self.get_pos_xku()
        elif self.head_type.startswith('C') and getattr(self.before, 'tail_type', '-') not in self.head_circles:
            self.head = self.before.head + self.before.get_pos_tsux() - self.get_pos_xtsu()
        elif self.head_type.startswith('X') and not self.name.endswith('hitei'):
            self.head = self.before.head + self.before.get_pos_tsux() - self.get_pos_xtsu()

        super().set_next_head(flick_len=flick_len, dz=dz)

    def get_paths(self, **kwargs):
        me = self.model
        me = re.sub('^B', '', me)
        me = re.sub('[0-9]', '', me)

        if not re.match(fr"^C[RL]$", me):
            me = re.sub('^C[RL]', '', me)

        if self.head_type.startswith('B') and self.before and self.before.tail_type in self.barbs:
            return self.barb(super().get_paths(me=me))
        elif self.head_type.startswith('C') and self.before and self.before.tail_type in self.head_circles:
            return self.add_head_circle(super().get_paths(me=me))
        else:
            return super().get_paths(me=me)

    def get_paths_extra(self, **kwargs):
        if self.soundmark == 'LONG':
            return [self.path_SEL1().transformed(pyx.trafo.translate(*self.get_pos_chouon()))]
        elif self.soundmark == 'VOICED':
            return [self.path_P().transformed(pyx.trafo.translate(*self.get_pos_dakuon()))]
        elif self.soundmark in {'LONG_VOICED', 'VOICED_LONG'}:
            return [self.path_SEL1().transformed(pyx.trafo.translate(*self.get_pos_choudakuon()))]
        else:
            return []

    @classmethod
    def path_SEL1(self):
        return pyx.path.path(
            pyx.path.moveto(85.823585, 83.254715),
            pyx.path.curveto(85.620614, 84.698926, 87.198756, 85.499698, 88.658235, 86.089365)).transformed(pyx.trafo.trafo().translated(-86.7471, -85.060493).scaled(25.4 / 72, -25.4 / 72))

    @classmethod
    def path_SWR1(self):
        return pyx.path.path(
            pyx.path.moveto(88.647368, 83.254715),
            pyx.path.curveto(88.850339, 84.698926, 87.272197, 85.499698, 85.812718, 86.089365)).transformed(pyx.trafo.trafo().translated(-87.723853, -85.060493).scaled(25.4 / 72, -25.4 / 72))

    @classmethod
    def path_P(cls, ta=None, **kwargs):
        z0 = P(0, -0)
        c0 = z0
        z1 = z0 + PP(0.01, -90)
        c1 = z1

        return pyx.metapost.path.path([
            pyx.metapost.path.beginknot(*z0),
            pyx.metapost.path.controlcurve(c0, c1),
            pyx.metapost.path.endknot(*z1)])
