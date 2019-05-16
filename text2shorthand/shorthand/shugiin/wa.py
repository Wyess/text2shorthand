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


class CharWa(ShugiinChar):
    def __init__(self, name='wa', kana='わ',
                 model='UWL3', head_type='SWL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'E', 'EL', 'SEL', 'NER'}

    @classmethod
    def path_UWL(cls, ta=None, **kwargs):
        #M -575.32184,-219.07408 C -576.78685,-221.11124 -582.12084,-220.13256 -582.05617,-216.34696 -582.00659,-213.44457 -578.04742,-212.29027 -576.26799,-213.2859
        z0 = P(0, -0)
        c0 = z0 + PP(0.885203, 125)
        z1 = z0 + PP(2.56313, -157)
        #z1 = z2 - PP(2.3099, ta + 303)
        c1 = z1 + PP(1.33567, 90)
        c2 = z1 + PP(1.02405, -89)
        z2 = z1 + PP(2.3099, -27)
        c3 = z2 + PP(0.719325, -150)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswl(cls, ta=None, **kwargs):
        pass


    @classmethod
    def path_eUWL(cls, ta=None, **kwargs):
        #M 377.45,173.055 C 374.94127,173.055 372.49656,174.32588 372.49656,178.11188 372.54756,181.01388 376.56456,182.10388 378.33056,181.08488

        z0 = P(0, -0)
        c0 = P(-0.885024, -0)
        c1 = P(-1.74746, -0.448338)
        z1 = P(-1.74746, -1.78395)
        c2 = P(-1.72947, -2.80772)
        c3 = P(-0.312364, -3.19224)
        z2 = P(0.310642, -2.83276)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_eUWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_eUWLswl(cls, ta=None, **kwargs):
        pass


    @classmethod
    def path_elUWL(cls, ta=None, **kwargs):
        #M 379.57125,79.080276 C 376.87521,81.066608 373.83181,83.185161 375.08771,85.166596 375.91791,86.476394 377.80173,86.700437 380.38857,85.44541

        z0 = P(0, -0)
        c0 = P(-0.951103, -0.700734)
        c1 = P(-2.02475, -1.44811)
        z1 = P(-1.58169, -2.14712)
        c2 = P(-1.28882, -2.60919)
        c3 = P(-0.624247, -2.68822)
        z2 = P(0.288332, -2.24548)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_elUWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elUWLswl(cls, ta=None, **kwargs):
        pass


    @classmethod
    def path_selUWL(cls, ta=None, **kwargs):
        #M 191.539,474.785 C 189.60791,474.785 186.49552,475.77273 186.49552,479.55873 186.54552,482.46073 190.56352,483.55073 192.32952,482.53073

        z0 = P(0, -0)
        c0 = P(-0.681246, -0)
        c1 = P(-1.77923, -0.348449)
        z1 = P(-1.77923, -1.68407)
        c2 = P(-1.76159, -2.70783)
        c3 = P(-0.344128, -3.09235)
        z2 = P(0.278878, -2.73252)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            endknot(*z2)])

    @classmethod
    def path_selUWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selUWLswl(cls, ta=None, **kwargs):
        pass


    @classmethod
    def path_nerUWL(cls, ta=None, **kwargs):
        return cls.path_eUWL()

    @classmethod
    def path_nerUWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerUWLswl(cls, ta=None, **kwargs):
        pass
