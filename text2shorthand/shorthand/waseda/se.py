import math
from ..waseda.char import WasedaChar
#from waseda_shi import CharShi
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

class CharSe(WasedaChar):
    def __init__(self, name='se', kana='せ',
                 model='NEL16CL1|SWR16CR1', head_type='NEL|SWR',
                 tail_type='NELCL1|SWRCR1'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.offset_from_centerline = -6

    @classmethod
    def path_NELCL(cls, ta=-60, **kwargs):
        #M 0,31 C 8.512939,25.832245 32.070328,11.337509 32.070328,2.136902 32.070328,-0.841675 28.414494,-0.23956452 29.340164,1.206207 30.263478,2.6483 30.908527,3.8121276 31.466156,4.888535

        z0 = P(0, 0)
        c0 = P(2.99196, 1.81626)
        c1 = P(11.2714, 6.91058)
        z1 = P(11.2714, 10.1442)
        c2 = P(11.2714, 11.1911)
        c3 = P(9.98655, 10.9795)
        z2 = P(10.3119, 10.4713)
        c4 = P(10.6364, 9.96448)
        c5 = P(10.8631, 9.55545)
        z3 = P(11.0591, 9.17713)

        #z0 = P(0, 0)
        #c0 = z0 + P(2.99196, 1.81626)
        #z1 = z0 + P(11.2714, 10.1442)
        #c1 = z1 + P(0, -3.23364)
        #c2 = z1 + P(0, 1.04685)
        #z2 = z1 + P(-0.959543, 0.327102)
        #c3 = z2 + P(-0.325336, 0.508131)
        #c4 = z2 + P(0.324508, -0.506838)
        #z3 = z2 + P(0.747201, -1.29419)
        #c5 = z3 + P(-0.195984, 0.378314)

        z0 = P(0, 0)
        c0 = z0 + PP(3.50009, 31)
        z1 = z0 + PP(15.1641, 41)
        c1 = z1 + PP(3.23364, -90)
        c2 = z1 + PP(1.04685, 90)
        #z2 = z1 + PP(1.01376, 161)
        z2 = z3 - PP(1.4944, -60)
        c3 = z2 + PP(0.603357, 122)
        #c4 = z2 + PP(0.601822, -57)
        #z3 = z2 + PP(1.4944, -60)
        #c5 = z3 + PP(0.426065, 117)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            endknot(*z3)])

    @classmethod
    def path_NELCLse(cls, ta=None, **kwargs):
        #M 47.3414,189.494 C 55.8458,184.384 79.7825,170.459 79.7825,161.293 79.7825,158.326 75.6657,158.361 76.572,159.811 77.696591,161.65758 78.21584,162.56968 78.69,163.48

        #z0 = P(0, -0)
        #c0 = P(2.98896, 1.79596)
        #c1 = P(11.4017, 6.69004)
        #z1 = P(11.4017, 9.91152)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(9.95485, 10.942)
        #z2 = P(10.2734, 10.4324)
        #c4 = P(10.6686, 9.78338)
        #c5 = P(10.8511, 9.46282)
        z3 = P(11.0178, 9.14288)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98896, 1.79596)
        #z1 = z0 + P(11.4017, 9.91152)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04278)
        #z2 = z1 + P(-1.12836, 0.520864)
        #c3 = z2 + P(-0.318528, 0.509617)
        #c4 = z2 + P(0.395249, -0.648999)
        #z3 = z2 + P(0.744392, -1.28951)
        #c5 = z3 + P(-0.166648, 0.319941)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48702, 31)
        z1 = z0 + PP(15.1075, 41)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04278, 90)
        #z2 = z1 + PP(1.24278, 155)
        z2 = z3 - PP(1.48894, ta + 3)
        c3 = z2 + PP(0.600974, 122)
        #c4 = z2 + PP(0.759882, -58)
        #z3 = z2 + PP(1.48894, -60)
        #c5 = z3 + PP(0.360741, 117)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLser(cls, ta=-60, **kwargs):
        #M 112.709,189.688 C 121.181,184.598 145.029,170.725 145.029,161.593 145.029,158.637 141.13412,159.63833 140.543,161.02487 139.97188,162.36447 142.755,162.942 143.94,163.772

        #z0 = P(0, -0)
        #c0 = P(2.97757, 1.78893)
        #c1 = P(11.3592, 6.66473)
        #z1 = P(11.3592, 9.87427)
        #c2 = P(11.3592, 10.9132)
        #c3 = P(9.99029, 10.5613)
        #z2 = P(9.78253, 10.0739)
        #c4 = P(9.58181, 9.60312)
        #c5 = P(10.56, 9.40015)
        z3 = P(10.9764, 9.10843)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.97757, 1.78893)
        #z1 = z0 + P(11.3592, 9.87427)
        #c1 = z1 + P(0, -3.20953)
        #c2 = z1 + P(0, 1.03892)
        #z2 = z1 + P(-1.57665, 0.199675)
        #c3 = z2 + P(0.207755, 0.487313)
        #c4 = z2 + P(-0.200726, -0.470816)
        #z3 = z2 + P(1.19391, -0.965506)
        #c5 = z3 + P(-0.41648, 0.291712)

        z0 = P(0, -0)
        c0 = z0 + PP(3.47364, 30)
        z1 = z0 + PP(15.051, 40)
        c1 = z1 + PP(3.20953, -90)
        c2 = z1 + PP(1.03892, 90)
        #z2 = z1 + PP(1.58924, 172)
        z2 = z3 - PP(1.53545, ta + -2)
        c3 = z2 + PP(0.529751, 66)
        #c4 = z2 + PP(0.511819, -113)
        #z3 = z2 + PP(1.53545, -38)
        #c5 = z3 + PP(0.508479, 144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLsel(cls, ta=-90, **kwargs):
        #M 183.745,189.494 C 192.25,184.384 216.186,170.459 216.186,161.293 216.186,158.326 213.79516,159.80495 213.432,160.85397 212.62634,163.18121 212.68152,166.76506 212.83944,168.23963

        #z0 = P(0, -0)
        #c0 = P(2.98917, 1.79596)
        #c1 = P(11.4017, 6.69004)
        #z1 = P(11.4017, 9.91152)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(10.5614, 10.4345)
        #z2 = P(10.4338, 10.0658)
        #c4 = P(10.1506, 9.24789)
        #c5 = P(10.17, 7.98831)
        z3 = P(10.2255, 7.47006)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98917, 1.79596)
        #z1 = z0 + P(11.4017, 9.91152)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04278)
        #z2 = z1 + P(-0.96792, 0.154301)
        #c3 = z2 + P(0.127636, 0.368688)
        #c4 = z2 + P(-0.283157, -0.817931)
        #z3 = z2 + P(-0.208261, -2.59576)
        #c5 = z3 + P(-0.0555025, 0.518252)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4872, 30)
        z1 = z0 + PP(15.1075, 41)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04278, 90)
        #z2 = z1 + PP(0.980142, 170)
        z2 = z3 - PP(2.6041, ta + -10)
        c3 = z2 + PP(0.390157, 70)
        #c4 = z2 + PP(0.865558, -109)
        #z3 = z2 + PP(2.6041, -94)
        #c5 = z3 + PP(0.521216, 96)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_elNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLer(cls, ta=None, **kwargs):
        #M 17032.394,39.278 C 17042.944,39.278 17056.049,10.538332 17056.061,1.3683402 17056.064,-1.0715537 17054.12,-0.20303395 17053.246,1.1396272 17052.788,1.8684526 17052.454,3.0431046 17052.898,3.6983824 17053.476,4.5507678 17054.705,3.7547879 17055.934,3.1307742

        #z0 = P(0, -0)
        #c0 = P(3.72181, -0)
        #c1 = P(8.34496, 10.1387)
        #z1 = P(8.34919, 13.3737)
        #c2 = P(8.35025, 14.2344)
        #c3 = P(7.66445, 13.928)
        #z2 = P(7.35612, 13.4544)
        #c4 = P(7.19455, 13.1973)
        #c5 = P(7.07672, 12.7829)
        #z3 = P(7.23336, 12.5517)
        #c6 = P(7.43726, 12.251)
        #c7 = P(7.87083, 12.5318)
        z4 = P(8.30439, 12.7519)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.72181, 0)
        #z1 = z0 + P(8.34919, 13.3737)
        #c1 = z1 + P(-0.00423333, -3.23497)
        #c2 = z1 + P(0.00105833, 0.86074)
        #z2 = z1 + P(-0.993069, 0.0806849)
        #c3 = z2 + P(0.308328, 0.473661)
        #c4 = z2 + P(-0.161572, -0.257113)
        #z3 = z2 + P(-0.122767, -0.902672)
        #c5 = z3 + P(-0.156633, 0.231167)
        #c6 = z3 + P(0.203906, -0.300703)
        #z4 = z3 + P(1.07103, 0.20024)
        #c7 = z4 + P(-0.433564, -0.220138)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72181, 0)
        z1 = z0 + PP(15.7659, 58)
        c1 = z1 + PP(3.23497, -90)
        c2 = z1 + PP(0.860741, 89)
        z2 = z1 + PP(0.996342, 175)
        c3 = z2 + PP(0.565173, 56)
        c4 = z2 + PP(0.303666, -122)
        #z3 = z2 + PP(0.910982, -97)
        z3 = z4 - PP(1.08959, ta + 343)
        c5 = z3 + PP(0.279235, 124)
        #c6 = z3 + PP(0.363317, -55)
        #z4 = z3 + PP(1.08959, 10)
        #c7 = z4 + PP(0.486249, -153)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_selNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLser(cls, ta=None, **kwargs):
        #M 240.603,1715.48 C 250.52505,1715.48 273.044,1696.45 273.044,1687.28 273.044,1685.765 270.06486,1686.2312 269.73979,1687.2835 269.3835,1688.4369 271.55959,1688.5581 272.72831,1689.3292

        #z0 = P(0, -0)
        #c0 = P(3.50028, -0)
        #c1 = P(11.4445, 6.71336)
        #z1 = P(11.4445, 9.94833)
        #c2 = P(11.4445, 10.4828)
        #c3 = P(10.3935, 10.3183)
        #z2 = P(10.2788, 9.9471)
        #c4 = P(10.1531, 9.5402)
        #c5 = P(10.9208, 9.49745)
        z3 = P(11.3331, 9.22542)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.50028, 0)
        #z1 = z0 + P(11.4445, 9.94833)
        #c1 = z1 + P(0, -3.23497)
        #c2 = z1 + P(0, 0.534458)
        #z2 = z1 + P(-1.16565, -0.00123472)
        #c3 = z2 + P(0.114677, 0.371228)
        #c4 = z2 + P(-0.125691, -0.406894)
        #z3 = z2 + P(1.05428, -0.721677)
        #c5 = z3 + P(-0.412298, 0.272027)

        z0 = P(0, -0)
        c0 = z0 + PP(3.50028, 0)
        z1 = z0 + PP(15.1639, 40)
        c1 = z1 + PP(3.23497, -90)
        c2 = z1 + PP(0.534458, 90)
        #z2 = z1 + PP(1.16565, -179)
        z2 = z3 - PP(1.27763, ta + 0)
        c3 = z2 + PP(0.388537, 72)
        #c4 = z2 + PP(0.425865, -107)
        #z3 = z2 + PP(1.27763, -34)
        #c5 = z3 + PP(0.493952, 146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_selNELCLsw(cls, ta=None, **kwargs):
        #M 186.444,1715.48 C 196.3652,1715.48 219.57707,1691.2609 220.31293,1687.6694 221.69699,1680.9142 216.16905,1692.8727 215.27709,1694.461

        #z0 = P(0, -0)
        #c0 = P(3.49998, -0)
        #c1 = P(11.6886, 8.54396)
        #z1 = P(11.9482, 9.81096)
        #c2 = P(12.4365, 12.194)
        #c3 = P(10.4863, 7.97535)
        z2 = P(10.1717, 7.41504)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.49998, 0)
        #z1 = z0 + P(11.9482, 9.81096)
        #c1 = z1 + P(-0.259595, -1.267)
        #c2 = z1 + P(0.488266, 2.38308)
        #z2 = z1 + P(-1.77653, -2.39593)
        #c3 = z2 + P(0.314664, 0.560317)

        z0 = P(0, -0)
        c0 = z0 + PP(3.49998, 0)
        #z1 = z0 + PP(15.4601, 39)
        z1 = z2 - PP(2.9827, ta + -6)
        c1 = z1 + PP(1.29332, -101)
        #c2 = z1 + PP(2.43259, 78)
        #z2 = z1 + PP(2.9827, -126)
        #c3 = z2 + PP(0.642626, 60)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_selNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCL(cls, ta=None, **kwargs):
        #M 17009.794,0 C 17009.794,12.8022 17021.844,39.278 17032.394,39.278 17042.944,39.278 17056.061,10.53834 17056.061,1.3683402 17056.061,-1.6016198 17051.961,-1.5910298 17052.861,-0.12545985 17053.761,1.3005402 17054.767,3.2880699 17055.367,4.3703699

        #z0 = P(0, 0)
        #c0 = P(0, -4.51633)
        #c1 = P(4.25097, -13.8564)
        #z1 = P(7.97278, -13.8564)
        #c2 = P(11.6946, -13.8564)
        #c3 = P(16.322, -3.71769)
        #z2 = P(16.322, -0.48272)
        #c4 = P(16.322, 0.565016)
        #c5 = P(14.8756, 0.56128)
        #z3 = P(15.1931, 0.0442594)
        #c6 = P(15.5106, -0.458802)
        #c7 = P(15.8655, -1.15996)
        z4 = P(16.0771, -1.54177)

        #z0 = P(0, 0)
        #c0 = z0 + P(0, -4.51633)
        #z1 = z0 + P(7.97278, -13.8564)
        #c1 = z1 + P(-3.72181, 0)
        #c2 = z1 + P(3.72181, 0)
        #z2 = z1 + P(8.34919, 13.3737)
        #c3 = z2 + P(0, -3.23497)
        #c4 = z2 + P(0, 1.04774)
        #z3 = z2 + P(-1.12889, 0.526979)
        #c5 = z3 + P(-0.3175, 0.517021)
        #c6 = z3 + P(0.3175, -0.503061)
        #z4 = z3 + P(0.884061, -1.58603)
        #c7 = z4 + P(-0.211667, 0.381811)

        z0 = P(0, 0)
        c0 = z0 + PP(4.51633, -90)
        z1 = z0 + PP(15.9864, -60)
        c1 = z1 + PP(3.72181, 180)
        c2 = z1 + PP(3.72181, 0)
        z2 = z1 + PP(15.7659, 58)
        c3 = z2 + PP(3.23497, -90)
        c4 = z2 + PP(1.04774, 90)
        z3 = z2 + PP(1.24583, 154)
        #z3 = z4 - PP(1.81578, ta + 1)
        c5 = z3 + PP(0.606726, 121)
        c6 = z3 + PP(0.594875, -57)
        z4 = z3 + PP(1.81578, -60)
        c7 = z4 + PP(0.436558, 119)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    @classmethod
    def path_NELCLer(cls, ta=None, **kwargs):
        #M 8919.77,0 C 8928.33,-4.94242 8952.09,-18.9637 8952.09,-28.0957 8952.09,-29.5737 8951.3679,-29.936644 8950.606,-29.852522 8949.1922,-29.696427 8947.6977,-27.144857 8948.6298,-26.070407 8949.4176,-25.162336 8950.15,-26.1832 8952.03,-27.2727

        #z0 = P(0, 0)
        #c0 = P(3.01978, 1.74358)
        #c1 = P(11.4018, 6.68997)
        #z1 = P(11.4018, 9.91154)
        #c2 = P(11.4018, 10.4329)
        #c3 = P(11.147, 10.561)
        #z2 = P(10.8783, 10.5313)
        #c4 = P(10.3795, 10.4762)
        #c5 = P(9.85227, 9.5761)
        #z3 = P(10.1811, 9.19706)
        #c6 = P(10.459, 8.87671)
        #c7 = P(10.7174, 9.23685)
        z4 = P(11.3806, 9.6212)

        #z0 = P(0, 0)
        #c0 = z0 + P(3.01978, 1.74358)
        #z1 = z0 + P(11.4018, 9.91154)
        #c1 = z1 + P(0, -3.22157)
        #c2 = z1 + P(0, 0.521406)
        #z2 = z1 + P(-0.523522, 0.619768)
        #c3 = z2 + P(0.268781, 0.0296764)
        #c4 = z2 + P(-0.498757, -0.0550668)
        #z3 = z2 + P(-0.697159, -1.33425)
        #c5 = z3 + P(-0.328824, 0.379042)
        #c6 = z3 + P(0.277918, -0.320347)
        #z4 = z3 + P(1.19952, 0.424142)
        #c7 = z4 + P(-0.663222, -0.384351)

        z0 = P(0, 0)
        c0 = z0 + PP(3.48699, 30)
        z1 = z0 + PP(15.1076, 41)
        c1 = z1 + PP(3.22157, -90)
        c2 = z1 + PP(0.521406, 90)
        z2 = z1 + PP(0.811288, 130)
        c3 = z2 + PP(0.270415, 6)
        c4 = z2 + PP(0.501788, -173)
        #z3 = z2 + PP(1.5054, -117)
        z3 = z4 - PP(1.27229, ta + 348)
        c5 = z3 + PP(0.501795, 130)
        #c6 = z3 + PP(0.4241, -49)
        #z4 = z3 + PP(1.27229, 19)
        #c7 = z4 + PP(0.766544, -149)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_NELCLe(cls, ta=None, **kwargs):
        #M 47.3414,89.3562 C 55.8458,84.2462 79.7825,70.3218 79.7825,61.1556 79.7825,58.1881 75.028996,60.708291 75.042231,62.336631 75.05429,63.820178 78.093099,63.42874 79.377916,63.3423

        #z0 = P(0, -0)
        #c0 = P(2.98896, 1.79596)
        #c1 = P(11.4017, 6.68983)
        #z1 = P(11.4017, 9.91138)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(9.73108, 10.0686)
        #z2 = P(9.73573, 9.49629)
        #c4 = P(9.73997, 8.97489)
        #c5 = P(10.808, 9.11246)
        z3 = P(11.2595, 9.14284)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98896, 1.79596)
        #z1 = z0 + P(11.4017, 9.91138)
        #c1 = z1 + P(0, -3.22155)
        #c2 = z1 + P(0, 1.04296)
        #z2 = z1 + P(-1.66601, -0.415085)
        #c3 = z2 + P(-0.00465157, 0.572296)
        #c4 = z2 + P(0.00423825, -0.521407)
        #z3 = z2 + P(1.52382, -0.353452)
        #c5 = z3 + P(-0.451562, -0.0303802)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48702, 31)
        z1 = z0 + PP(15.1075, 40)
        c1 = z1 + PP(3.22155, -90)
        c2 = z1 + PP(1.04296, 90)
        #z2 = z1 + PP(1.71694, -166)
        z2 = z3 - PP(1.56427, ta-13)
        c3 = z2 + PP(0.572315, 90)
        #c4 = z2 + PP(0.521424, -89)
        #z3 = z2 + PP(1.56427, -13)
        #c5 = z3 + PP(0.452582, -176)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLel(cls, ta=-30, **kwargs):
        #M 129.717,89.3562 C 138.221,84.2462 162.158,70.3218 162.158,61.1556 162.158,58.1881 159.27106,58.390874 158.49374,59.277093 156.78797,61.221827 159.6616,62.489586 161.065,63.3423

        #z0 = P(0, -0)
        #c0 = P(2.98881, 1.79596)
        #c1 = P(11.4017, 6.68983)
        #z1 = P(11.4017, 9.91138)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(10.3871, 10.8831)
        #z2 = P(10.1139, 10.5716)
        #c4 = P(9.51436, 9.8881)
        #c5 = P(10.5243, 9.44254)
        z3 = P(11.0176, 9.14284)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98881, 1.79596)
        #z1 = z0 + P(11.4017, 9.91138)
        #c1 = z1 + P(0, -3.22155)
        #c2 = z1 + P(0, 1.04296)
        #z2 = z1 + P(-1.28784, 0.66022)
        #c3 = z2 + P(0.273197, 0.31147)
        #c4 = z2 + P(-0.59951, -0.683496)
        #z3 = z2 + P(0.903695, -1.42876)
        #c5 = z3 + P(-0.493239, 0.299695)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4869, 31)
        z1 = z0 + PP(15.1074, 41)
        c1 = z1 + PP(3.22155, -90)
        c2 = z1 + PP(1.04296, 90)
        #z2 = z1 + PP(1.44721, 152)
        z2 = z1 + PP(1.44721, 180 + ta + 4)
        #z2 = z3 - PP(1.69057, ta-25)
        c3 = z2 + PP(0.414307, 48)
        #c4 = z2 + PP(0.909164, -131)
        #z3 = z2 + PP(1.69057, -57)
        #c5 = z3 + PP(0.577149, 148)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])
        pass

    @classmethod
    def path_NELCLne(cls, ta=None, **kwargs):
        #M 47.3414,120.035 C 55.8458,114.925 79.7825,101.001 79.7825,91.8346 79.7825,88.8671 74.864576,93.909723 75.495496,95.055322 76.142569,96.230251 78.186111,94.465346 78.69,94.0213

        #z0 = P(0, -0)
        #c0 = P(2.98896, 1.79596)
        #c1 = P(11.4017, 6.68969)
        #z1 = P(11.4017, 9.91131)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(9.67329, 9.18199)
        #z2 = P(9.89504, 8.77935)
        #c4 = P(10.1225, 8.36641)
        #c5 = P(10.8407, 8.98671)
        z3 = P(11.0178, 9.14277)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98896, 1.79596)
        #z1 = z0 + P(11.4017, 9.91131)
        #c1 = z1 + P(0, -3.22162)
        #c2 = z1 + P(0, 1.04296)
        #z2 = z1 + P(-1.50671, -1.13195)
        #c3 = z2 + P(-0.221743, 0.402632)
        #c4 = z2 + P(0.22742, -0.41294)
        #z3 = z2 + P(1.12274, 0.363417)
        #c5 = z3 + P(-0.177097, -0.156064)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48702, 31)
        z1 = z0 + PP(15.1074, 40)
        c1 = z1 + PP(3.22162, -90)
        c2 = z1 + PP(1.04296, 90)
        #z2 = z1 + PP(1.88454, -143)
        z2 = z3 - PP(1.18009, 17)
        c3 = z2 + PP(0.459655, 118)
        #c4 = z2 + PP(0.471423, -61)
        #z3 = z2 + PP(1.18009, 17)
        #c5 = z3 + PP(0.236049, -138)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLnel(cls, ta=None, **kwargs):
        #M 208.04784,106.95605 C 216.60784,102.01405 241.33184,89.135451 241.33184,80.003351 241.33184,78.525151 240.63871,78.533576 239.94445,78.396235 238.7441,78.158777 236.94595,79.203998 236.6684,80.052276 236.19546,81.497786 239.02886,80.588136 241.33184,80.003351

        #z0 = P(0, -0)
        #c0 = P(3.01978, 1.74343)
        #c1 = P(11.7419, 6.28671)
        #z1 = P(11.7419, 9.50831)
        #c2 = P(11.7419, 10.0298)
        #c3 = P(11.4973, 10.0268)
        #z2 = P(11.2524, 10.0753)
        #c4 = P(10.829, 10.159)
        #c5 = P(10.1946, 9.79031)
        #z3 = P(10.0967, 9.49105)
        #c6 = P(9.92985, 8.98111)
        #c7 = P(10.9294, 9.30201)
        z4 = P(11.7419, 9.50831)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.01978, 1.74343)
        #z1 = z0 + P(11.7419, 9.50831)
        #c1 = z1 + P(0, -3.2216)
        #c2 = z1 + P(0, 0.521476)
        #z2 = z1 + P(-0.48944, 0.566955)
        #c3 = z2 + P(0.24492, -0.0484509)
        #c4 = z2 + P(-0.423457, 0.0837699)
        #z3 = z2 + P(-1.15572, -0.584214)
        #c5 = z3 + P(0.0979135, 0.299254)
        #c6 = z3 + P(-0.166843, -0.509944)
        #z4 = z3 + P(1.64516, 0.0172597)
        #c7 = z4 + P(-0.81244, -0.206299)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48692, 29)
        z1 = z0 + PP(15.1089, 38)
        c1 = z1 + PP(3.2216, -90)
        c2 = z1 + PP(0.521476, 90)
        z2 = z1 + PP(0.748992, 130)
        c3 = z2 + PP(0.249666, -11)
        c4 = z2 + PP(0.431663, 168)
        z3 = z2 + PP(1.29499, -153)
        #z3 = z4 - PP(1.64525, ta - 11)
        c5 = z3 + PP(0.314865, 71)
        c6 = z3 + PP(0.536544, -108)
        z4 = z3 + PP(1.64525, 0)
        #c7 = z4 + PP(0.838223, -165)
        c7 = z4 + PP(0.838223, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    @classmethod
    def path_NELCLner(cls, ta=None, **kwargs):
        #M 184.583,120.035 C 193.087,114.925 217.024,101.001 217.024,91.8346 217.024,87.790603 211.14199,92.6703 213.18976,95.735185 213.78845,96.631226 215.54597,94.818605 215.931,94.0213

        #z0 = P(0, -0)
        #c0 = P(2.98881, 1.79596)
        #c1 = P(11.4017, 6.68969)
        #z1 = P(11.4017, 9.91131)
        #c2 = P(11.4017, 11.3326)
        #c3 = P(9.33442, 9.61759)
        #z2 = P(10.0541, 8.54041)
        #c4 = P(10.2645, 8.22549)
        #c5 = P(10.8822, 8.86255)
        z3 = P(11.0176, 9.14277)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98881, 1.79596)
        #z1 = z0 + P(11.4017, 9.91131)
        #c1 = z1 + P(0, -3.22162)
        #c2 = z1 + P(0, 1.4213)
        #z2 = z1 + P(-1.34758, -1.3709)
        #c3 = z2 + P(-0.719709, 1.07718)
        #c4 = z2 + P(0.210416, -0.314922)
        #z3 = z2 + P(0.963436, 0.602362)
        #c5 = z3 + P(-0.135323, -0.280221)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4869, 31)
        z1 = z0 + PP(15.1074, 40)
        c1 = z1 + PP(3.22162, -90)
        c2 = z1 + PP(1.4213, 90)
        #z2 = z1 + PP(1.92233, -134)
        z2 = z3 - PP(1.13624, ta-33)
        c3 = z2 + PP(1.29549, 123)
        #c4 = z2 + PP(0.378749, -56)
        #z3 = z2 + PP(1.13624, 32)
        #c5 = z3 + PP(0.311185, -115)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLsw(cls, ta=None, **kwargs):
        #M 47.3414,237.123 C 55.8458,232.013 79.7825,218.089 79.7825,208.923 79.7825,205.955 78.475514,208.10159 78.158434,209.02743 77.219452,211.76917 76.107932,215.12293 75.951217,216.43055

        #z0 = P(0, -0)
        #c0 = P(2.98896, 1.79596)
        #c1 = P(11.4017, 6.68969)
        #z1 = P(11.4017, 9.91117)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(10.9424, 10.1999)
        #z2 = P(10.831, 9.87447)
        #c4 = P(10.5009, 8.91085)
        #c5 = P(10.1103, 7.73214)
        z3 = P(10.0552, 7.27257)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98896, 1.79596)
        #z1 = z0 + P(11.4017, 9.91117)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04313)
        #z2 = z1 + P(-0.570794, -0.036703)
        #c3 = z2 + P(0.111441, 0.325396)
        #c4 = z2 + P(-0.330014, -0.963612)
        #z3 = z2 + P(-0.775748, -2.6019)
        #c5 = z3 + P(0.055079, 0.459576)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48702, 31)
        z1 = z0 + PP(15.1073, 40)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04313, 90)
        z2 = z1 + PP(0.571973, -176)
        #z2 = z3 - PP(2.71508, ta + -9)
        c3 = z2 + PP(0.34395, 71)
        #c4 = z2 + PP(1.01856, -108)
        #z3 = z2 + PP(2.71508, -106)
        #c5 = z3 + PP(0.462865, 83)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLswr(cls, ta=None, **kwargs):
        #M117.335 237.123C125.839 232.013 149.776 218.089 149.776 208.923C149.776 205.955 145.659 205.99 146.565 207.441C147.485 208.878 148.128 210.037 148.683 211.109

        #z0 = P(0, -0)
        #c0 = P(2.98881, 1.79596)
        #c1 = P(11.4017, 6.68969)
        #z1 = P(11.4017, 9.91117)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(9.95475, 10.942)
        #z2 = P(10.2732, 10.432)
        #c4 = P(10.5965, 9.92698)
        #c5 = P(10.8225, 9.51964)
        z3 = P(11.0176, 9.14288)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98881, 1.79596)
        #z1 = z0 + P(11.4017, 9.91117)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04313)
        #z2 = z1 + P(-1.12854, 0.520864)
        #c3 = z2 + P(-0.318423, 0.509968)
        #c4 = z2 + P(0.323343, -0.505048)
        #z3 = z2 + P(0.744392, -1.28915)
        #c5 = z3 + P(-0.19506, 0.376765)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4869, 31)
        z1 = z0 + PP(15.1073, 40)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04313, 90)
        #z2 = z1 + PP(1.24294, 155)
        z2 = z3 - PP(1.48864, ta + 4)
        c3 = z2 + PP(0.601216, 121)
        #c4 = z2 + PP(0.599687, -57)
        #z3 = z2 + PP(1.48864, -59)
        #c5 = z3 + PP(0.424264, 117)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLswl(cls, ta=None, **kwargs):
        #M 71.7779,950.021 C 80.2739,945.116 103.575,933.168 104.837,924.193 105.898,916.638 102.66933,925.22329 100.22273,931.27829

        #z0 = P(0, -0)
        #c0 = P(2.9972, 1.73037)
        #c1 = P(11.2173, 5.94536)
        #z1 = P(11.6625, 9.11154)
        #c2 = P(12.0368, 11.7768)
        #c3 = P(10.8978, 8.74808)
        #z2 = P(10.0347, 6.61201)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.9972, 1.73037)
        #z1 = z0 + P(11.6625, 9.11154)
        #c1 = z1 + P(-0.445206, -3.16618)
        #c2 = z1 + P(0.374297, 2.66524)
        #z2 = z1 + P(-1.62781, -2.49953)
        #c3 = z2 + P(0.863106, 2.13607)

        z0 = P(0, -0)
        c0 = z0 + PP(3.46084, 29)
        z1 = z0 + PP(14.7998, 37)
        #z1 = z2 - PP(2.98286, ta + -10)
        c1 = z1 + PP(3.19733, -98)
        #c2 = z1 + PP(2.69139, 82)
        z2 = z1 + PP(2.98286, -123)
        #c3 = z2 + PP(2.30385, 67)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_NELCLs(cls, ta=None, **kwargs):
        #M 47.3414,136.138 C 55.8458,131.028 79.7825,117.103 79.7825,107.937 79.7825,104.97 77.096937,105.34119 77.242401,106.51087 77.394559,107.73436 77.577236,112.30118 77.572685,113.42874

        #z0 = P(0, -0)
        #c0 = P(2.98896, 1.79596)
        #c1 = P(11.4017, 6.69004)
        #z1 = P(11.4017, 9.91152)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(10.4579, 10.8238)
        #z2 = P(10.509, 10.4127)
        #c4 = P(10.5625, 9.98274)
        #c5 = P(10.6267, 8.37769)
        z3 = P(10.6251, 7.98139)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98896, 1.79596)
        #z1 = z0 + P(11.4017, 9.91152)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04278)
        #z2 = z1 + P(-0.892743, 0.501227)
        #c3 = z2 + P(-0.0511248, 0.411096)
        #c4 = z2 + P(0.0534774, -0.430008)
        #z3 = z2 + P(0.116082, -2.43135)
        #c5 = z3 + P(0.00159949, 0.396292)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48702, 31)
        z1 = z0 + PP(15.1075, 41)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04278, 90)
        #z2 = z1 + PP(1.02383, 150)
        z2 = z3 - PP(2.43412, ta + 4)
        c3 = z2 + PP(0.414262, 97)
        #c4 = z2 + PP(0.43332, -82)
        #z3 = z2 + PP(2.43412, -87)
        #c5 = z3 + PP(0.396295, 89)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_NELCLsl(cls, ta=None, **kwargs):
        #M 6351.13,0 C 6359.6,-5.0907 6383.2146,-18.928626 6383.45,-28.0953 6383.4947,-29.834909 6378.4208,-20.624608 6377.327,-18.541165

        #z0 = P(0, 0)
        #c0 = P(2.98803, 1.79589)
        #c1 = P(11.3187, 6.6776)
        #z1 = P(11.4018, 9.9114)
        #c2 = P(11.4175, 10.5251)
        #c3 = P(9.62759, 7.2759)
        z2 = P(9.24172, 6.54091)

        #z0 = P(0, 0)
        #c0 = z0 + P(2.98803, 1.79589)
        #z1 = z0 + P(11.4018, 9.9114)
        #c1 = z1 + P(-0.0830439, -3.2338)
        #c2 = z1 + P(0.0157692, 0.613695)
        #z2 = z1 + P(-2.16006, -3.37049)
        #c3 = z2 + P(0.385868, 0.734992)

        z0 = P(0, 0)
        c0 = z0 + PP(3.48619, 31)
        z1 = z0 + PP(15.1075, 40)
        #z1 = z2 - PP(4.00325, ta + -4)
        c1 = z1 + PP(3.23486, -91)
        c2 = z1 + PP(0.613898, 88)
        z2 = z1 + PP(4.00325, -122)
        c3 = z2 + PP(0.830125, 62)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    def path_NELCLsr(cls, ta=None, **kwargs):
        #M195.084 136.138C203.588 131.028 227.525 117.103 227.525 107.937C227.525 104.97 223.408 105.005 224.314 106.455C225.234 107.892 225.877 109.051 226.432 110.124

        #z0 = P(0, -0)
        #c0 = P(2.98881, 1.79596)
        #c1 = P(11.4017, 6.69004)
        #z1 = P(11.4017, 9.91152)
        #c2 = P(11.4017, 10.9543)
        #c3 = P(9.95475, 10.942)
        #z2 = P(10.2732, 10.4324)
        #c4 = P(10.5965, 9.92734)
        #c5 = P(10.8225, 9.51999)
        z3 = P(11.0176, 9.14288)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98881, 1.79596)
        #z1 = z0 + P(11.4017, 9.91152)
        #c1 = z1 + P(0, -3.22148)
        #c2 = z1 + P(0, 1.04278)
        #z2 = z1 + P(-1.12854, 0.520864)
        #c3 = z2 + P(-0.318423, 0.509617)
        #c4 = z2 + P(0.323343, -0.505048)
        #z3 = z2 + P(0.744392, -1.28951)
        #c5 = z3 + P(-0.19506, 0.377116)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4869, 31)
        z1 = z0 + PP(15.1075, 41)
        c1 = z1 + PP(3.22148, -90)
        c2 = z1 + PP(1.04278, 90)
        #z2 = z1 + PP(1.24294, 155)
        z2 = z3 - PP(1.48894, ta + 3)
        c3 = z2 + PP(0.600918, 121)
        #c4 = z2 + PP(0.599687, -57)
        #z3 = z2 + PP(1.48894, -60)
        #c5 = z3 + PP(0.424577, 117)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_erSWRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRne(cls, ta=None, **kwargs):
        #M 227.43,278.61 C 235.09099,287.73168 218.38793,318.54303 208.054,318.336 206.1841,318.29854 209.84309,316.37048 211.47108,315.8119 212.4312,315.48248 213.23806,315.38421 215.21697,314.559

        #z0 = P(0, -0)
        #c0 = P(2.70263, -3.21793)
        #c1 = P(-3.18984, -14.0875)
        #z1 = P(-6.83542, -14.0144)
        #c2 = P(-7.49508, -14.0012)
        #c3 = P(-6.20427, -13.3211)
        #z2 = P(-5.62995, -13.124)
        #c4 = P(-5.29124, -13.0078)
        #c5 = P(-5.0066, -12.9731)
        z3 = P(-4.30849, -12.682)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.70263, -3.21793)
        #z1 = z0 + P(-6.83542, -14.0144)
        #c1 = z1 + P(3.64558, -0.0730356)
        #c2 = z1 + P(-0.659659, 0.0132151)
        #z2 = z1 + P(1.20547, 0.890446)
        #c3 = z2 + P(-0.574319, -0.197055)
        #c4 = z2 + P(0.338709, 0.116212)
        #z3 = z2 + P(1.32147, 0.441995)
        #c5 = z3 + P(-0.698115, -0.291116)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20229, -49)
        z1 = z0 + PP(15.5926, -116)
        c1 = z1 + PP(3.64631, -1)
        c2 = z1 + PP(0.659792, 178)
        z2 = z1 + PP(1.49868, 36)
        #z2 = z3 - PP(1.39343, ta + 355)
        c3 = z2 + PP(0.607184, -161)
        #c4 = z2 + PP(0.358091, 18)
        #z3 = z2 + PP(1.39343, 18)
        #c5 = z3 + PP(0.756382, -157)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_erSWRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCR(cls, ta=None, **kwargs):
        #M 227.43,278.61 C 235.09099,287.73168 218.39,318.336 208.054,318.336 204.195,317.93 213.90297,314.559 215.21697,314.559

        #z0 = P(0, -0)
        #c0 = P(2.70263, -3.21793)
        #c1 = P(-3.18911, -14.0144)
        #z1 = P(-6.83542, -14.0144)
        #c2 = P(-8.19679, -13.8712)
        #c3 = P(-4.77204, -12.682)
        z2 = P(-4.30849, -12.682)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.70263, -3.21793)
        #z1 = z0 + P(-6.83542, -14.0144)
        #c1 = z1 + P(3.64631, 0)
        #c2 = z1 + P(-1.36137, 0.143228)
        #z2 = z1 + P(2.52694, 1.33244)
        #c3 = z2 + P(-0.46355, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20229, -49)
        z1 = z0 + PP(15.5926, -116)
        #z1 = z2 - PP(2.85671, ta + 27)
        c1 = z1 + PP(3.64631, 0)
        c2 = z1 + PP(1.36888, 173)
        z2 = z1 + PP(2.85671, 27)
        c3 = z2 + PP(0.46355, 180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_nerSWRCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRer(cls, ta=30, **kwargs):
        #M 167.822,341.867 C 167.822,353.824 158.46959,381.60486 148.09459,381.60486 144.21527,381.26234 153.58447,378.49731 154.78413,377.95076

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-3.287, -13.9663)
        #z1 = P(-6.93339, -13.9663)
        #c2 = P(-8.29682, -13.8459)
        #c3 = P(-5.00392, -12.8741)
        z2 = P(-4.58229, -12.682)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-6.93339, -13.9663)
        #c1 = z1 + P(3.6464, 0)
        #c2 = z1 + P(-1.36343, 0.120382)
        #z2 = z1 + P(2.3511, 1.28427)
        #c3 = z2 + P(-0.421632, -0.19209)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.5926, -116)
        #z1 = z2 - PP(2.679, ta + 363)
        c1 = z1 + PP(3.6464, 0)
        c2 = z1 + PP(1.36873, 174)
        #z2 = z1 + PP(2.679, 28)
        #c3 = z2 + PP(0.463328, -155)
        c3 = z2 + PP(0.463328, ta-180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            #endknot(*z2, angle=ta)])
            endknot(*z2)])

    @classmethod
    def path_SWRCRel(cls, ta=None, **kwargs):
        #M 124.589,341.867 C 124.589,353.824 113.059,381.387 102.683,381.387 100.127,381.387 100.88241,377.6417 101.76224,378.19318 102.78204,378.8324 104.27785,379.93595 105.457,380.783

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-4.05233, -13.8897)
        #z1 = P(-7.69908, -13.8897)
        #c2 = P(-8.59741, -13.8897)
        #c3 = P(-8.33192, -12.5734)
        #z2 = P(-8.02269, -12.7672)
        #c4 = P(-7.66427, -12.9919)
        #c5 = P(-7.13855, -13.3797)
        z3 = P(-6.72413, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-7.69908, -13.8897)
        #c1 = z1 + P(3.64675, 0)
        #c2 = z1 + P(-0.898331, 0)
        #z2 = z1 + P(-0.32361, 1.1225)
        #c3 = z2 + P(-0.309225, 0.193823)
        #c4 = z2 + P(0.358419, -0.22466)
        #z3 = z2 + P(1.29856, -0.910218)
        #c5 = z3 + P(-0.414424, 0.297704)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64675, 0)
        c2 = z1 + PP(0.898331, 180)
        #z2 = z1 + PP(1.16822, 106)
        z2 = z3 - PP(1.5858, ta + 1)
        c3 = z2 + PP(0.364949, 147)
        #c4 = z2 + PP(0.423009, -32)
        #z3 = z2 + PP(1.5858, -35)
        #c5 = z3 + PP(0.510269, 144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRe(cls, ta=None, **kwargs):
        #M 70.0186,341.867 C 70.0186,353.824 58.4877,381.387 48.1125,381.387 45.5562,381.387 46.100166,379.28724 46.97398,379.28248 49.034522,379.27124 52.120369,379.19719 53.399166,379.2425

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-4.05265, -13.8897)
        #z1 = P(-7.69912, -13.8897)
        #c2 = P(-8.59755, -13.8897)
        #c3 = P(-8.40637, -13.1517)
        #z2 = P(-8.09926, -13.15)
        #c4 = P(-7.37506, -13.1461)
        #c5 = P(-6.29051, -13.1201)
        z3 = P(-5.84106, -13.136)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-7.69912, -13.8897)
        #c1 = z1 + P(3.64647, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(-0.400144, 0.739654)
        #c3 = z2 + P(-0.307111, -0.00167295)
        #c4 = z2 + P(0.724198, 0.00395041)
        #z3 = z2 + P(2.2582, 0.0140514)
        #c5 = z3 + P(-0.449446, 0.0159246)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64647, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(0.840954, 118)
        z2 = z3 - PP(2.25824, ta + 3)
        c3 = z2 + PP(0.307115, -179)
        #c4 = z2 + PP(0.724209, 0)
        #z3 = z2 + PP(2.25824, 0)
        #c5 = z3 + PP(0.449728, 177)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRner(cls, ta=None, **kwargs):
        #M 151.651,437.476 C 151.651,449.433 144.38607,478.26357 140.68854,476.16663 138.55908,474.95897 143.9208,471.10881 145.13569,469.82839

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-2.55333, -14.3352)
        #z1 = P(-3.85286, -13.5982)
        #c2 = P(-4.60128, -13.1738)
        #c3 = P(-2.71686, -11.8206)
        z2 = P(-2.28987, -11.3706)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-3.85286, -13.5982)
        #c1 = z1 + P(1.29953, -0.73699)
        #c2 = z1 + P(-0.74842, 0.424444)
        #z2 = z1 + P(1.56299, 2.22764)
        #c3 = z2 + P(-0.426985, -0.450016)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(14.1335, -105)
        #z1 = z2 - PP(2.72127, ta + 367)
        c1 = z1 + PP(1.49397, -29)
        #c2 = z1 + PP(0.860398, 150)
        #z2 = z1 + PP(2.72127, 54)
        #c3 = z2 + PP(0.620347, -133)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_SWRCRne(cls, ta=None, **kwargs):
        #M 211.413,199.646 C 211.413,211.558 197.57787,239.82079 190.92697,239.46399 188.38363,239.32755 191.8304,237.05479 193.0434,236.29679 194.7334,235.23979 196.526,234.347 198.179,233.232

        #z0 = P(0, -0)
        #c0 = P(0, -4.20229)
        #c1 = P(-4.88073, -14.1728)
        #z1 = P(-7.22702, -14.0469)
        #c2 = P(-8.12425, -13.9988)
        #c3 = P(-6.90831, -13.197)
        #z2 = P(-6.48039, -12.9296)
        #c4 = P(-5.88419, -12.5567)
        #c5 = P(-5.2518, -12.2417)
        z3 = P(-4.66866, -11.8484)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20229)
        #z1 = z0 + P(-7.22702, -14.0469)
        #c1 = z1 + P(2.34629, -0.125871)
        #c2 = z1 + P(-0.897234, 0.048133)
        #z2 = z1 + P(0.746629, 1.11732)
        #c3 = z2 + P(-0.427919, -0.267406)
        #c4 = z2 + P(0.596194, 0.372886)
        #z3 = z2 + P(1.81173, 1.08119)
        #c5 = z3 + P(-0.583142, -0.393347)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20229, -90)
        z1 = z0 + PP(15.797, -117)
        c1 = z1 + PP(2.34966, -3)
        c2 = z1 + PP(0.898524, 176)
        #z2 = z1 + PP(1.34382, 56)
        z2 = z3 - PP(2.10982, ta + 355)
        c3 = z2 + PP(0.5046, -147)
        #c4 = z2 + PP(0.703201, 32)
        #z3 = z2 + PP(2.10982, 30)
        #c5 = z3 + PP(0.703403, -145)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRnel(cls, ta=None, **kwargs):
        #M 342.858,199.646 C 342.858,211.558 334.10045,244.55269 326.3164,239.84214 324.25363,238.59385 326.62543,238.34672 328.55529,237.89639 330.48515,237.44606 331.97309,236.79252 332.46393,236.53197

        #z0 = P(0, -0)
        #c0 = P(0, -4.20229)
        #c1 = P(-3.08947, -15.8421)
        #z1 = P(-5.83551, -14.1803)
        #c2 = P(-6.56321, -13.7399)
        #c3 = P(-5.72649, -13.6528)
        #z2 = P(-5.04568, -13.4939)
        #c4 = P(-4.36487, -13.335)
        #c5 = P(-3.83995, -13.1045)
        z3 = P(-3.6668, -13.0126)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20229)
        #z1 = z0 + P(-5.83551, -14.1803)
        #c1 = z1 + P(2.74604, -1.66178)
        #c2 = z1 + P(-0.727699, 0.440369)
        #z2 = z1 + P(0.789831, 0.686417)
        #c3 = z2 + P(-0.680812, -0.158866)
        #c4 = z2 + P(0.680812, 0.158866)
        #z3 = z2 + P(1.37888, 0.481337)
        #c5 = z3 + P(-0.173157, -0.0919162)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20229, -90)
        z1 = z0 + PP(15.3341, -112)
        c1 = z1 + PP(3.20971, -31)
        c2 = z1 + PP(0.850571, 148)
        z2 = z1 + PP(1.04642, 40)
        #z2 = z3 - PP(1.46048, ta + 351)
        c3 = z2 + PP(0.699102, -166)
        #c4 = z2 + PP(0.699102, 13)
        #z3 = z2 + PP(1.46048, 19)
        #c5 = z3 + PP(0.196041, -152)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRsw(cls, ta=None, **kwargs):
        #M 70.0186,749.352 C 70.0186,761.31 58.4877,788.872 48.1125,788.872 45.5562,788.872 50.44799,783.97889 51.694249,784.44465 53.019489,784.93993 51.270729,787.24852 50.8858,788.268

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05265, -13.8897)
        #z1 = P(-7.69912, -13.8897)
        #c2 = P(-8.59755, -13.8897)
        #c3 = P(-6.87828, -12.17)
        #z2 = P(-6.44027, -12.3337)
        #c4 = P(-5.97451, -12.5077)
        #c5 = P(-6.58912, -13.3191)
        z3 = P(-6.72441, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.69912, -13.8897)
        #c1 = z1 + P(3.64647, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(1.25884, 1.55604)
        #c3 = z2 + P(-0.43801, 0.163696)
        #c4 = z2 + P(0.465769, -0.174071)
        #z3 = z2 + P(-0.284137, -1.34375)
        #c5 = z3 + P(0.135287, 0.358306)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64647, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(2.00148, 51)
        z2 = z3 - PP(1.37347, ta + 10)
        c3 = z2 + PP(0.467599, 159)
        #c4 = z2 + PP(0.497234, -20)
        #z3 = z2 + PP(1.37347, -101)
        #c5 = z3 + PP(0.382996, 69)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])
        
    @classmethod
    def path_SWRCRswr(cls, ta=None, **kwargs):
        #M 112.207,749.352 C 112.207,761.31 100.677,788.872 90.3014,788.872 87.7451,788.872 90.312972,785.14079 91.559324,785.60657 92.884571,786.10183 92.878673,787.39376 93.0747,788.268

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05233, -13.8897)
        #z1 = P(-7.69894, -13.8897)
        #c2 = P(-8.59738, -13.8897)
        #c3 = P(-7.69487, -12.5783)
        #z2 = P(-7.25683, -12.742)
        #c4 = P(-6.79106, -12.9161)
        #c5 = P(-6.79313, -13.3702)
        z3 = P(-6.72424, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.69894, -13.8897)
        #c1 = z1 + P(3.64661, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(0.44211, 1.14767)
        #c3 = z2 + P(-0.438043, 0.163703)
        #c4 = z2 + P(0.465771, -0.174064)
        #z3 = z2 + P(0.532594, -0.935386)
        #c5 = z3 + P(-0.0688956, 0.30726)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8807, -118)
        c1 = z1 + PP(3.64661, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(1.22988, 68)
        z2 = z3 - PP(1.07638, ta + 18)
        c3 = z2 + PP(0.467632, 159)
        #c4 = z2 + PP(0.497233, -20)
        #z3 = z2 + PP(1.07638, -60)
        #c5 = z3 + PP(0.31489, 102)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])
    
    @classmethod
    def path_SWRCRswl(cls, ta=None, *kwargs):
        #M 148.374,749.352 C 148.374,761.31 136.843,788.872 126.468,788.872 123.911,788.872 129.60223,784.63241 130.84846,785.09823 132.17333,785.59344 131.29588,787.539 129.241,788.268

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05268, -13.8897)
        #z1 = P(-7.69908, -13.8897)
        #c2 = P(-8.59776, -13.8897)
        #c3 = P(-6.59752, -12.3996)
        #z2 = P(-6.15952, -12.5634)
        #c4 = P(-5.69389, -12.7374)
        #c5 = P(-6.00227, -13.4212)
        z3 = P(-6.72448, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.69908, -13.8897)
        #c1 = z1 + P(3.6464, 0)
        #c2 = z1 + P(-0.898683, 0)
        #z2 = z1 + P(1.53956, 1.32633)
        #c3 = z2 + P(-0.438, 0.163717)
        #c4 = z2 + P(0.465639, -0.174046)
        #z3 = z2 + P(-0.564958, -1.11405)
        #c5 = z3 + P(0.722208, 0.256214)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.6464, 0)
        c2 = z1 + PP(0.898683, 180)
        #z2 = z1 + PP(2.03209, 40)
        z2 = z3 - PP(1.24911, ta + 45)
        c3 = z2 + PP(0.467597, 159)
        #c4 = z2 + PP(0.497103, -20)
        #z3 = z2 + PP(1.24911, -116)
        #c5 = z3 + PP(0.766309, 19)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRse(cls, ta=None, **kwargs):
        #M 70.0186,636.793 C 70.0186,648.75 58.4877,676.313 48.1125,676.313 45.5562,676.313 47.586664,671.77958 48.571609,672.39399 49.576814,673.02104 50.181437,674.32642 50.8858,675.709

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-4.05265, -13.8897)
        #z1 = P(-7.69912, -13.8897)
        #c2 = P(-8.59755, -13.8897)
        #c3 = P(-7.88393, -12.2964)
        #z2 = P(-7.53776, -12.5123)
        #c4 = P(-7.18447, -12.7327)
        #c5 = P(-6.97197, -13.1915)
        z3 = P(-6.72441, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-7.69912, -13.8897)
        #c1 = z1 + P(3.64647, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(0.161358, 1.37737)
        #c3 = z2 + P(-0.346169, 0.21594)
        #c4 = z2 + P(0.353289, -0.220383)
        #z3 = z2 + P(0.813345, -1.16509)
        #c5 = z3 + P(-0.247555, 0.485921)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64647, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(1.38679, 83)
        z2 = z3 - PP(1.42091, ta + 9)
        c3 = z2 + PP(0.407999, 148)
        #c4 = z2 + PP(0.416392, -31)
        #z3 = z2 + PP(1.42091, -55)
        #c5 = z3 + PP(0.545347, 116)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRser(cls, ta=None, **kwargs):
        #M 107.582,636.793 C 107.582,648.75 96.0507,676.313 85.6755,676.313 83.1192,676.313 83.363089,673.45365 84.6096,673.919 85.934695,674.41369 87.2361,674.98 88.4488,675.709

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-4.05279, -13.8897)
        #z1 = P(-7.69926, -13.8897)
        #c2 = P(-8.59769, -13.8897)
        #c3 = P(-8.51198, -12.8847)
        #z2 = P(-8.07388, -13.0483)
        #c4 = P(-7.60816, -13.2222)
        #c5 = P(-7.15077, -13.4212)
        z3 = P(-6.72455, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-7.69926, -13.8897)
        #c1 = z1 + P(3.64647, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(-0.374621, 0.841395)
        #c3 = z2 + P(-0.438099, 0.163552)
        #c4 = z2 + P(0.465718, -0.173864)
        #z3 = z2 + P(1.34932, -0.629113)
        #c5 = z3 + P(-0.426215, 0.256214)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.8809, -119)
        c1 = z1 + PP(3.64647, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(0.921025, 114)
        z2 = z3 - PP(1.48878, ta + 8)
        c3 = z2 + PP(0.467632, 159)
        #c4 = z2 + PP(0.497113, -20)
        #z3 = z2 + PP(1.48878, -24)
        #c5 = z3 + PP(0.497298, 148)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRsel(cls, ta=None, **kwargs):
        #M 150.814,636.793 C 150.814,648.75 139.283,676.313 128.908,676.313 126.351,676.313 130.58968,672.21907 131.83607,672.68447 133.16078,673.17911 131.70253,674.18119 131.681,675.709

        #z0 = P(0, -0)
        #c0 = P(0, -4.20241)
        #c1 = P(-4.05268, -13.8897)
        #z1 = P(-7.69908, -13.8897)
        #c2 = P(-8.59776, -13.8897)
        #c3 = P(-7.10804, -12.4508)
        #z2 = P(-6.66998, -12.6144)
        #c4 = P(-6.2044, -12.7883)
        #c5 = P(-6.71691, -13.1404)
        z3 = P(-6.72448, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20241)
        #z1 = z0 + P(-7.69908, -13.8897)
        #c1 = z1 + P(3.6464, 0)
        #c2 = z1 + P(-0.898683, 0)
        #z2 = z1 + P(1.0291, 1.27528)
        #c3 = z2 + P(-0.438056, 0.163569)
        #c4 = z2 + P(0.465582, -0.173846)
        #z3 = z2 + P(-0.0545009, -1.063)
        #c5 = z3 + P(0.00756693, 0.536964)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20241, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.6464, 0)
        c2 = z1 + PP(0.898683, 180)
        #z2 = z1 + PP(1.63872, 51)
        z2 = z3 - PP(1.0644, ta + -1)
        c3 = z2 + PP(0.467598, 159)
        #c4 = z2 + PP(0.49698, -20)
        #z3 = z2 + PP(1.0644, -92)
        #c5 = z3 + PP(0.537017, 89)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRsl(cls, ta=None, **kwargs):
        #M 116.085,518.507 C 116.085,530.465 104.555,558.027 94.1795,558.027 91.6232,558.027 96.442271,554.22318 97.688529,554.68894 99.013769,555.18422 97.700827,555.9678 96.9527,557.423

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05233, -13.8897)
        #z1 = P(-7.6989, -13.8897)
        #c2 = P(-8.59734, -13.8897)
        #c3 = P(-6.90363, -12.5528)
        #z2 = P(-6.46562, -12.7165)
        #c4 = P(-5.99985, -12.8906)
        #c5 = P(-6.4613, -13.166)
        z3 = P(-6.72424, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.6989, -13.8897)
        #c1 = z1 + P(3.64657, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(1.23328, 1.17319)
        #c3 = z2 + P(-0.43801, 0.163696)
        #c4 = z2 + P(0.465769, -0.174071)
        #z3 = z2 + P(-0.258614, -0.960912)
        #c5 = z3 + P(0.262937, 0.511444)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8807, -118)
        c1 = z1 + PP(3.64657, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(1.70217, 43)
        z2 = z3 - PP(0.995105, ta + 13)
        c3 = z2 + PP(0.467599, 159)
        #c4 = z2 + PP(0.497234, -20)
        #z3 = z2 + PP(0.995105, -105)
        #c5 = z3 + PP(0.575075, 62)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])
    
    @classmethod
    def path_SWRCRsr(cls,ta=None, **kwargs):
        #M 162.152,518.507 C 162.152,530.465 150.622,558.027 140.246,558.027 137.69,558.027 138.01398,555.04476 139.32524,555.2699 140.94152,555.54742 142.38796,556.3309 143.02,557.423

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05233, -13.8897)
        #z1 = P(-7.69908, -13.8897)
        #c2 = P(-8.59741, -13.8897)
        #c3 = P(-8.48355, -12.8416)
        #z2 = P(-8.02269, -12.9207)
        #c4 = P(-7.45463, -13.0182)
        #c5 = P(-6.94627, -13.2936)
        z3 = P(-6.72413, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.69908, -13.8897)
        #c1 = z1 + P(3.64675, 0)
        #c2 = z1 + P(-0.898331, 0)
        #z2 = z1 + P(-0.32361, 0.96901)
        #c3 = z2 + P(-0.460855, 0.0791277)
        #c4 = z2 + P(0.568058, -0.0975371)
        #z3 = z2 + P(1.29856, -0.756728)
        #c5 = z3 + P(-0.222137, 0.383829)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64675, 0)
        c2 = z1 + PP(0.898331, 180)
        #z2 = z1 + PP(1.02162, 108)
        z2 = z3 - PP(1.50296, ta + 30)
        c3 = z2 + PP(0.467599, 170)
        #c4 = z2 + PP(0.57637, -9)
        #z3 = z2 + PP(1.50296, -30)
        #c5 = z3 + PP(0.443475, 120)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCRs(cls, ta=None, **kwargs):
        #M 70.0186,518.507 C 70.0186,530.465 58.4877,558.027 48.1125,558.027 45.5562,558.027 48.673889,553.8023 49.920148,554.26806 51.245388,554.76334 50.836839,556.40906 50.8858,557.423

        #z0 = P(0, -0)
        #c0 = P(0, -4.20276)
        #c1 = P(-4.05265, -13.8897)
        #z1 = P(-7.69912, -13.8897)
        #c2 = P(-8.59755, -13.8897)
        #c3 = P(-7.50181, -12.4049)
        #z2 = P(-7.0638, -12.5686)
        #c4 = P(-6.59803, -12.7426)
        #c5 = P(-6.74162, -13.3211)
        z3 = P(-6.72441, -13.6774)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20276)
        #z1 = z0 + P(-7.69912, -13.8897)
        #c1 = z1 + P(3.64647, 0)
        #c2 = z1 + P(-0.898437, 0)
        #z2 = z1 + P(0.635316, 1.32112)
        #c3 = z2 + P(-0.43801, 0.163696)
        #c4 = z2 + P(0.465769, -0.174071)
        #z3 = z2 + P(0.339388, -1.10883)
        #c5 = z3 + P(-0.0172078, 0.356359)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20276, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64647, 0)
        c2 = z1 + PP(0.898437, 180)
        #z2 = z1 + PP(1.46594, 64)
        z2 = z3 - PP(1.15961, ta + 16)
        c3 = z2 + PP(0.467599, 159)
        #c4 = z2 + PP(0.497234, -20)
        #z3 = z2 + PP(1.15961, -72)
        #c5 = z3 + PP(0.356774, 92)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SWRCR(cls, ta=None, **kwargs):
        #M24.000000 -0.000000C24.000000 12.001999,11.736954 39.278046,1.322876 39.278046C-1.243011 39.278046,-1.032211 36.431870,0.222641 36.888626C1.557022 37.374329,2.846466 37.975586,4.076248 38.685608

        #z0 = P(0, -0)
        #c0 = P(0, -4.21822)
        #c1 = P(-4.30997, -13.8047)
        #z1 = P(-7.9701, -13.8047)
        #c2 = P(-8.87191, -13.8047)
        #c3 = P(-8.79782, -12.8043)
        #z2 = P(-8.35679, -12.9649)
        #c4 = P(-7.88781, -13.1356)
        #c5 = P(-7.43462, -13.3469)
        #z3 = P(-7.0024, -13.5964)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.21822)
        #z1 = z0 + P(-7.9701, -13.8047)
        #c1 = z1 + P(3.66013, 0)
        #c2 = z1 + P(-0.901806, 0)
        #z2 = z1 + P(-0.386688, 0.839785)
        #c3 = z2 + P(-0.44103, 0.160531)
        #c4 = z2 + P(0.468981, -0.170705)
        #z3 = z2 + P(1.35439, -0.631567)
        #c5 = z3 + P(-0.432219, 0.249544)

        z0 = P(0, -0)
        c0 = z0 + PP(4.21822, -90)
        z1 = z0 + PP(15.9402, -119)
        c1 = z1 + PP(3.66013, 0)
        c2 = z1 + PP(0.901806, 180)
        z2 = z1 + PP(0.924536, 114)
        c3 = z2 + PP(0.469338, 159)
        c4 = z2 + PP(0.499083, -20)
        z3 = z2 + PP(1.4944, -25)
        c5 = z3 + PP(0.499085, 149)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            endknot(*z3)])

    @classmethod
    def path_selNELCL(cls, ta=None, **kwargs):
        #M 138.79,1506.89 C 148.71205,1506.89 171.231,1487.86 171.231,1478.69 171.231,1475.72 167.115,1475.76 168.021,1477.21 168.941,1478.64 170.04789,1480.3707 170.60389,1481.4507

        #z0 = P(0, -0)
        #c0 = P(3.50028, -0)
        #c1 = P(11.4445, 6.71336)
        #z1 = P(11.4445, 9.94833)
        #c2 = P(11.4445, 10.9961)
        #c3 = P(9.99243, 10.982)
        #z2 = P(10.312, 10.4704)
        #c4 = P(10.6366, 9.96597)
        #c5 = P(11.0271, 9.35542)
        z3 = P(11.2232, 8.97442)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.50028, 0)
        #z1 = z0 + P(11.4445, 9.94833)
        #c1 = z1 + P(0, -3.23497)
        #c2 = z1 + P(0, 1.04775)
        #z2 = z1 + P(-1.13242, 0.522111)
        #c3 = z2 + P(-0.319617, 0.511528)
        #c4 = z2 + P(0.324556, -0.504472)
        #z3 = z2 + P(0.911186, -1.49602)
        #c5 = z3 + P(-0.196144, 0.381)

        z0 = P(0, -0)
        c0 = z0 + PP(3.50028, 0)
        z1 = z0 + PP(15.1639, 40)
        c1 = z1 + PP(3.23497, -90)
        c2 = z1 + PP(1.04775, 90)
        z2 = z1 + PP(1.24698, 155)
        #z2 = z3 - PP(1.75167, ta + 5)
        c3 = z2 + PP(0.603171, 121)
        c4 = z2 + PP(0.599857, -57)
        #z3 = z2 + PP(1.75167, -58)
        c5 = z3 + PP(0.428525, 117)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_NELCLNE(cls, ta=None, **kwargs):
        #M 332.847,89.3562 C 341.32,84.2653 365.653,70.9615 365.653,61.8293 365.653,60.3511 364.38594,60.300424 363.5643,60.4478 362.47814,60.642626 361.30411,62.5446 361.61001,63.119904 362.22621,64.278794 364.36527,62.627304 365.653,61.8293 367.00954,60.988659 368.09287,60.428362 369.14916,59.693917

        #z0 = P(0, -0)
        #c0 = P(2.98909, 1.79596)
        #c1 = P(11.5732, 6.48924)
        #z1 = P(11.5732, 9.71088)
        #c2 = P(11.5732, 10.2324)
        #c3 = P(11.1262, 10.2502)
        #z2 = P(10.8364, 10.1982)
        #c4 = P(10.4532, 10.1295)
        #c5 = P(10.039, 9.45854)
        #z3 = P(10.147, 9.25558)
        #c6 = P(10.3643, 8.84675)
        #c7 = P(11.1189, 9.42936)
        #z4 = P(11.5732, 9.71088)
        #c8 = P(12.0518, 10.0074)
        #c9 = P(12.434, 10.2051)
        #z5 = P(12.8066, 10.4642)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.98909, 1.79596)
        #z1 = z0 + P(11.5732, 9.71088)
        #c1 = z1 + P(0, -3.22164)
        #c2 = z1 + P(0, 0.521476)
        #z2 = z1 + P(-0.736847, 0.487363)
        #c3 = z2 + P(0.289856, 0.051991)
        #c4 = z2 + P(-0.383173, -0.0687303)
        #z3 = z2 + P(-0.68943, -0.942659)
        #c5 = z3 + P(-0.107915, 0.202954)
        #c6 = z3 + P(0.217382, -0.408831)
        #z4 = z3 + P(1.42628, 0.455296)
        #c7 = z4 + P(-0.454283, -0.281518)
        #c8 = z4 + P(0.478557, 0.296559)
        #z5 = z4 + P(1.23337, 0.753316)
        #c9 = z5 + P(-0.372636, -0.259096)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48713, 30)
        z1 = z0 + PP(15.1076, 39)
        c1 = z1 + PP(3.22164, -90)
        c2 = z1 + PP(0.521476, 90)
        z2 = z1 + PP(0.88344, 146)
        c3 = z2 + PP(0.294482, 10)
        c4 = z2 + PP(0.389288, -169)
        z3 = z2 + PP(1.16787, -126)
        c5 = z3 + PP(0.229861, 118)
        c6 = z3 + PP(0.463031, -61)
        z4 = z3 + PP(1.49718, 17)
        #z4 = z5 - PP(1.44523, ta + 356)
        c7 = z4 + PP(0.534439, -148)
        c8 = z4 + PP(0.562996, 31)
        z5 = z4 + PP(1.44523, 31)
        c9 = z5 + PP(0.453859, -145)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_selNELCLNE(cls, ta=None, **kwargs):
        #M 369.356,147.216 C 376.97839,147.216 402.162,128.8213 402.162,119.6891 402.162,118.2109 400.89494,118.16023 400.0733,118.3076 398.98714,118.50243 397.81311,120.4044 398.11901,120.97971 398.73521,122.1386 400.87427,120.48711 402.162,119.6891 403.51854,118.84846 404.60187,118.28816 405.65816,117.55372

        #z0 = P(0, -0)
        #c0 = P(2.68901, -0)
        #c1 = P(11.5732, 6.48924)
        #z1 = P(11.5732, 9.71088)
        #c2 = P(11.5732, 10.2324)
        #c3 = P(11.1262, 10.2502)
        #z2 = P(10.8364, 10.1982)
        #c4 = P(10.4532, 10.1295)
        #c5 = P(10.039, 9.45854)
        #z3 = P(10.147, 9.25558)
        #c6 = P(10.3643, 8.84675)
        #c7 = P(11.1189, 9.42936)
        #z4 = P(11.5732, 9.71088)
        #c8 = P(12.0518, 10.0074)
        #c9 = P(12.434, 10.2051)
        #z5 = P(12.8066, 10.4642)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.68901, 0)
        #z1 = z0 + P(11.5732, 9.71088)
        #c1 = z1 + P(0, -3.22164)
        #c2 = z1 + P(0, 0.521476)
        #z2 = z1 + P(-0.736847, 0.487363)
        #c3 = z2 + P(0.289856, 0.0519889)
        #c4 = z2 + P(-0.383173, -0.0687317)
        #z3 = z2 + P(-0.68943, -0.942661)
        #c5 = z3 + P(-0.107915, 0.202957)
        #c6 = z3 + P(0.217382, -0.408831)
        #z4 = z3 + P(1.42628, 0.455299)
        #c7 = z4 + P(-0.454283, -0.28152)
        #c8 = z4 + P(0.478557, 0.296559)
        #z5 = z4 + P(1.23337, 0.753315)
        #c9 = z5 + P(-0.372636, -0.259094)

        z0 = P(0, -0)
        c0 = z0 + PP(2.68901, 0)
        z1 = z0 + PP(15.1076, 39)
        c1 = z1 + PP(3.22164, -90)
        c2 = z1 + PP(0.521476, 90)
        z2 = z1 + PP(0.88344, 146)
        c3 = z2 + PP(0.294482, 10)
        c4 = z2 + PP(0.389289, -169)
        z3 = z2 + PP(1.16787, -126)
        c5 = z3 + PP(0.229863, 118)
        c6 = z3 + PP(0.463031, -61)
        z4 = z3 + PP(1.49718, 17)
        #z4 = z5 - PP(1.44523, ta + 356)
        c7 = z4 + PP(0.53444, -148)
        c8 = z4 + PP(0.562996, 31)
        z5 = z4 + PP(1.44523, 31)
        c9 = z5 + PP(0.453858, -145)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCRNE(cls, ta=None, **kwargs):
        #M 354.182,237.273 C 354.182,249.185 342.695,276.645 332.358,276.645 329.812,276.645 334.41234,274.40912 335.683,273.659 337.63898,272.50431 339.9458,271.40226 341.6496,270.36777 343.16741,269.44622 344.46726,268.84261 345.96063,267.98507

        #z0 = P(0, -0)
        #c0 = P(0, -4.20229)
        #c1 = P(-4.05236, -13.8896)
        #z1 = P(-7.69902, -13.8896)
        #c2 = P(-8.59719, -13.8896)
        #c3 = P(-6.9743, -13.1008)
        #z2 = P(-6.52604, -12.8362)
        #c4 = P(-5.83601, -12.4288)
        #c5 = P(-5.02221, -12.04)
        #z3 = P(-4.42115, -11.6751)
        #c6 = P(-3.8857, -11.35)
        #c7 = P(-3.42714, -11.1371)
        #z4 = P(-2.90032, -10.8345)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20229)
        #z1 = z0 + P(-7.69902, -13.8896)
        #c1 = z1 + P(3.64666, 0)
        #c2 = z1 + P(-0.898172, 0)
        #z2 = z1 + P(1.17299, 1.05339)
        #c3 = z2 + P(-0.448261, -0.264626)
        #c4 = z2 + P(0.690026, 0.407349)
        #z3 = z2 + P(2.10488, 1.16107)
        #c5 = z3 + P(-0.601063, -0.364945)
        #c6 = z3 + P(0.53545, 0.325102)
        #z4 = z3 + P(1.52084, 0.840564)
        #c7 = z4 + P(-0.526828, -0.302521)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20229, -90)
        z1 = z0 + PP(15.8806, -118)
        c1 = z1 + PP(3.64666, 0)
        c2 = z1 + PP(0.898172, 180)
        z2 = z1 + PP(1.57656, 41)
        c3 = z2 + PP(0.520542, -149)
        c4 = z2 + PP(0.801292, 30)
        z3 = z2 + PP(2.40388, 28)
        #z3 = z4 - PP(1.73767, ta + 358)
        c5 = z3 + PP(0.703179, -148)
        c6 = z3 + PP(0.626417, 31)
        z4 = z3 + PP(1.73767, 28)
        c7 = z4 + PP(0.607508, -150)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    def to_reverse(self):
        if self.before:
            to_reverse = self.before.tail_type in {
                'ER', 'ERCL1', 'ERCL4', 'E', 'ECL1', 'ECL4', 'ELCL4', 
                'NER', 'NE', 'NECL1', 'NECL4', 'NECL4', 'NELCL4'}
            to_reverse = to_reverse and self.before.model != 'ER4' 
            to_reverse = to_reverse and self.before.model != 'ER8SWR4'
        else:
            to_reverse = False
        
        return to_reverse

    def get_paths(self):
        if self.to_reverse():
            if self.tail_type.endswith('F'):
                self.model = 'SWR16CR1NE1F'
                return [self.path_SWRCRNE()]

            self.head_type = 'SWR'
            self.tail_type = 'SWRCR1'
            self.model = 'SWR16CR1'

            self.head_ligature = {'ER', 'NER'}
            self.tail_ligature = {'ER', 'EL', 'E', 'NER', 'NE', 'NEL', 
                                  'SW', 'S', 'SL', 'SR', 'SE', 'SER', 
                                  'SEL', 'SWR', 'SWL'}
            self.both_ligature = {}
        else:
            if self.tail_type.endswith('F'):
                self.model = 'NEL16CL1NE1F'
                if (getattr(self.before, 'tail_type', '') == 'SEL'):
                    return [self.path_selNELCLNE()]
                else:
                    return [self.path_NELCLNE()]
                

            self.head_type = 'NEL'
            self.tail_type = 'NEL16CL1'
            self.model = 'NEL16CL1'

            self.head_ligature = {'EL', 'SWL', 'SL', 'SEL'}
            self.tail_ligature = {'ER', 'E', 'EL', 'NE', 'NER', 'NEL',
                                  'SW', 'SWL', 'S', 'SL', 'SER', 'SEL', 'SR',
                                  'SE', 'SWR', 'SE', 'SER'}
            self.both_ligature = {}

        return super().get_paths()

