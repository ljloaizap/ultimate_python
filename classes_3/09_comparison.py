class Coordinates:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon

    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon

    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coords1 = Coordinates(44, 27)
coords2 = Coordinates(45, 27)
print(coords1)
print(coords2)

print('==  ', coords1 == coords2)  # __eq__
print('!=  ', coords1 != coords2)  # __ne__
print('<  ', coords1 < coords2)  # __lt__
print('>  ', coords1 > coords2)  # (python infers)
print('<=  ', coords1 <= coords2)  # __le__
print('>=  ', coords1 >= coords2)  # (python infers)
