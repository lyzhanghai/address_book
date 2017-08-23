class Kls(object):
    no_inst = 0

    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst

    @staticmethod
    def getno_of_instance():
        return None


ik1 = Kls()
ik1.get_no_of_instance()
# ik2 = Kls()

print(Kls.get_no_of_instance())
# print(Kls.get_no_of_instance())
