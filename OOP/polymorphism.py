class Dog:

    def sound(self):
        print("Dog says: Woof!")


class Cat:

    def sound(self):
        print("Cat says: Meow!")


class Cow:

    def sound(self):
        print("Cow says: Moo!")


animals = [
    Dog(),
    Cat(),
    Cow()
]

for animal in animals:
    animal.sound()
