print("상속, super,오버라이딩, 다형성")
# 부모클래스
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name, "직원이 일합니다")
    def print_info(self):
        print("이름:",self.name)
        print("급여:",self.salary,"원")

# 자식클래스
class Developer(Employee):# 상속
    def __init__(self, name, salary,language):
        # 부모 생성자 호출
        super().__init__(name, salary)
        # 자식만 있는 변수
        self.language= language
    # 오버라이딩(재정의)
    def work(self):
        print(self.name, "개발자가", self.language,"프로그램을 작성합니다.")
    def print_info(self):
        super().print_info()
        print("사용언어:",self.language)

# 자식클래스 2
# 선생님 -> 과목 subject
# ~선생님이 ~ 과목을 강의합니다
# 교과과목으로 과목도 출력(이름, 급여 포함 출력)
class Teacher(Employee):# 상속

    def __init__(self, name, salary, subject):        
        super().__init__(name, salary)

        # 자식2만 가지는 변수
        self.subject = subject

    # 부모의 work() 메서드를 재정의
    def work(self):
        print(self.name, "선생님이", self.subject, "과목을 강의합니다.")
    
    def print_info(self):
        super().print_info()
        print("교과 과목:", self.subject)

d= Developer("홍길동",4500000,"파이썬")
t= Teacher("장길동",3000000,"정보처리능력")

print("개발자 정보")
d.print_info()
print("\n교사 정보")
t.print_info()

print("\n직원들의 업무")
e_list=[d,t]
for e in e_list:
    e.work()
#자바 다형성: 부모타입=자식객체
#파이썬 다형성: 객체가 같은 이름의 함수를 갖고있음
