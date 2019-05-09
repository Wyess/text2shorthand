import re
import pyx
from text2shorthand.common.point import Point as P, PPoint as PP
from text2shorthand.common.char import Char

class WasedaChar(Char):
    def __init__(self, name='', model='', kana='', head_type='', tail_type='', soundmark=''):
        super().__init__(name, model, kana, head_type, tail_type)
        self.soundmark = soundmark
        if self.soundmark != '':
            self.drawn_extra = False

        self.tail_ligature = {'E', 'ER', 'EL', 'NE', 'NER', 'NEL', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SW', 'SWR', 'SWL'}
        self.barbs = {'', 'P'}
        self.head_circles = {'', 'P'}

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
        
    def get_pos_nai(self):
        if self.paths:
            return P(*self.paths[-1].reversed().at(1.2))
        else:
            return P(0, 0)

    def get_pos_naku(self):
        return self.get_pos_nai()

    def get_pos_nakatta(self):
        if self.paths:
            return P(*(self.paths[-1].at(self.paths[-1].arclen() * 0.5)))
        else:
            return P(0, 0)

    def get_pos_nakereba(self):
        return self.get_pos_nai()

    def get_pos_neba(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + P(2, 0)
        else:
            return P(0, 0)

    def get_pos_nakya(self):
        return self.get_pos_nai()

    def get_pos_mai(self):
        return self.get_pos_nai()

    def get_pos_dakuon(self):
        if self.paths:
            if self.head_type in {'NE', 'NE|SW', 'SW'}:
                return self.get_pos_nakatta() + P(-0.5, 1.5)
            else:
                return self.get_pos_nakatta() + P(0, -1)
        else:
            return P(0, 0)

    def get_pos_chouon(self):
        return self.get_pos_dakuon()

    def get_pos_choudakuon(self):
        return self.get_pos_nakatta()

    def get_pos_rare(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(3, -45)
        else:
            return PP(3, -45)

    def get_pos_sare(self):
        return self.get_pos_rare()

    def get_pos_a(self): 
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(2, -135) 
        else:
            return P(0, 0)

    def get_pos_aru(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + P(2, 0)
        else:
            return P(0, 0)

    def get_pos_oru(self):
        return self.get_pos_aru() + P(0, 1.3)

    def get_pos_an(self):
        return self.get_pos_a()

    def get_pos_i(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(2, 135)
        else:
            return P(0, 0)

    def get_pos_iru(self):
        return self.get_pos_aru()

    def get_pos_in(self):
        return self.get_pos_i()

    def get_pos_e(self):
        if self.paths:
            return P(*self.paths[-1].reversed().at(1.0))
        else:
            return P(0, 0)

    def get_pos_omou(self):
        return self.get_pos_a()

    def get_pos_ka(self):
        return self.get_pos_dakuon()

    def get_pos_kka(self):
        return self.get_pos_ka()

    def get_pos_kai(self):
        return self.get_pos_ka()
        
    def get_pos_kaku(self):
        return self.get_pos_ka()

    def get_pos_gaku(self):
        return self.get_pos_kaku()

    def get_pos_kata(self):
        if self.paths:
           return  P(*self.paths[-1].atend()) + PP(2, 45)
        else:
            return P(0, 0)

    def get_pos_hou(self):
        return self.get_pos_kata()

    def get_pos_kata_x(self):
        if self.paths:
            return P(*self.flick_atend(self.paths[-1].reversed()))
        else:
            return P(0, 0)

    def get_pos_kantan(self):
        return self.get_pos_kata_x()

    def get_pos_kyou(self):
        return self.get_pos_nakatta() + P(0, 1)

    def get_pos_gyou(self):
        return self.get_pos_kyou()

    def get_pos_shi(self):
        return self.get_pos_kyou()

    def get_pos_ji(self):
        return self.get_pos_i()

    def get_pos_sai(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + P(0, -2)
        else:
            return P(0, 0)

    def get_pos_juuon12(self):
        return self.get_pos_omou()

    def get_pos_juuon3(self):
        if self.paths:
            return self.get_pos_nakatta() + P(0, 2)
        else:
            return P(0, 0)

    def get_pos_su(self):
        return self.get_pos_i()

    def get_pos_suru(self):
        return self.get_pos_rare()

    def get_pos_ssuru(self):
        return self.get_pos_nakatta()

    def get_pos_soku(self):
        return self.get_pos_nakatta()

    def get_pos_zoku(self):
        return self.get_pos_soku()

    def get_pos_dai(self):
        if self.paths:
            return P(*self.paths[-1].atbegin()) + P(-3, 0)
        else:
            return P(0, 0)

    def get_pos_chi(self):
        return self.get_pos_i()

    def get_pos_chou(self):
        return self.get_pos_kai()

    def get_pos_tsu(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(3, 45)
        else:
            return P(0, 0)

    def get_pos_de(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + P(0, 1)
        else:
            return P(0, 0)

    def get_pos_teki(self):
        return self.get_pos_omou()

    def get_pos_tteki(self):
        return self.get_pos_ssuru()

    def get_pos_teki_x(self):
        if self.paths:
            return P(*self.paths[-1].atbegin()) + P(-1, 0)
        else:
            return P(0, 0)

    def get_pos_ten(self):
        if self.paths:
            return P(*self.paths[-1].atend()) + PP(2, 45)
        else:
            return P(0, 0)

    def get_pos_tten(self):
        return self.get_pos_nakatta()

    def get_pos_ten_x(self):
        if self.paths:
            return P(*self.paths[-1].atbegin()) + P(0, 1)
        else:
            return P(0, 0)

    def get_pos_naka(self):
       return self.get_pos_nakatta() + P(0, -1)

    def get_pos_nozo(self):
        return self.get_pos_omou()

    def get_pos_nodearu(self):
        return self.get_pos_aru()

    def get_pos_huu(self):
        return self.get_pos_nakatta() + P(0, -2)

    def get_pos_mx(self):
        if self.paths:
            return P(*self.paths[-1].atbegin()) + P(-1, 0)
        else:
            return P(0, 0)

    def get_pos_mi(self):
        return self.get_pos_i()

    def get_pos_you(self):
        if self.paths:
            x = self.get_pos_nakatta().x
            x = (self.paths[-1].bbox().left() + self.paths[-1].bbox().right()) / 2
            if self.after.head_type in {'SW|NE', 'SW', 'NE', 'P', 'SR', 'SL'}:
                y = self.get_pos_nakatta().y + 2
            else:
                y = self.paths[-1].bbox().top() + 2

            return P(x, y)

    def get_pos_ra(self):
        return self.get_pos_nakatta() + P(0, 1)

    def get_pos_tsux(self):
        if self.paths:
            return P(*self.paths[-1].reversed().at(1.5))
        else:
            return P(0, 0)

    def get_pos_xtsu(self):
        if self.paths:
            return P(*self.paths[0].at(1.5))
        else:
            return P(0, 0)

    def get_pos_xku(self):
        if self.paths:
            return P(*self.paths[0].at(1.5))
        else:
            return P(0, 0)

    def get_pos_x_kitsuon(self):
        return self.get_pos_nakatta()

    def get_pos_kitsuon_x(self):
        if self.paths:
            return P(*self.paths[0].at(1.5))
        else:
            return P(0, 0)

    def get_pos_p_kitsuon(self):
        return self.get_pos_nakatta() + P(0, -1.8)

    def get_pos_kitsuon_p(self):
        return self.get_pos_nakatta() + P(0, -1)

    def get_pos_ue(self):
        return self.get_pos_you() + P(0, 1)

    def get_pos_shita(self):
        return self.get_pos_huu()

    def get_pos_made(self):
        return self.get_pos_aru() + P(-1, 1)

    def get_pos_teido(self):
        return self.get_pos_made()

    def get_pos_go(self):
        return self.get_pos_kai() + P(0, -2)

    def get_pos_nen(self):
        return self.get_pos_nai()

    def get_pos_kasane(self):
        if self.paths:
            return P(*self.paths[0].at(0)) + P(0, -1.5)
        else:
            return P(0, 0)
    
    def get_pos_omoidasu(self):
        if self.paths:
            return P(*self.paths[-1].reversed().at(2)) + P(-1.5, 0)
        else:
            return P(0, 0)

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
