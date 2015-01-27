"""This file should have our melon-type classes in it."""

class AbstractMelon(object):
    BASE_MELON_PRICE = 5.0
    def __init__(self,melon_type):
        self.melon_type = melon_type
        self.color = None
        self.imported = False
        self.shape = "natural"
        self.seasons = None
        self.pricetag = self.BASE_MELON_PRICE
    def get_price(self,qty,pricetag=BASE_MELON_PRICE):
        return pricetag*qty

class SquareMelon(AbstractMelon):
    def __init__(self, melon_type):
        super(SquareMelon,self).__init__(melon_type)
        # reset attributes for a square melon
        self.shape = "square"
        self.pricetag = self.pricetag * 2   # 10
    def get_price(self,qty):
        return super(SquareMelon,self).get_price(qty,self.pricetag)

class ImportedMelon(AbstractMelon):
    def __init__(self, melon_type):
        super(ImportedMelon,self).__init__(melon_type)
        # reset attributes for an imported melon
        self.imported = True   
        self.pricetag = self.pricetag * 1.5     # 7.5
    def get_price(self,qty):
        return super(ImportedMelon,self).get_price(qty,self.pricetag)

class Xigua(SquareMelon):
    def __init__(self, melon_type="Xigua"):
        super(Xigua,self).__init__(melon_type)
        # Xigua is square and imported. Reset price tag.
        self.pricetag = self.pricetag * 1.5     # 15
        # Xigua has other specific attributes of color and seasons.
        self.color = "black"
        self.seasons = ['Summer']

class Xigua2(SquareMelon,ImportedMelon):
    def __init__(self, melon_type="Xigua"):
        super(Xigua2,self).__init__(melon_type)
        # the two class, with the self.pricetag=self.pricetag * modifier
            #outcome should be pricetag = 15
        # Xigua has other specific attributes of color and seasons.
        self.color = "black"
        self.seasons = ['Summer']

## TODO:  separate class per each type of melon?
## TODO:  how can do dual-class?  imported and square?


