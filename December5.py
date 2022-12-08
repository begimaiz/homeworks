# this homework was done using help from AI

# create the following in python:
# 1. Create a class Car with four parameters that include car_name, model, year, speed, where speed is a tuple that holds two values for km and hour
# 2. Create a class Electric_car that inherits the class Car with additional 2 parameters that include engine and type
# 3. create a class Fuel_car that inherits the class Car with additional 2 parameters that include engine and fuel
# 4. create getters and setters for all parameters
# 5. in a method called generate_cars, create randomly 3 objects of Electric_car with unique parameters and 2 objects of Fuel_car with unique parameters and add it to a list called my_cars
# 6. create method called start_race that takes as parameters user_distance and the list my_cars  and then takes their speed and calculates which car has the biggest speed for given distance.  print every all objects with description of parameters and values in the list and then print the object with max speed in separate line
# 7. call the method start_race with a randomly generator number as distance


import random

class Car:
    def __init__(self, car_name, model, year, speed):
        self.car_name = car_name
        self.model = model
        self.year = year
        self.speed = speed

    def get_car_name(self):
        return self.car_name

    def set_car_name(self, car_name):
        self.car_name = car_name

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed


class Electric_car(Car):
    def __init__(self, car_name, model, year, speed, engine, type):
        super().__init__(car_name, model, year, speed)
        self.engine = engine
        self.type = type

    def get_engine(self):
        return self.engine

    def set_engine(self, engine):
        self.engine = engine

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type


class Fuel_car(Car):
    def __init__(self, car_name, model, year, speed, engine, fuel):
        super().__init__(car_name, model, year, speed)
        self.engine = engine
        self.fuel = fuel

    def get_engine(self):
        return self.engine

    def set_engine(self, engine):
        self.engine = engine

    def get_fuel(self):
        return self.fuel

    def set_fuel(self, fuel):
        self.fuel = fuel


def generate_cars():
    my_cars = []
    for i in range(3):
        my_cars.append(
            Electric_car("car" + str(i + 1), "model" + str(i + 1), 2020, (20, 30), "electric", "type" + str(i + 1)))
    for i in range(2):
        my_cars.append(Fuel_car("car" + str(i + 1), "model" + str(i + 1), 2020, (30, 40), "fuel", "fuel" + str(i + 1)))
    return my_cars


def start_race(user_distance, my_cars):
    max_speed = 0
    chosen_car = None
    for car in my_cars:
        speed_km = car.speed[0]
        speed_h = car.speed[1]
        distance_km = user_distance * speed_km
        distance_h = user_distance * speed_h
        print(
            "Description of car: car_name: {}, model: {}, year: {}, speed: {}".format(car.car_name, car.model, car.year,
                                                                                      car.speed))
        if car.speed[0] > max_speed:
            max_speed = car.speed[0]
            chosen_car = car
    print("Chosen car is: car_name: {}, model: {}, year: {}, speed: {}".format(chosen_car.car_name, chosen_car.model,
                                                                               chosen_car.year, chosen_car.speed))


distance = random.randint(1, 10)
start_race(distance, generate_cars())