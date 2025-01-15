def auto_init(model, max_speed):
    return {
        "model": model,
        "max_speed": max_speed,
        "speed": 0,
        "engine": False
    }


def start_engine(car):
    if car["engine"]:
        print("engine is already working")
    else:
        car["engine"] = True
        print("engine is working")


def stop_engine(car):
    if car["engine"]:
        if car["speed"] == 0:
            car["engine"] = False
            print("engine is stopped")
        else:
            print("slow down first")

    else:
        print("engine is already stopped")


def speed_up(car, amount):
    if car["engine"]:
        car["speed"] = min(car["speed"] + amount, car["max_speed"])
        print(f"Your speed is {car['speed']}")
    else:
        print("start engine first")


def slow_down(car, amount):
    car["speed"] = max(car["speed"] - amount, 0)
    print(f"Your speed is {car['speed']}")


fiat = auto_init("500", 100)
speed_up(fiat, 20)
start_engine(fiat)
speed_up(fiat, 20)
speed_up(fiat, 200)
stop_engine(fiat)
slow_down(fiat, 40)
slow_down(fiat, 70)
stop_engine(fiat)

