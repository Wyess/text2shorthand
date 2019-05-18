from math import atan, atan2, degrees
import re
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx import canvas, style, path, trafo, unit
from pyx.metapost.path import (
    beginknot, endknot, smoothknot, knot,
    tensioncurve, curve, path as mpath)

class Char():
    centerline = 0
    
    def __init__(self, name='', kana='',
                 model='', head_type='', tail_type='',
                 color=pyx.color.rgb.black):
        self.name                   = name
        self.model                  = model
        self.kana                   = kana
        self.paths                  = []
        self.paths_extra            = []
        self.soundmark              = ""
        self.w_soundmark            = False
        self.head                   = P(0, 0)
        self.tail                   = P(0, 0)
        #self.head_dir               = P(0, 0)
        #self.tail_dir               = P(0, 0)
        self.head_type              = head_type
        self.tail_type              = tail_type
        self.to_flick               = None  # True, False or None(default)
        self.before                 = None
        self.after                  = None
        self.bottom                 = 0
        self.offset                 = P(0, 0)
        self.offset_from_centerline = 0
        self.leftside               = 0
        self.dot_pos                = {}
        self.description            = ''
        self.color                  = color
        self.head_ligature          = set()
        self.tail_ligature          = set()
        self.both_ligature          = set() 
        self.head_translation       = {}
        self.tail_translation       = {}
        self.prev_name_ligature     = set()
        self.next_name_ligature     = set()
        self.drawn                  = False
        self.drawn_extra            = None

    def get_paths_extra(self, **kwargs):
        pass

    def get_paths(self, **kwargs):
        self.color = pyx.color.rgb.black

        bt = getattr(self.before, 'tail_type', '')
        bt = self.head_translation.get(bt, bt)

        ah = getattr(self.after, 'head_type', '')
        ah = self.tail_translation.get(ah, ah)

        me = kwargs.get('me', re.sub('[0-9]', '', self.model))

        if  bt + ':' + ah not in self.both_ligature:
            bt = bt if bt in self.head_ligature else ''
            ah = ah if ah in self.tail_ligature else ''

        ha = getattr(self.before, 'tail_angle', 0)
        ta = getattr(self.after, 'head_angle', 0)

        try:
            path_func = getattr(self, f'path_{bt.lower()}{me}{ah.lower()}', None)
            path = path_func(ta=ta, ha=ha)

            if path is None:
                self.color = pyx.color.rgb.red
                path_func = getattr(self, f'path_{bt.lower()}{me}', None)
                path = path_func(ta=ta, ha=ha)

            if path is None:
                self.color = pyx.color.rgb.red
                path_func = getattr(self, f'path_{me}{bt.lower()}', None)
                path = path_func(ta=ta, ha=ha)

            if path is None:
                raise Exception('path_func did not return a path')

            if isinstance(path, list):
                return path
            else:
                return [path]
        except:
            self.color = pyx.color.rgb.red
            path_func = getattr(self, f'path_{me}', None)
            if path_func is None:
                raise Exception('path_func did not return a path')
            else:
                path = path_func()
                if isinstance(path, list):
                    return path
                else:
                    return [path]

    def set_paths(self):
        pass

    def set_dot_pos(self):
        pass

    def connect(self, before, after):
        self.before = before
        self.after = after

    def set_before_after(self):
        self.before = before
        self.after = after

    def draw(self, canvas, linewidth=0.3, color=None):
        if color is None:
            color = self.color

        for p in self.paths:
            tmp = p.transformed(trafo.translate(*self.head))
            canvas.stroke(tmp,
                          [style.linecap.round,
                          style.linewidth(linewidth),
                          style.linejoin.round,
                          color])

        self.drawn = True


    @classmethod
    def move_to_tail(cls, path1, path2):
        if isinstance(path1, list):
            path1 = path1[-1]
        
        if isinstance(path2, list):
            return [p.transformed(trafo.translate(*path1.atend())) for p in path2]
        else:
            return path2.transformed(trafo.translate(*path1.atend()))

    def draw_extra(self, canvas, linewidth=0.3, color=None):
        if color is None:
            color = self.color

        if self.drawn_extra == False:
            for p in self.paths_extra:
                canvas.stroke(p.transformed(trafo.translate(*self.head)),
                              [style.linecap.round,
                              style.linewidth(linewidth),
                              style.linejoin.round,
                              color])
            self.drawn_extra = True

    def draw_dot(self, canvas, linewidth=0.3, color=None, dot=P(0, 0)):
        if color is None:
            color = self.color

        p = pyx.path.path(
            pyx.path.moveto(*dot),
            pyx.path.rlineto(*PP(0.1, -45)))

        canvas.stroke(p.transformed(trafo.translate(*self.head)),
                          [style.linecap.round,
                          style.linewidth(linewidth),
                          style.linejoin.round,
                          color]) 
        
    def flick_atend(self, apath, flick_len=2.0):
        return apath.tangent(apath.end(), length=flick_len).atend()

    def get_top(self):
        return max([p.bbox().top() for p in self.paths], default=0)

    def get_left_edge(self):
        return min([p.bbox().left() for p in self.paths], default=0)

    def get_right_edge(self):
        return max([p.bbox().right() for p in self.paths], default=0)

    def get_bottom(self):
        return min([p.bbox().bottom() for p in self.paths], default=0)

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if self.after is None:
            return

        if len(self.paths) > 0:
            self.tail = self.head + P(*self.paths[-1].atend()) + dz + self.offset

        if self.to_flick is None:
            self.to_flick = self.tail_type.endswith('F')

        if self.to_flick and (dz.x == 0 and dz.y == 0):
            self.after.head = self.head + P(*self.flick_atend(self.paths[-1], flick_len))
        else:
            self.after.head = self.tail

    @classmethod
    def jog(cls, paths, length=0.5, deg=10):
        if not isinstance(paths, list):
            paths = [paths]

        x, y = [coord / unit.length(1) for coord in
        paths[-1].tangent(paths[-1].end()).atend()]
        d = degrees(atan2(y, x))
        
        begin = P(*paths[-1].tangent(paths[-1].end()).atbegin())
        end = P(*paths[-1].tangent(paths[-1].end()).atend())
        tan = end - begin

        d = degrees(atan2(*[coord / unit.length(1) for coord in tan][::-1]))
        dp = trafo.rotate(d - deg if d <= -90 else d + deg).apply(-length, 0)
        paths[-1].append(path.rlineto(*dp))

        return paths

    @classmethod
    def add_head_circle(cls, paths, diameter=1.5):
        next_head_angle = degrees(atan2(*([coord / unit.length(1) for coord in
                                        paths[0].tangent(0).atend()[::-1]])))
        
        if next_head_angle >= 0:
            a0 = -70 + next_head_angle
            ha = next_head_angle - 90
            ta = next_head_angle
        else:
            a0 = -70 + next_head_angle
            ha = next_head_angle - 90
            ta = next_head_angle

        z0 = P(*paths[0].at(diameter))

        circle = pyx.metapost.path.path([
            beginknot(*z0, angle=ha),
            curve(),
            knot(*PP(diameter*0.7, a0)),
            curve(),
            endknot(0, 0, angle=ta)])

        paths[0] = circle.joined(paths[0])

        return paths

    @classmethod
    def bend(cls, paths, a1=10, a2=None, tn=1.0):
        assert isinstance(paths, list) and len(paths) > 0, 'Char.bend() takes a list of paths as an argument'
        assert tn >= 0.75, 'Tension value must be greater than or equal to 0.75'

        a2 = a2 if a2 is not None else a1
        
        rad0 = atan2(*[coord / unit.length(1) for coord
                       in pyx.trafo.rotate(a1).apply(*paths[0].tangent(0).atend())][::-1])
        z0   = paths[0].at(0)
        rad1 = atan2(*[coord / unit.length(1) for coord
                       in pyx.trafo.rotate(-a2).apply(*paths[0].tangent(paths[0].end()).atend())][::-1])
        z1   = paths[0].atend()

        return pyx.metapost.path.path([
            beginknot(*z0, angle=degrees(rad0)), 
            tensioncurve(tn), 
            endknot(*z1, angle=degrees(rad1))])

    @classmethod
    def barb(cls, paths, len_=2.0):
        next_head_angle = degrees(atan2(*([coord / unit.length(1) for coord in
                                        paths[0].tangent(0).atend()[::-1]])))
        
        if next_head_angle >= 0:
            a0 = 30 + next_head_angle
            ha = next_head_angle + 80 + 180
            ta = next_head_angle + 180
        else:
            a0 = -30 + next_head_angle
            ha = next_head_angle + 80
            ta = next_head_angle + 180

        barb = pyx.metapost.path.path([
            beginknot(*PP(len_, a0), angle=ha),
            curve(),
            endknot(0, 0, angle=ta)])

        paths[0] = barb.joined(paths[0])

        return paths

    def set_form(self):
        self.paths = self.get_paths()
        self.paths_extra = self.get_paths_extra()

    @property
    def head_dir(self):
        if len(self.paths) > 1:
            return P(*self.paths[0].tangent(0).atend())
        else:
            return P(1, 0)

    @property
    def tail_dir(self):
        if len(sefl.paths) > 1:
            return P(*self.paths[-1].tangent(self.paths[-1].end()).atend())
        else:
            return P(1, 0)

    @property
    def head_angle(self):
        if self.paths is None or len(self.paths) == 0:
            return 0

        begin = P(*self.paths[0].tangent(0).atbegin())
        end = P(*self.paths[0].tangent(0).atend())
        tan = end - begin

        return degrees(atan2(*[coord / unit.length(1) for coord in tan][::-1]))

    @property
    def tail_angle(self):
        if self.paths is None or len(self.paths) == 0:
            return 0

        begin = P(*self.paths[-1].tangent(self.paths[-1].end()).atbegin())
        end = P(*self.paths[-1].tangent(self.paths[-1].end()).atend())
        tan = end - begin

        return degrees(atan2(*[coord / unit.length(1) for coord in tan][::-1]))
