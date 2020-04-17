class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):    
    return self.artist + ": " + self.title + " , " + str(self.year) + "; " + self.medium + ". " + self.owner.name +" , "+ "({})".format(self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listing = []
  
  def add_listing(self, new_listing):
    self.listing.append(new_listing)
  
  def remove_listing(self, new_listing):
    self.listing.remove(new_listing)
  
  def show_listing(self):
    for l in self.listing:
      print(l)

class Client:
  
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
       self.location = "Private Collector"
  
  def sell_artwork(self, artwork, price):
    if self is artwork.owner:
      lis = Listing(artwork, price, self)
      veneer.add_listing(lis)
  
  def buy_artwork(self,artwork):
    art_listing = None
    if artwork.owner != self :
      for listing in veneer.listing:
        if listing.art == artwork:
          art_listing = listing
          break
    if art_listing != None:
      artwork.owner = self
      veneer.remove_listing(art_listing)


class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return  self.art.title +", Price: "+str(self.price) +" USD )"
  

  
veneer = Marketplace()

edytta = Client("Edytta Halpirt", None, False)
moma = Client("THE MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin,(Fanny Tellier)" , "oil on canvas", 1910, edytta)

print(girl_with_mandolin)
veneer.show_listing()

edytta.sell_artwork(girl_with_mandolin, 6000000)
veneer.show_listing()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)







  