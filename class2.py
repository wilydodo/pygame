class Hello():
    def __init__(self,name):
            self.name = name
            #method
    def greeting(self):
        print("hello I'm "+self.name)
    def bye(self):
         print('さよなら')
a = Hello("엄준식")
a.greeting()
b = Hello("김정은")
b.greeting()
c = Hello("엄정현")
c.bye()