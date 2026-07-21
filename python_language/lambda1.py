# 1. 람다 함수란?
# 람다 함수는 "이름이 없는 짧은 함수"입니다.
# 일반 함수는 def를 사용하지만,
# 람다 함수는 lambda라는 단어를 사용합니다.
#람다 함수는 짧고 간단한 계산에 적합합니다.

# 일반 함수 형식
# def 함수이름(매개변수):
#     return 계산식
#
# 람다 함수 형식
# lambda 매개변수: 계산식

print("예제 1. 일반 함수와 람다 함수 비교")
print("*" * 60)

def double(x):
    return x*2

print(double(10))


b=lambda x : x*2
print(b(10))

print("")
print("계산 람다 함수")
print("*" * 60)

square=lambda x:x**2
print("5의 제곱",square(5))
print("10의 제곱",square(10))

add=lambda x,y:x+y
print("10+20=",add(10,20))

mul=lambda x,y:x*y
print("4*5=",mul(4,5))

print("")
print("조건식이 들어간 람다 함수")
print("*" * 60)

res=lambda x: "짝수" if x%2==0 else "홀수"
print(res(5))
print(res(10))

print("")
print("매개변수가 없는 람다 함수")
print("*" * 60)

h=lambda : "안녕하세요"
print(h())

a=lambda x,y: x if x>y else y
print(a(10,60))

# map()은 리스트의 값을 하나씩 꺼내
# 같은 계산을 반복할 때 사용합니다.
#
# 형식
# map(함수, 리스트)
#
# map()의 결과는 바로 리스트가 아니기 때문에
# list()를 사용하여 리스트로 바꿉니다.

print("")
print("고차함수")
print("*" * 60)

number = [1,2,3,4,5]
result = list(map(lambda x:x*2 , number)) #리스트로 끝남
print("원본:",number)
print("결과:",result)

score=[78,89,91,56]
score_result=list(map(lambda x:x+5,score))
print("원본:", score)
print("결과", score_result)

# filter()는 조건에 맞는 값만 골라냅니다.
#
# 형식
# filter(조건 함수, 리스트)
#
# 람다 함수의 계산 결과가 True이면 남기고,
# False이면 제외합니다.

num=[10,33,45,26,40,88]
num_list=list(filter(lambda x: x%3==0 , num))
print(num_list)

jumsu = [45,60,90,77,55]
a=list(filter(lambda x:x>=70, jumsu))
print(a)