#클래스 만들기
class Fighter(object):
    def __init__(self,model,missile):
        self.model = model
        self.missile = missile
    def attack(self):
        print(self.model + " go!")
    def fire(self):
        print(self.missile + " fire!")

fighter1 = Fighter("ultimate great levolution darkness hell","dark energy")
fighter1.attack()
fighter1.fire()
fighter2 = Fighter("sans","gaster blaster")
fighter2.attack()
fighter2.fire()