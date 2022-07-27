class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness
        self.mass_for_1sqr_metr = 25

    def total_mass(self):
        ''' length, width in metres, thickness in centimetres, return tons'''

        return (self._length * self._width * self.mass_for_1sqr_metr * self.thickness)/1000

my_road = Road(5000, 20, 5)
print(my_road.total_mass())
