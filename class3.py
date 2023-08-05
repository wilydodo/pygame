class God():
    def __init__(self,name,age,country,height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def intro(self):
        print(f"my name is {self.name}, im {self.age} years old, Im from {self.country} and my height is {self.height}")

a = God("minedapple",29,"korean",169.9)
b = God("hatsune miku",16,"japan",174)
c = God("a",1,"a",111)
d = God("b",2,"b",222)
e = God("c",3,"c",333)

b.intro()