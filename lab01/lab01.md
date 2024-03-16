# Лабораторна робота № 1
## Тема: Довгий метод. 

#### Опис проблеми:
> Цей код порушує принцип єдиної відповідальності (Single Responsibility Principle, SRP), оскільки метод move_vehicle() відповідає за надто багато різних завдань: визначення типу транспортного засобу, визначення операції та виконання відповідної дії для кожного типу транспортного засобу.

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


### Рішення: зробити інтерфейс з методом move_vehicle(), що описує транспортний засіб та його підкласи. 
### також виокремимо метод get_vehicle() для отримання класу відповідно до типу транспорту

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



### Висновок: маємо можливість створювати безліч нових класів типу транспорту