class CharSen(CharSe):
    def __init__(self, name='sen', kana='せん',
                 model='NEL16CL1NE1F|SWR16CR1NE1F', head_type='NEL|SWR',
                 tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSeku(CharSe):
    def __init__(self, name='seku', kana='せく',
                 model='BNEL16CL1|BSWR16CR1', head_type='BNEL|BSWR',
                 tail_type='NELCL1|SWRCR1'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

    def set_next_head(self, flick_len=2.0, dz=P(0, 0)):
        if getattr(self.before, 'tail_type', '') not in self.barbs:
            self.head = self.before.tail - self.get_pos_xku()
        super().set_next_head(flick_len=flick_len, dz=dz)

class CharSesu(CharSe):
    def __init__(self, name='sesu', kana='せす',
                 model='NEL16CL1TS3|SWR16CR1TS3', head_type='NEL|SWR',
                 tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
    
    @classmethod
    def path_SWRCRTS(cls, ta=None, **kwargs):
        #M 595.811,105.717 C 595.811,117.63 584.9973,144.87662 574.677,145.464 572.69424,145.57685 572.4751,142.56 573.51828,141.83713 574.06834,141.45597 575.10463,142.3853 575.35775,143.08083 575.64028,143.85718 575.51508,145.27296 574.677,145.464 573.05566,145.83359 572.87433,142.10618 572.87433,140.05375 572.87433,142.88838 572.87433,145.723 572.87433,148.55763

        #z0 = P(0, -0)
        #c0 = P(0, -4.20264)
        #c1 = P(-3.81483, -13.8146)
        #z1 = P(-7.45561, -14.0219)
        #c2 = P(-8.15508, -14.0617)
        #c3 = P(-8.23239, -12.9974)
        #z2 = P(-7.86438, -12.7424)
        #c4 = P(-7.67033, -12.6079)
        #c5 = P(-7.30475, -12.9358)
        #z3 = P(-7.21545, -13.1811)
        #c6 = P(-7.11578, -13.455)
        #c7 = P(-7.15995, -13.9545)
        #z4 = P(-7.45561, -14.0219)
        #c8 = P(-8.02758, -14.1522)
        #c9 = P(-8.09155, -12.8373)
        #z5 = P(-8.09155, -12.1132)
        #c10 = P(-8.09155, -13.1132)
        #c11 = P(-8.09155, -14.1132)
        z6 = P(-8.09155, -15.1132)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -4.20264)
        #z1 = z0 + P(-7.45561, -14.0219)
        #c1 = z1 + P(3.64077, 0.207215)
        #c2 = z1 + P(-0.699474, -0.039811)
        #z2 = z1 + P(-0.408771, 1.27948)
        #c3 = z2 + P(-0.368011, -0.255012)
        #c4 = z2 + P(0.194049, 0.134465)
        #z3 = z2 + P(0.648924, -0.43875)
        #c5 = z3 + P(-0.0892951, 0.245368)
        #c6 = z3 + P(0.0996703, -0.273879)
        #z4 = z3 + P(-0.240153, -0.840729)
        #c7 = z4 + P(0.295656, 0.0673947)
        #c8 = z4 + P(-0.571973, -0.130383)
        #z5 = z4 + P(-0.635942, 1.90862)
        #c9 = z5 + P(0, -0.724052)
        #c10 = z5 + P(0, -0.999994)
        #z6 = z5 + P(0, -2.99998)
        #c11 = z6 + P(0, 0.999994)

        z0 = P(0, -0)
        c0 = z0 + PP(4.20264, -90)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64666, 3)
        c2 = z1 + PP(0.700606, -176)
        z2 = z1 + PP(1.34319, 107)
        c3 = z2 + PP(0.447731, -145)
        c4 = z2 + PP(0.236084, 34)
        z3 = z2 + PP(0.783329, -34)
        c5 = z3 + PP(0.261111, 109)
        c6 = z3 + PP(0.291451, -70)
        z4 = z3 + PP(0.874357, -105)
        c7 = z4 + PP(0.30324, 12)
        c8 = z4 + PP(0.586645, -167)
        z5 = z4 + PP(2.01177, 108)
        #z5 = z6 - PP(2.99998, ta + 0)
        c9 = z5 + PP(0.724052, -90)
        c10 = z5 + PP(0.999994, -90)
        z6 = z5 + PP(2.99998, -90)
        c11 = z6 + PP(0.999994, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

    @classmethod
    def path_SWRCRTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRTS(cls, ta=None, **kwargs):
        #M 362.685,297.589 C 368.41254,305.34239 351.874,336.795 341.551,337.336 339.57,337.475 339.399,334.423 340.438,333.695 340.993,333.321 342.038,334.237 342.279,334.937 342.562,335.713 342.478,337.152 341.638,337.331 340.017,337.705 339.875,333.96 339.875,331.907 339.87836,334.74502 340.36977,338.0711 339.875,340.411

        #z0 = P(0, -0)
        #c0 = P(2.02055, -2.73522)
        #c1 = P(-3.81388, -13.831)
        #z1 = P(-7.45561, -14.0219)
        #c2 = P(-8.15446, -14.0709)
        #c3 = P(-8.21478, -12.9942)
        #z2 = P(-7.84825, -12.7374)
        #c4 = P(-7.65246, -12.6055)
        #c5 = P(-7.2838, -12.9286)
        #z3 = P(-7.19878, -13.1755)
        #c6 = P(-7.09895, -13.4493)
        #c7 = P(-7.12858, -13.9569)
        #z4 = P(-7.42491, -14.0201)
        #c8 = P(-7.99677, -14.152)
        #c9 = P(-8.04686, -12.8309)
        #z5 = P(-8.04686, -12.1066)
        #c10 = P(-8.04568, -13.1078)
        #c11 = P(-7.87232, -14.2812)
        z6 = P(-8.04686, -15.1067)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.02055, -2.73522)
        #z1 = z0 + P(-7.45561, -14.0219)
        #c1 = z1 + P(3.64173, 0.190853)
        #c2 = z1 + P(-0.698853, -0.0490361)
        #z2 = z1 + P(-0.392642, 1.28446)
        #c3 = z2 + P(-0.366536, -0.256822)
        #c4 = z2 + P(0.195792, 0.131939)
        #z3 = z2 + P(0.649464, -0.43815)
        #c5 = z3 + P(-0.0850194, 0.246944)
        #c6 = z3 + P(0.0998361, -0.273756)
        #z4 = z3 + P(-0.226131, -0.84455)
        #c7 = z4 + P(0.296333, 0.0631472)
        #c8 = z4 + P(-0.571853, -0.131939)
        #z5 = z4 + P(-0.621947, 1.91347)
        #c9 = z5 + P(0, -0.724253)
        #c10 = z5 + P(0.00118533, -1.00119)
        #z6 = z5 + P(0, -3.00002)
        #c11 = z6 + P(0.174544, 0.825465)

        z0 = P(0, -0)
        c0 = z0 + PP(3.4006, -53)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64672, 2)
        c2 = z1 + PP(0.700571, -175)
        z2 = z1 + PP(1.34314, 106)
        c3 = z2 + PP(0.447556, -144)
        c4 = z2 + PP(0.236098, 33)
        z3 = z2 + PP(0.78344, -34)
        c5 = z3 + PP(0.26117, 108)
        c6 = z3 + PP(0.291392, -69)
        z4 = z3 + PP(0.8743, -104)
        c7 = z4 + PP(0.302987, 12)
        c8 = z4 + PP(0.586876, -167)
        z5 = z4 + PP(2.01201, 108)
        #z5 = z6 - PP(3.00002, ta + 12)
        c9 = z5 + PP(0.724253, -90)
        c10 = z5 + PP(1.00119, -89)
        z6 = z5 + PP(3.00002, -90)
        c11 = z6 + PP(0.843717, 78)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

    @classmethod
    def path_erSWRCRTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRTS(cls, ta=None, **kwargs):
        #M 348.469,815.985 C 355.85503,823.5339 337.658,855.191 327.335,855.732 325.354,855.871 325.182,852.819 326.222,852.091 326.777,851.717 327.822,852.633 328.063,853.333 328.345,854.109 328.262,855.548 327.421,855.727 325.801,856.101 325.659,852.356 325.659,850.303 325.67323,853.13767 326.10329,855.97233 325.659,858.807

        #z0 = P(0, -0)
        #c0 = P(2.60563, -2.66308)
        #c1 = P(-3.81388, -13.831)
        #z1 = P(-7.45561, -14.0219)
        #c2 = P(-8.15446, -14.0709)
        #c3 = P(-8.21514, -12.9942)
        #z2 = P(-7.84825, -12.7374)
        #c4 = P(-7.65246, -12.6055)
        #c5 = P(-7.2838, -12.9286)
        #z3 = P(-7.19878, -13.1755)
        #c6 = P(-7.0993, -13.4493)
        #c7 = P(-7.12858, -13.9569)
        #z4 = P(-7.42527, -14.0201)
        #c8 = P(-7.99677, -14.152)
        #c9 = P(-8.04686, -12.8309)
        #z5 = P(-8.04686, -12.1066)
        #c10 = P(-8.04184, -13.1066)
        #c11 = P(-7.89013, -14.1066)
        z6 = P(-8.04686, -15.1067)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.60563, -2.66308)
        #z1 = z0 + P(-7.45561, -14.0219)
        #c1 = z1 + P(3.64173, 0.190853)
        #c2 = z1 + P(-0.698853, -0.0490361)
        #z2 = z1 + P(-0.392642, 1.28446)
        #c3 = z2 + P(-0.366889, -0.256822)
        #c4 = z2 + P(0.195792, 0.131939)
        #z3 = z2 + P(0.649464, -0.43815)
        #c5 = z3 + P(-0.0850194, 0.246944)
        #c6 = z3 + P(0.0994833, -0.273756)
        #z4 = z3 + P(-0.226483, -0.84455)
        #c7 = z4 + P(0.296686, 0.0631472)
        #c8 = z4 + P(-0.5715, -0.131939)
        #z5 = z4 + P(-0.621594, 1.91347)
        #c9 = z5 + P(0, -0.724253)
        #c10 = z5 + P(0.00502003, -1.00001)
        #z6 = z5 + P(0, -3.00002)
        #c11 = z6 + P(0.156736, 1.00001)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72576, -45)
        z1 = z0 + PP(15.8808, -118)
        c1 = z1 + PP(3.64672, 2)
        c2 = z1 + PP(0.700571, -175)
        z2 = z1 + PP(1.34314, 106)
        c3 = z2 + PP(0.447845, -145)
        c4 = z2 + PP(0.236098, 33)
        z3 = z2 + PP(0.78344, -34)
        c5 = z3 + PP(0.26117, 108)
        c6 = z3 + PP(0.291271, -70)
        z4 = z3 + PP(0.874391, -105)
        c7 = z4 + PP(0.303332, 12)
        c8 = z4 + PP(0.586532, -167)
        z5 = z4 + PP(2.0119, 107)
        #z5 = z6 - PP(3.00002, ta + 9)
        c9 = z5 + PP(0.724253, -90)
        c10 = z5 + PP(1.00002, -89)
        z6 = z5 + PP(3.00002, -90)
        c11 = z6 + PP(1.01222, 81)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

    @classmethod
    def path_nerSWRCRTSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRCRTS())

    @classmethod
    def path_nerSWRCRTSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRCRTS())

    @classmethod
    def path_nerSWRCRTSswr(cls, ta=None, **kwargs):
        return cls.jog(cls.path_SWRCRTS())

    @classmethod
    def path_NELCLTS(cls, ta=None, **kwargs):
        #M 616.665,89.3562 C 625.226,84.4137 649.47,70.9615 649.47,61.8293 649.47,58.8729 647.15202,60.021442 646.75666,60.892743 646.16544,62.195662 646.71837,64.443125 647.95615,64.408545 649.88866,64.354556 649.5195,61.469612 649.5195,58.823416 649.5195,61.658041 649.5195,64.492666 649.5195,67.327291

        #z0 = P(0, -0)
        #c0 = P(3.02013, 1.7436)
        #c1 = P(11.5729, 6.48924)
        #z1 = P(11.5729, 9.71088)
        #c2 = P(11.5729, 10.7538)
        #c3 = P(10.7551, 10.3487)
        #z2 = P(10.6157, 10.0413)
        #c4 = P(10.4071, 9.58163)
        #c5 = P(10.6022, 8.78878)
        #z3 = P(11.0388, 8.80098)
        #c6 = P(11.7206, 8.82002)
        #c7 = P(11.5903, 9.83777)
        #z4 = P(11.5903, 10.7713)
        #c8 = P(11.5903, 9.77129)
        #c9 = P(11.5903, 8.7713)
        z5 = P(11.5903, 7.77131)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.02013, 1.7436)
        #z1 = z0 + P(11.5729, 9.71088)
        #c1 = z1 + P(0, -3.22164)
        #c2 = z1 + P(0, 1.04295)
        #z2 = z1 + P(-0.957206, 0.330396)
        #c3 = z2 + P(0.139474, 0.307376)
        #c4 = z2 + P(-0.208569, -0.459641)
        #z3 = z2 + P(0.423153, -1.2403)
        #c5 = z3 + P(-0.436661, -0.0121991)
        #c6 = z3 + P(0.681747, 0.0190461)
        #z4 = z3 + P(0.551515, 1.97031)
        #c7 = z4 + P(0, -0.933519)
        #c8 = z4 + P(0, -0.999993)
        #z5 = z4 + P(0, -2.99998)
        #c9 = z5 + P(0, 0.999993)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48731, 29)
        z1 = z0 + PP(15.1074, 40)
        c1 = z1 + PP(3.22164, -90)
        c2 = z1 + PP(1.04295, 90)
        z2 = z1 + PP(1.01262, 160)
        c3 = z2 + PP(0.337539, 65)
        c4 = z2 + PP(0.504748, -114)
        z3 = z2 + PP(1.31049, -71)
        c5 = z3 + PP(0.436832, -178)
        c6 = z3 + PP(0.682013, 1)
        z4 = z3 + PP(2.04604, 74)
        #z4 = z5 - PP(2.99998, ta + 0)
        c7 = z4 + PP(0.933519, -90)
        c8 = z4 + PP(0.999993, -90)
        z5 = z4 + PP(2.99998, -90)
        c9 = z5 + PP(0.999993, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_NELCLTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLTS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLTS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLTS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLTSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLTSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLTSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLTS(cls, ta=None, **kwargs):
        #M 294.585,113.513 C 304.47065,113.513 319.43744,84.718795 319.43744,75.586595 319.43744,72.630195 317.14444,73.737695 316.74044,74.604795 316.15844,75.911895 316.71144,78.160395 317.94944,78.117195 319.88244,78.083495 319.54844,75.188295 319.54844,72.542095 319.54844,75.376731 319.54844,78.470978 319.54844,81.045995

        #z0 = P(0, -0)
        #c0 = P(3.48744, -0)
        #c1 = P(8.76739, 10.158)
        #z1 = P(8.76739, 13.3796)
        #c2 = P(8.76739, 14.4225)
        #c3 = P(7.95847, 14.0318)
        #z2 = P(7.81595, 13.726)
        #c4 = P(7.61063, 13.2648)
        #c5 = P(7.80572, 12.4716)
        #z3 = P(8.24246, 12.4869)
        #c6 = P(8.92437, 12.4987)
        #c7 = P(8.80655, 13.5201)
        #z4 = P(8.80655, 14.4536)
        #c8 = P(8.80655, 13.4536)
        #c9 = P(8.80655, 12.362)
        z5 = P(8.80655, 11.4536)

        #z0 = P(0, -0)
        #c0 = z0 + P(3.48744, 0)
        #z1 = z0 + P(8.76739, 13.3796)
        #c1 = z1 + P(0, -3.22164)
        #c2 = z1 + P(0, 1.04295)
        #z2 = z1 + P(-0.951442, 0.346357)
        #c3 = z2 + P(0.142522, 0.305894)
        #c4 = z2 + P(-0.205317, -0.461116)
        #z3 = z2 + P(0.426508, -1.2391)
        #c5 = z3 + P(-0.436739, -0.01524)
        #c6 = z3 + P(0.681919, 0.0118886)
        #z4 = z3 + P(0.564092, 1.96677)
        #c7 = z4 + P(0, -0.933521)
        #c8 = z4 + P(0, -0.999997)
        #z5 = z4 + P(0, -2.99999)
        #c9 = z5 + P(0, 0.908409)

        z0 = P(0, -0)
        c0 = z0 + PP(3.48744, 0)
        z1 = z0 + PP(15.9963, 56)
        c1 = z1 + PP(3.22164, -90)
        c2 = z1 + PP(1.04295, 90)
        z2 = z1 + PP(1.01252, 159)
        c3 = z2 + PP(0.337466, 65)
        c4 = z2 + PP(0.50476, -114)
        z3 = z2 + PP(1.31045, -71)
        c5 = z3 + PP(0.437005, -178)
        c6 = z3 + PP(0.682023, 0)
        z4 = z3 + PP(2.04607, 73)
        #z4 = z5 - PP(2.99999, ta + 0)
        c7 = z4 + PP(0.933521, -90)
        c8 = z4 + PP(0.999997, -90)
        z5 = z4 + PP(2.99999, -90)
        c9 = z5 + PP(0.908409, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_selNELCLTSs(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELCLTS())

    @classmethod
    def path_selNELCLTSsel(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELCLTS())

    @classmethod
    def path_selNELCLTSswr(cls, ta=None, **kwargs):
        return cls.jog(cls.path_selNELCLTS())

    def get_paths(self):
        if self.to_reverse():
            self.head_type = 'SWR'
            self.tail_type = 'S'
            self.model = 'SWR16CR1TS3'

            self.head_ligature = {'ER', 'NER'}
            self.tail_ligature = {'S', 'SEL', 'SWR'}
            self.both_ligature = {}
        else:
            self.head_type = 'NEL'
            self.tail_type = 'S'
            self.model = 'NEL16CL1TS3'

            self.head_ligature = {'EL', 'SWL', 'SL', 'SEL'}
            self.tail_ligature = {'S', 'SEL', 'SWR'}
            self.head_ligature = {'SEL'}
            self.tail_ligature = {}
            self.both_ligature = {}

        return super(WasedaChar, self).get_paths()
