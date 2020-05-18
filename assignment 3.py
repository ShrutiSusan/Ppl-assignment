class cat():

    def __init__(self, color,legs, eyes):
      self.color=color;
      self.legs=legs;
      self.__eyes=eyes; 
    def eats(self):
        print("Eats Meat")
    def get_legs(self):
      return self.legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.color
    def __sounds(self):
        print("PURRR......")


class dog():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("Eats Meat")
    def get_legs(self):
      return self.__legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def sounds(self):
      print("Barkss...")

class elephant():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("Eats Grass and leaves")
    def get_legs(self):
      return self.__egs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def sounds(self):
      print("Trumpet")
class Lion():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("Eats Meat-other animals")
    def get_legs(self):
      return self.__legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def sounds(self):
      print("Growls")
class Cheetah():
    def __init__(self, color,legs, eyes):
      self.color=color;
      self.legs=legs;
      self.eyes=eyes;
    def eats(self):
        print("Eats Meat")
    def get_legs(self):
      return self.legs;
    def get_eyes(self):
      return self.eyes;
    def get_color (self):
      return self.color
    def  characteristics(self):
      print("Runs The Fastest ")
class monkey():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("Eats Bananasss")
    def get_legs(self):
      return self.__legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def  characteristics(self):
      print("Monkeys swing arm-to-arm in trees ")

class Humans():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("humans eat meat as well as grass")
    def get_legs(self):
      return self.__legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def  characteristics(self):
      print("they are mammals")
class Whales():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__legs=legs;
      self.__eyes=eyes;
    def eats(self):
        print("Eats a variety of fish")
    def get_legs(self):
      return self.__legs;
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def  characteristics(self):
      print("they are mammals and swim in the water")
class Birds():
    def __init__(self, color,legs, eyes):
      self.__color=color;
      self.__eyes=eyes;
    def eats(self):
        print("Eats worms")
    def get_eyes(self):
      return self.__eyes;
    def get_color (self):
      return self.__color
    def  characteristics(self):
      print("They have feathers")
class Snakes():
    def __init__(self,color):
      self.__color=color;
    def eats(self):
        print("Snakes are carnivores")
    def get_eyes(self):
      return self.eyes;
    def get_color (self):
      return self.__color
    def  characteristics(self):
      print("Ectotherms-covered by scales and is generally dry to the touch")
    def sounds(self):
      print("HISSSS...");
print("Cats")
c=cat("brown",4,2);
print("The no of eyes the animal has is:-")
print(c.get_eyes())
print("The color of the animal is")
print(c.get_color())
print("Food-")
c.eats()
print("\n")
print("Monkeys")
m=monkey("black",2,2);
m.eats()
print("The no of eyes the animal has is:-")
print(c.get_eyes())
print("The color of the animal is")
print(c.get_color())

print("\n")
print("Humans")
h=Humans("Different complexions",2,2);
h.eats()
print("The no of eyes the animal has is:-")
print(h.get_eyes())
print("The color of the animal is")
print(h.get_color())
print("Characteristics -")
h.characteristics()

print("\n")
print("Snakes")
s=Snakes("Green");
s.eats()
print("The color of the animal is")
print(s.get_color())
print("Characteristics -")
s.characteristics()
print("sounds")
s.sounds()

print("\n")
print("Cheetah")
c=Cheetah("Brown",4,2);
c.eats()
print("The no of eyes the animal has is:-")
print(c.get_eyes())
c.eats()
print("The color of the animal is")
print(c.get_color())
print("Characteristics -")
c.characteristics()

