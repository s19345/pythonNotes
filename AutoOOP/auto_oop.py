class Auto():
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0
        self.engine = False

    def start_engine(self):
        if self.engine:
            print("engine is already working")
        else:
            self.engine = True
            print("engine is working")

    def stop_engine(self):
        if self.engine:
            if self.speed == 0:
                self.engine = False
                print("engine is stopped")
            else:
                print("slow down first")

        else:
            print("engine is already stopped")

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f"Your speed is {self.speed}")
        else:
            print("start engine first")

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f"Your speed is {self.speed}")

    def opis(self):
        print(f"Model: {self.model}, Max Speed: {self.max_speed}, Speed: {self.speed}, Engine: {self.engine}")

    def __str__(self):
        return f"(to jest metoda __str__) Model: {self.model}, Max Speed: {self.max_speed}, Speed: {self.speed}, Engine: {self.engine}"


class Van(Auto):
    def __init__(self, model, max_speed, seats=7):
        super().__init__(model, max_speed)
        self.seats = seats

    def van(self):
        print(f"This is a van")

    def __str__(self):
        return f"(to jest metoda __str__) Model: {self.model}, Max Speed: {self.max_speed}, Speed: {self.speed}, Engine: {self.engine}, Seats: {self.seats}"


# class SportCar(Auto, Van):
#     def __init__(self, model, max_speed, turbo_enabled=True):
#         super().__init__(model, max_speed)
#         self.turbo_enabled = turbo_enabled
#
#     def speed_up(self, amount):
#         if self.engine:
#             if self.turbo_enabled:
#                 print("Turbo mode activated!")
#                 amount *= 2
#             self.speed = min(self.speed + amount, self.max_speed)
#             print(f"Your speed is {self.speed}")
#         else:
#             print("start engine first")
#
#     def enable_turbo(self):
#         self.turbo_enabled = True
#         print("Turbo mode is now enabled")
#
#     def disable_turbo(self):
#         self.turbo_enabled = False
#         print("Turbo mode is now disabled")


fiat = Auto("500", 100)
ford = Van("Transit", 150)


# ferrari = SportCar("F40", 200, turbo_enabled=False)
# ferrari.van()
# ferrari.max_speed
# ferrari.enable_turbo()
# ferrari.start_engine()
# ferrari.opis()


# print(SportCar.__mro__)
# print(dir(SportCar))
# # print(ferrari.__str__())
# print(ferrari.__repr__())


def run(car):
    print(car)
    car.start_engine()
    car.speed_up(30)
    car.speed_up(70)
    car.stop_engine()
    car.slow_down(270)
    car.stop_engine()


run(fiat)
run(ford)
