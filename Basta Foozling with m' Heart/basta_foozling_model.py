class Menu:
  
  def __init__( self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time= start_time
    self.end_time= end_time
  
  def __repr__(self):
    return self.name +" will be available from "+ str( self.start_time) +" to "+ str(self.end_time)
  
  def calculate_bill(self, purchased_items):
    t_price = 0
    for pur in purchased_items:
      t_price += self.items[pur]   
    return t_price
  
brunch  = Menu( "Brunch", {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)


early_bird = Menu( "Early-bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu("Kids Food", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)

arepas_menu = Menu("Take a’ Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10 ,20)

# print(brunch)
# print(early_bird.calculate_bill(["salumeria plate",'mushroom ravioli (vegan)']))

class Franchise:
  def __init__(self,address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address
  
  def available_menus(self,time):
    for i in self.menus:
      if i.start_time <= time and i.end_time >= time:
        print(i)
    
flagship_store  = Franchise("1232 West End Road",[ kids, brunch, early_bird, dinner])
new_installment = Franchise("12 East Mulberry Street", [kids, brunch, early_bird, dinner])

# flagship_store.available_menus(12)
# flagship_store.available_menus(17)

class Bussiness:
  def __init__(self,name,franchise):
    self.name = name
    self.franchise = franchise
    
bussiness = Bussiness("Basta Fazoolin' with my Heart",[flagship_store, new_installment])










