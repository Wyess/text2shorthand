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


class CharKa(ShugiinChar):
    def __init__(self, name='ka', kana='か',
                 model='E9', head_type='E', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature = {'E'}
    
    @classmethod
    def path_E(cls, ta=None, **kwargs):
        #M -807.64162,-189.49302 C -801.44934,-189.45591 -795.09916,-189.41881 -788.16217,-189.3817
        z0 = P(0, -0)
        c0 = z0 + PP(2.18454, 0)
        z1 = z0 + PP(9, 0)
        c1 = z1 + PP(2.44725, 179)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    @classmethod
    def path_Ee(cls, ta=None, **kwargs):
        return ShugiinChar.jog(cls.path_E())
        #return cls.path_E()

    @classmethod
    def path_Eer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ene(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ener(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Enel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Es(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ese(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswl(cls, ta=None, **kwargs):
        pass

class CharGa(CharKa):
    def __init__(self, name='ga', kana='が',
                 model='E7', head_type='E', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
