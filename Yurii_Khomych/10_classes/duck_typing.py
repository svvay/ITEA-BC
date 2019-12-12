class Duck:
    def quack(self):
        print("Quack!")

    def feathers(self):
        print("The duck has white and gray feathers")


class Person:
    def yell(self):
        print("A person is yelling")

    def feathers(self):
        print("Man lifted feathers from the ground and shows him")

    def name(self):
        print("John English")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()