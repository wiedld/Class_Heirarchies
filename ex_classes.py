from melons import *

sq_test = SquareMelon("Squarey")
imp_test = ImportedMelon("Frenchie")
oggie = Ogen()
cher = Sharlyn()
w = Watermelon()
canna = Cantaloupe()
xiggy = Xigua()

print "SQUARE Melon attributes:"
print "\t Melon type:", sq_test.melon_type
print "\t Imported:", sq_test.imported
print "\t Shape:", sq_test.shape
print "\t Seasons:", sq_test.seasons
print "\t Pricetag:", sq_test.pricetag
print "\t Cost for two:", sq_test.get_price(2)

print "IMPORTED Melon attributes:"
print "\t Melon type:", imp_test.melon_type
print "\t Imported:", imp_test.imported
print "\t Shape:", imp_test.shape
print "\t Seasons:", imp_test.seasons
print "\t Pricetag:", imp_test.pricetag
print "\t Cost for two:", imp_test.get_price(2)

print "Ogen Melon attributes:"
print "\t Melon type:", oggie.melon_type
print "\t Imported:", oggie.imported
print "\t Shape:", oggie.shape
print "\t Seasons:", oggie.seasons
print "\t Pricetag:", oggie.pricetag
print "\t Cost for two:", oggie.get_price(2)

print "Sharlyn Melon attributes:"
print "\t Melon type:", cher.melon_type
print "\t Imported:", cher.imported
print "\t Shape:", cher.shape
print "\t Seasons:", cher.seasons
print "\t Pricetag:", cher.pricetag
print "\t Cost for two:", cher.get_price(2)

print "Watermelon Melon attributes:  special pricing!"
print "\t Melon type:", w.melon_type
print "\t Imported:", w.imported
print "\t Shape:", w.shape
print "\t Seasons:", w.seasons
print "\t Pricetag:", w.pricetag
print "\t Cost for two:", w.get_price(2)

print "Canteloupe Melon attributes:  special pricing!"
print "\t Melon type:", canna.melon_type
print "\t Imported:", canna.imported
print "\t Shape:", canna.shape
print "\t Seasons:", canna.seasons
print "\t Pricetag:", canna.pricetag
print "\t Cost for two:", canna.get_price(2)

print "XIGUA Melon attributes:  multiple hierarchies!"
print "\t Melon type:", xiggy.melon_type
print "\t Imported:", xiggy.imported
print "\t Shape:", xiggy.shape
print "\t Seasons:", xiggy.seasons
print "\t Pricetag:", xiggy.pricetag
print "\t Cost for two:", xiggy.get_price(2)