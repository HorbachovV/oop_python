class Vehicle:
    all_atribute_list = []
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        Vehicle.all_atribute_list.append(self)

    def engine_start(self):
        print('Engine is start')

    def engine_stop(self):
        print('Engine is stop')
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.make}', {self.model}, {self.year})"

    
class Car(Vehicle):

    def __init__(self, make, model, year, color):
        self.color = color
        super().__init__(
            make, model, year
        )
    
ford = Car('Ford', 'Edge', 2023, 'Silver')

for obj in ford.all_atribute_list:
    if isinstance(obj, Car):
        print(obj)


class Tank(Vehicle):
    
    def __init__(self, make, model, year, weight):
        self.weight = weight
        super().__init__(
            make, model, year
        )
    def fire(self):
        print('Tank is fire')

leopard = Tank('Reihnmetall', 'leopard 2A6A', 2021, 65)


for obj in leopard.all_atribute_list:
    if isinstance(obj, Tank):
        print(obj)