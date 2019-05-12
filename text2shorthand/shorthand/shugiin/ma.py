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

    @classmethod
    def path_ER(cls, ta=None, **kwargs):
        #M -694.043,-150.46041 C -689.81648,-155.16578 -680.12928,-157.87156 -673.53933,-150.57848
        z0 = P(0, -0)
        c0 = z0 + PP(2.23127, 48)
        z1 = z0 + PP(7.23336, 0)
        c1 = z1 + PP(3.46758, 132)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
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
        pass

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
