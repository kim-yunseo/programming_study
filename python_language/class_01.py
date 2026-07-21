print("클래스변수와 인스턴스변수")

class Student:
    s_name="중앙직업전문학교" #클래스 변수

    def __init__(self,name,score): #인스턴스변수
        self.name=name
        self.score=score

    def print_info(self):
        print("학교:", Student.s_name)
        print("이름:", self.name)
        print("점수:", self.score)

s1=Student("홍길동",90)
s2=Student("유관순",72)
s2.score=99
s1.print_info()
s2.print_info()

Student.s_name="글로벌 학교"
print("학교명:",Student.s_name)

print("\n"+"="*50)
print("파이썬의 함수 오버로딩")

class Calculator:

    def add(self,a,b):
        return a+b
    def add(self,a,b,c=100):
        return a+b+c

c1=Calculator()
print(c1.add(10,20,30))
#print(c1.add(100,200))
#파이썬에서는 같은 이름의 함수를 여러번 작성하면 마지막으로 작성한 함수만 남는다