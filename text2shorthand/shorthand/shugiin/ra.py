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


class CharRa(ShugiinChar):
    def __init__(self, name='ra', kana='ら',
                 model='SER9', head_type='SER', tail_type='SER',
                 flick_pos=None):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature -= {'SR', 'S', 'EL', 'ER', 'SWL'}

    @classmethod
    def path_SER(cls, ta=None, **kwargs):
        #M -629.80918,-167.2956 C -622.58458,-167.62224 -612.614,-159.54934 -616.38931,-150.92415
        z0 = P(0, -0)
        c0 = z0 + PP(2.55128, 2)
        z1 = z0 + PP(7.46788, -50)
        c1 = z1 + PP(3.32149, 66)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    @classmethod
    def path_SERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERne(cls, ta=None, **kwargs):
        #M 0,173.055 C 7.1567541,174.09526 13.489981,179.21199 15.054283,188.2579
        z0 = P(0, -0)
        c0 = P(2.52474, -0.366981)
        c1 = P(4.75897, -2.17205)
        z1 = P(5.31082, -5.36325)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SERner(cls, ta=None, **kwargs):
        #M 268.536,78.6614 C 275.763,78.409 282.143,85.462627 282.143,94.8777

        z0 = P(0, -0)
        c0 = P(2.54952, 0.0890411)
        c1 = P(4.80025, -2.39932)
        z1 = P(4.80025, -5.72075)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERswl(cls, ta=None, **kwargs):
        pass
