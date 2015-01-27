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
        return self.pricetag*qty

class ImportedMelon(AbstractMelon):
    def __init__(self, melon_type):
        super(ImportedMelon,self).__init__(melon_type)
        # reset attributes for an imported melon
        self.imported = True   
        self.pricetag = self.pricetag * 1.5     # 7.5
    def get_price(self,qty):
        return self.pricetag*qty


########## INDIVIDUAL MELON, PARENT: ABSTRACT ##########
class Ogen(AbstractMelon):
    def __init__(self, melon_type="Ogen"):
        super(Ogen,self).__init__(melon_type)
    # Ogen specific attributes:
        self.pricetag = self.pricetag + 1
        self.color = "tan"
        self.seasons = ['Spring', 'Summer']
    def get_price(self,qty):
        return self.pricetag*qty


########## INDIVIDUAL MELON, SINGLE PARENT (IMPORTED) ##########
class Sharlyn(ImportedMelon):
    def __init__(self, melon_type="Sharlyn"):
        super(Sharlyn,self).__init__(melon_type)
    # Sharlyn specific attributes:
        self.color = "tan"
        self.seasons = ['Summer']
    # can use parent get_price(), since pricetag does not change


########## INDIVIDUAL MELON, PARENT: ABSTRACT, special pricing ##########
class Watermelon(AbstractMelon):
    def __init__(self, melon_type="Watermelon"):
        super(Watermelon,self).__init__(melon_type)
    # Watermelon specific attributes:
        self.color = "green"
        self.seasons = ['Fall','Summer']
    def get_price(self,qty):
        if qty >=3:
            return self.pricetag*qty*0.75
        else: 
            return self.pricetag*qty  
         
class Cantaloupe(AbstractMelon):
    def __init__(self, melon_type="Cantaloupe"):
        super(Cantaloupe,self).__init__(melon_type)
    # Cantaloupe specific attributes:
        self.color = "tan"
        self.seasons = ['Spring','Summer']
    def get_price(self,qty):
        if qty >=5:
            return self.pricetag*qty*0.5
        else: 
            return self.pricetag*qty


########## INDIVIDUAL MELON, MULTIPLE PARENTS ##########
class Xigua(SquareMelon,ImportedMelon):
    def __init__(self, melon_type="Xigua"):
        super(Xigua,self).__init__(melon_type)
        # the two class, with the self.pricetag=self.pricetag * modifier
            # outcome should be pricetag = 15
        # Xigua specific attributes:
        self.color = "black"
        self.seasons = ['Summer']
    def get_price(self,qty):
        return self.pricetag*qty
