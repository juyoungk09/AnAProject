class Hello:
    def hello_world(self):
        print("Hello World!")


a = Hello()
a.hello_world()

class ReallyBeatifulStar:
    def print_starpyramid(self):
        for i in range(10):
            print('*'*(i+1))

a = ReallyBeatifulStar()
a.print_starpyramid()

class Member:
    def __init__(self, ㅤ):
        self.name = ㅤ
    def member_me(self):
        print("제 이름은 {} 입니다.".format(self.name))
    

a = Member("김주영")
a.member_me()


class MyInfo:
    def __init__(self, ㅤ, ㅤㅤ, ㅤㅤㅤ):
        self.name = ㅤ
        self.age = ㅤㅤ
        self.where = ㅤㅤㅤ
    def introduce_me(self):
        print(f"저의 이름은 {self.name} 이고, 나이는 {self.age}살, 사는 곳은 {self.where} 입니다.")

a = MyInfo("김주영", 17, "인천")
a.introduce_me()


class Bread:
    def __init__(self, ㅤ, ㅤㅤ, ㅤㅤㅤ):
        self.name = ㅤ
        self.price = ㅤㅤ
        self.stock = ㅤㅤㅤ
    def buy(self):
        if self.stock == 0 :
            print("재고가 없습니다.")
        else :
            print("구매해주셔서 감사합니다.")
            self.stock -= 1
    def bake(self, ㅤ):
        self.stock += ㅤ
        print(f"{self.name}을/를 {ㅤ}개 만들었습니다.")
a = Bread("바게트", 1000, 10)
for i in range(15):
    a.buy()
a.bake(2)
print("!!!!!!!!")
class Bun(Bread):
    def __init__(self, ᅠ, ᅠᅠ, ᅠᅠᅠ, ㅤㅤㅤㅤ):
        super().__init__(ᅠ, ᅠᅠ, ᅠᅠᅠ)
        self.inside = ㅤㅤㅤㅤ
    def buy(self):
        super().buy()
    def bake(self, ᅠ):
        print("만들기 실패!!")
a = Bread("바게트", 2, 10)
a.bake(4)
for i in range(15):
    a.buy()

b = Bun("이상한거", 2, 5, "슈크림")
b.bake(3)
for i in range(10):
    b.buy()