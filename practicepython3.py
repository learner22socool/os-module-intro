# Parent class
class Animal:
    def __init__(self, name,breed,age):   
        self.name = name
        self._breed=breed
        self.__age=age
         
         
    def speak(self):
        print(f"{self.name} makes a sound,he is part of {self.breed}")
        # child class
class Age(Animal)  :
    def year(self):
           print(f"{self.name} makes a sound,he is part of {self._breed} tribe, " f"they live up to the age of {self._Animal__age}")
# Child class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")

# d1 = Animal("Tommy","greman")
# d1.speak()    # Tommy barks
# d2 = Animal("momita","lebra")
# d2.speak()
# d3 = Animal("Toni","husky")
# d3.speak()


d1 = Age("Tommy","greman",12)
d1.year()    
d2 = Age("momita","lebra",13)
d2.year()
d3 = Age("Toni","husky",15)
d3.year()