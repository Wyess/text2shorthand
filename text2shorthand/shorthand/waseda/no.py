from ..waseda.char import WasedaChar
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve, path

class CharNo(WasedaChar):
    def __init__(self, name='no', kana='の', model='EL16', head_type='EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)
        
    @classmethod
    def path_template(cls, ta=90, tn=2.5):
        return path([beginknot(0, 0, angle=-13), tensioncurve(tn), endknot(16, 0, angle=ta)])

    @classmethod
    def path_fusion(cls, ta=90, tn=1.0):
        return cls.path_template(ta, tn)

    @classmethod
    def path_tan(cls, ta=80):
        return cls.path_template(ta+180)

    @classmethod
    def path_flat(cls):
        return cls.path_template(ta=60)

    @classmethod
    def path_up(cls):
        return cls.path_template(ta=90)

    @classmethod
    def path_EL(cls, ta=None, **kwargs):
        return cls.path_template()

    @classmethod
    def path_ELsel(cls, ta=None, **kwargs):
        return cls.path_flat()

    @classmethod
    def path_ELxne(cls, ta=None, **kwargs):
        return cls.path_flat()

    @classmethod
    def path_ELer(cls, ta=None, **kwargs):
        return cls.path_fusion(ta)

    @classmethod
    def path_ELsw(cls, ta=None, **kwargs):
        return cls.path_tan(ta)

    @classmethod
    def path_ELswl(cls, ta=None, **kwargs):
        return cls.path_tan(ta)

    @classmethod
    def path_ELe(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELse(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELnel(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELswr(cls, ta=None, **kwargs):
        return cls.path_up()

    @classmethod
    def path_ELne(cls, ta=None, **kwargs):
        return cls.path_up()
        
class CharNon(CharNo):
    def __init__(self, name='non', kana='のん', model='EL16F', head_type='EL', tail_type='F'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharNoku(CharNo):
    def __init__(self, name='noku', kana='のく', model='BEL16', head_type='BEL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.barbs:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharNotsu(CharNo):
    def __init__(self, name='notsu', kana='のつ', model='CL1EL16', head_type='CL1EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in self.head_circles:
            return self.add_head_circle(super().get_paths())
        else:
            return super().get_paths()
