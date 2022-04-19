import random

#class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", _hit_points=0, lives=1):
        self.name = name
        self._hit_points = _hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("Random monster attacked me! I took {} points damage and have {} left.".format(damage, self._hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("I attack {0.name}, he lost a life".format(self))
            else:
                print("{0.name} is dead.".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, _hit_points=3)
        super().__init__(name=name, lives=1, _hit_points=3)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))
        
class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, _hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)