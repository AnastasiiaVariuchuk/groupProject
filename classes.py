class Parcel:
    LENGTH = 10
    HEIGHT = 5

    def __init__(self, width, weight):
        self.width = width
        self.weight = weight
        if self.width < 0 or self.weight < 0:
            raise ValueError("Parcel dimensions exceed limits")


class Recipient:
    def __init__(self, address):
        self.address = address


class Road:
    def __init__(self, address1, address2, length):
        self.address1 = address1
        self.address2 = address2
        self.length = length


class Courier:
    def __init__(self, speed):
        self.speed = speed


# class Bag:
#     def __init__(self, height, width, length):
#         self.height = height
#         self.width = width
#         self.length = length
#

class FootCourier(Courier):
    class Bag:
        HEIGHT = 40
        WIDTH = 30
        LENGTH = 40
        MAX_WEIGHT = 25

    def __init__(self, speed, salary_costs_per_hour):
        super().__init__(speed)
        self.salary_costs_per_hour = salary_costs_per_hour
        self.bag = self.Bag()


class CarCourier(Courier):
    class Trunk:
        HEIGHT = 50
        WIDTH = 60
        LENGTH = 100
        MAX_WEIGHT = 300

    def __init__(self, speed, salary_costs_per_hour, fuel_per_hour):
        super().__init__(speed)
        self.salary_costs_per_hour = salary_costs_per_hour
        self.fuel_per_hour = fuel_per_hour
        self.trunk = self.Trunk()
