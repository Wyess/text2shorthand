from ..shugiin.char import ShugiinChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)


class JoshiKara(ShugiinChar):
    def __init__(self, name='a', kana='あ',
                 model='E9SWR9F', head_type='E', tail_type='SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {}

    def set_next_head(self, flick_len=2.0, dz=P(0, -1.5)):
        if getattr(self.after, 'name', '') in {'ta', 'da'}:
            self.to_flick = False
            super().set_next_head(flick_len, P(0, 0))
        else:
            super().set_next_head(flick_len, dz)

    @classmethod
    def path_ESWRF(cls, ta=None, **kwargs):
        #M 316.2205,405.47952 C 316.2205,405.47952 338.18469,404.12151 341.19942,405.13016 353.98793,409.40887 346.70778,420.32538 338.75393,423.12197

        z0 = P(0, -0)
        c0 = P(0, -0)
        c1 = P(7.74848, 0.479076)
        z1 = P(8.81201, 0.123246)
        c2 = P(13.3235, -1.38619)
        c3 = P(10.7552, -5.23729)
        z2 = P(7.94929, -6.22386)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_ESWRFe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRFswl(cls, ta=None, **kwargs):
        pass

class CharKara(ShugiinChar):
    def __init__(self, name='kara', kana='から',
                 model='E9SWR9F', head_type='E', tail_type='SWRF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {}

    def set_next_head(self, flick_len=2.0, dz=P(0, -1.5)):
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_ESWRF(cls, ta=None, **kwargs):
        #M 316.2205,405.47952 C 316.2205,405.47952 338.18469,404.12151 341.19942,405.13016 353.98793,409.40887 346.70778,420.32538 338.75393,423.12197

        z0 = P(0, -0)
        c0 = P(0, -0)
        c1 = P(7.74848, 0.479076)
        z1 = P(8.81201, 0.123246)
        c2 = P(13.3235, -1.38619)
        c3 = P(10.7552, -5.23729)
        z2 = P(7.94929, -6.22386)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])
