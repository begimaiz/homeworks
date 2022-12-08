class Car():
    def __init__(self, car_name, model, year, speed):
        self.car_name = car_name
        self.model = model
        self.year = year
        self.speed = speed

    def get_car_name(self):
        return self.car_name

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_speed(self):
        return self.speed

    def set_car_name(self, car_name):
        self.car_name = car_name

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_speed(self, speed):
        self.speed = speed


class Electric_car(Car):
    def __init__(self, car_name, model, year, speed, engine, capacity):
        super().__init__(car_name, model, year, speed)
        self.engine = engine
        self.capacity = capacity

    def get_engine(self):
        return self.engine

    def get_capacity(self):
        return self.capacity

    def set_engine(self, engine):
        self.engine = engine

    def set_capacity(self, capacity):
        self.capacity = capacity


class Fuel_car(Car):
    def __init__(self, car_name, model, year, speed, engine, fuel):
        super().__init__(car_name, model, year, speed)
        self.engine = engine
        self.fuel = fuel

    def get_engine(self):
        return self.engine

    def get_fuel(self):
        return self.fuel

    def set_engine(self, engine):
        self.engine = engine

    def set_fuel(self, fuel):
        self.fuel = fuel


def generate_cars():
    my_cars = []
    electric_1 = Electric_car("Tesla", "X", 2020, (200, 100), "Electric", 2000)
    electric_2 = Electric_car("Volkswagen", "e-Golf", 2021, (180, 90), "Electric", 1800)
    electric_3 = Electric_car("Volvo", "XC40 Recharge", 2020, (220, 110), "Electric", 2200)
    fuel_1 = Fuel_car("Ferrari", "488 GTB", 2020, (250, 130), "V8", "Petrol")
    fuel_2 = Fuel_car("Porsche", "911", 2021, (260, 140), "V6", "Diesel")
    my_cars.append(electric_1)
    my_cars.append(electric_2)
    my_cars.append(electric_3)
    my_cars.append(fuel_1)
    my_cars.append(fuel_2)
    return my_cars


def start_race(user_distance, my_cars):
    max_speed = 0
    fastest_car = None
    for car in my_cars:
        speed_in_km = car.get_speed()[0]
        speed_in_hour = car.get_speed()[1]
        total_speed = speed_in_km + speed_in_hour * user_distance
        if total_speed > max_speed:
            max_speed = total_speed
            fastest_car = car
    print("Cars with their details:")
    for car in my_cars:
        print(car.__dict__)
    print("\nFastest car:")
    print(fastest_car.__dict__)


my_cars = generate_cars()
start_race(100, my_cars)