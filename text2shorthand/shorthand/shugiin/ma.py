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


class CharMa(ShugiinChar):
    def __init__(self, name='ma', kana='ま',
                 model='ER9', head_type='ER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature -= {'EL', 'SEL', 'NER', 'SWL', 'S', 'E'}

    @classmethod
    def path_ER(cls, ta=None, **kwargs):
        #M155.759735457 173.496744455C160.81491909 167.883854524 172.391803128 164.772880425 180.246266334 173.496744455

        z0 = P(0, -0)
        c0 = P(1.78336, 1.9801)
        c1 = P(5.86742, 3.07759)
        z1 = P(8.6383, -0)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_ERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsr(cls, ta=None, **kwargs):
        #M 339.716,456.236 C 344.771,450.623 365.63329,450.89437 364.202,456.236

        z0 = P(0, -0)
        c0 = P(1.78329, 1.98014)
        c1 = P(9.14304, 1.88441)
        z1 = P(8.63812, -0)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_ERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERswl(cls, ta=None, **kwargs):
        pass
