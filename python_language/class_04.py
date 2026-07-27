print("다중 상속과 mro")
class Login:
    def run(self):
        print("run() 실행")
    def login(self):
        print("login() 실행")

class Printer:
    def run(self):
        print("printer 클래스의 run() 실행")
    def print_info(self):
        print("프린트 합니다")

class Study(Login,Printer):
    def study(self):
        print("수업중입니다")

s=Study()
s.login()
s.print_info()
s.study()
s.run()        #Login클래스의 run실행
Printer.run(s) #Printer클래스의 run실행

print("함수 탐색 순서:")
print(Study.mro()) #클래스.mro(): 클래스 실행 순서를 리스트로 보여줌