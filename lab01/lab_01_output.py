class Vehicle:
    def move(self):
        raise NotImplementedError()


class Car(Vehicle):
    def move(self):
        print("Машина поїхала")


class Airplane(Vehicle):
    def move(self):
        print("Літак пішов на взліт")


def get_vehicle(vehicle_type):
    if vehicle_type == "машина":
        return Car()
    elif vehicle_type == "літак":
        return Airplane()
    else:
        print("Не знаю що за транспорт :(")
        return None



def main():
    vehicle = get_vehicle("машина")
    vehicle.move()

    vehicle = get_vehicle("літак")
    vehicle.move()


if __name__ == "__main__":
    main()
