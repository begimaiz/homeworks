# Ai generated homework
# create the following in python with comments:
# 1. Create a class Car with four parameters that include car_name, model, year, speed, where speed is a tuple that holds two values for km and hour. create getters and setters for all parameters
# 2. Create a class Electric_car that inherits the class Car with additional 2 parameters that include engine and capacity. create getters and setters for all parameters
# 3. create a class Fuel_car that inherits the class Car with additional 2 parameters that include engine and fuel. create getters and setters for all parameters
# 4. in a method called generate_cars, create random 3 objects of Electric_car and 2 objects of Fuel_car with unique values and add it to a list called my_cars
# 5. create method called start_race that takes as parameters user_distance and the list my_cars  and then takes their speed and calculates which car has the biggest speed for given distance.  print every all objects with description of parameters and values in the list and then print the object with max speed in separate line
# 6. call the method start_race with a randomly generated number as distance


# 1 Create a class Car
class Car:
    # constructor
    def __init__(self, car_name, model, year, speed):
        self.__car_name = car_name
        self.__model = model
        self.__year = year
        self.__speed = speed

    # getters
    def get_car_name(self):
        return self.__car_name

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    # setters
    def set_car_name(self, car_name):
        self.__car_name = car_name

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_speed(self, speed):
        self.__speed = speed

# 2 Create a class Electric_car
class Electric_car(Car):
    # constructor
    def __init__(self, car_name, model, year, speed, engine, capacity):
        # call parent constructor
        super().__init__(car_name, model, year, speed)
        self.__engine = engine
        self.__capacity = capacity

    # getters
    def get_engine(self):
        return self.__engine

    def get_capacity(self):
        return self.__capacity

    # setters
    def set_engine(self, engine):
        self.__engine = engine

    def set_capacity(self, capacity):
        self.__capacity = capacity


# 3 create a class Fuel_car
class Fuel_car(Car):
    # constructor
    def __init__(self, car_name, model, year, speed, engine, fuel):
        # call parent constructor
        super().__init__(car_name, model, year, speed)
        self.__engine = engine
        self.__fuel = fuel

    # getters
    def get_engine(self):
        return self.__engine

    def get_fuel(self):
        return self.__fuel

    # setters
    def set_engine(self, engine):
        self.__engine = engine

    def set_fuel(self, fuel):
        self.__fuel = fuel


# 4 create a method generate_cars
def generate_cars():
    my_cars = []
    # create random 3 objects of Electric_car
    for i in range(3):
        car_name = 'Electric_' + str(i)
        model = 'Model_' + str(i)
        year = i + 2020
        speed = (i + 20, i + 30)
        engine = 'Engine_' + str(i)
        capacity = i + 50
        car = Electric_car(car_name, model, year, speed, engine, capacity)
        my_cars.append(car)
    # create random 2 objects of Fuel_car
    for i in range(2):
        car_name = 'Fuel_' + str(i)
        model = 'Model_' + str(i)
        year = i + 2021
        speed = (i + 30, i + 40)
        engine = 'Engine_' + str(i)
        fuel = 'Fuel_' + str(i)
        car = Fuel_car(car_name, model, year, speed, engine, fuel)
        my_cars.append(car)
    return my_cars


# 5 create a method start_race
def start_race(user_distance, my_cars):
    # calculate the max speed
    max_speed = 0
    max_car = None
    for car in my_cars:
        km, hour = car.get_speed()
        speed = km / hour
        total_speed = speed * user_distance
        if total_speed > max_speed:
            max_speed = total_speed
            max_car = car
    # print every object
    for car in my_cars:
        print(car.__dict__)
    # print the object with max speed
    print("The car with max speed is: ")
    print(max_car.__dict__)


# 6 call the method start_race with a randomly generated number as distance
import random

user_distance = random.randint(1, 10)
my_cars = generate_cars()
start_race(user_distance, my_cars)