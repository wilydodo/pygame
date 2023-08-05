name = "\"구도헌\""
#\뒤는 문자로 인식
ment = "안녕하세요?"
print(ment[-4:-2])
age = 13
pie = 3.14
t=True
f=False

print(name)

units=666
score=666
stamina="66666%"
life="66개"

print("파괴한 유닛 수: {},점수: {}".format(units,score))
print("체력: {},목숨: {}".format(stamina,life))

print(f"파괴한 유닛 수: {units},점수: {score}")
print(f"체력: {stamina},목숨: {life}")

list=[1,2,2.5,3,3.9,4,5,6,7,8,9,"sans",True]
food=["라면","목살","김치볶음밥"]
print(food)
food.append("김치찌개")
print(food)
food.append("민초")
print(food)
food.insert(0,"순대국밥")
print(food)
food.remove("목살")
print(food)
del(food[0])
print(food)

sport = ("농구","수영","볼링")
print(sport[0])
#리스트는 수정가능하지만 튜플은 안된다

people = {'name':'miku','age':16}
print(people["age"])