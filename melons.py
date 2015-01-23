"""This file should have our melon-type classes in it."""

class AbstractMelon(object):
    def __init__(self,my_type,my_shape="natural",origin=False):
        self.melon_type = my_type
        self.color = None
        self.imported = origin
        self.shape = my_shape
        self.seasons = None

class SquareMelon(AbstractMelon):
    def __init__(self, my_type):
        return super(SquareMelon,self).__init__(my_type,my_shape="square")

class ImportedMelon(AbstractMelon):
    def __init__(self, my_type):
        return super(ImportedMelon,self).__init__(my_type,origin=True)



# class Xigua(SquareMelon):
#     def __init__(self):
#         super(Xigua,self).__init__(my_type)
