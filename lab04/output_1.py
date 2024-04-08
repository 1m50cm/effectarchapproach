class Animal:
    def speak(self):
        pass

    def move(self):
        pass


class Dog:
    anml = Animal()

    def speak(self):
        return self.anml.speak()

    def move(self):
        return self.anml.move()


def main():
    dog = Dog()
    dog.speak()
    dog.move()


if __name__ == '__main__':
    main()
