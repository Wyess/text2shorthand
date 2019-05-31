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


class CharMan(ShugiinChar):
    def __init__(self, name='man', kana='まん',
                 model='ER9F', head_type='ER', tail_type='ERF'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature -= {'EL', 'SEL', 'NER', 'SWL', 'S', 'E'}

    def set_next_head(self, flick_len=2.0, dz=P(1, 0)):
        if self.after.head_type == 'S':
            dz = P(0.5, -0.5)
        super().set_next_head(flick_len, dz)

    @classmethod
    def path_ERF(cls, ta=None, **kwargs):
        #M 741.6525,426.05961 C 747.4925,421.75319 760.96995,421.08987 767.16375,426.2497
        z0 = P(0, -0)
        c0 = P(2.06022, 1.51921)
        c1 = P(6.81477, 1.75321)
        z1 = P(8.9998, -0.0670595)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])
