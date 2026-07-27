import math
import random
num=25

print("제곱근:",math.sqrt(num))
print("2의 세제곱",math.pow(2,3))
print("원주율:",math.pi)

student=["홍길동","권율","유관순","세종"]
sel=random.choice(student) #리스트 안에서 무작위 선택
dice=random.randint(1,6)   #1~6까지 안에서 무작위 선택

print("발표학생 선출:",sel)
print("주사위 숫자:",dice)