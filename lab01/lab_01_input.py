def move_vehicle(vehicle_type, operation):
    if vehicle_type == "машина":
        if operation == "їхати":
            print("Машина поїхала")
        else:
            print("Я таке не вмію")
    elif vehicle_type == "літак":
        if operation == "їхати":
            print("Літак пішов на взліт")
        else:
            print("Я таке не вмію(")
    else:
        print("Не знаю що за транспорт :(")


def main():
    move_vehicle("машина", "їхати")
    move_vehicle("літак", "їхати")


if __name__ == '__main__':
    main()
