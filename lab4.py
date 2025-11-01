class Car:
    def __init__(self, make, model):
        self._make = make 
        self._model = model 

    def drive(self):
        print(f"Driving the {self._make} {self._model}")
my_car = Car ("Toyota", "Corolla")
print(my_car._make)
my_car.drive()