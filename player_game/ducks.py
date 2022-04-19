class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun!")
        elif self.ratio == 1:
            print(" This is hard work but Im flying")
        else:
            print("I think Ill just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")
    
    def swim(self):
        print("Come on in, but its a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a laugh? Im a penguin!")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)
