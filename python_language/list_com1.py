#컴프리헨션: 반복문과 조건문을 한 줄로 간단하게 작성하여 리스트나 딕셔너리 세트를 만드는 방법

#1. 리스트 컴프리헨션
#[저장할 값(표현식) for 변수 in 반복할 데이터]
#[표현식 for 변수 in 반복할_데이터 if 조건식]
#[참일_때_값 if 조건식 else 거짓일_때_값 for 변수 in 반복할_데이터]
numbers= []
for i in range(1,6):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1,6)]
print(numbers)

mul = []
for i in range(1,6):
    mul.append(i*i)
print(mul)

mul = [i*i for i in range(1,6)]
print(mul)

even_num=[]
for i in range(1,11):
    if i % 2 == 0:
        even_num.append(i)
print(even_num)
even_num = [i for i in range(1,11) if i % 2 ==0]
print(even_num)

names=["홍길동", "장길동", "박길동"]
lengths=[len(a) for a in names]
print(lengths)

names=["홍길동", "장길동", "박길동"]
lengths=[]
for i in names:
    lengths.append(len(i))
print(lengths)

words=["apple", "banana", "kiwi", "pear"]
result= [i for i in words if len(i)>=5]
print(result)
print("개수: ",len(result))

res=["짝수" if i%2 ==0 else "홀수" for i in range(1,11)]
print(res)


# 딕셔너리 컴프리헨션 {키: 값 for 변수 in 반복할_데이터}

squars={i: i*i for i in range(1,6)}
print(squars)

scores={
    "김철수" : 85,
    "이영희" : 70,
    "홍길동" : 90
}

passed={i:j for i,j in scores.items()}
print(passed)
passed={i:j for j,i in scores.items()}
print(passed)


# 예제
num=[i*3 for i in range(1,11)]
print(num)

tri=[i for i in range(1,21) if i%3==0]
print(tri)

tri_num=[i if i%3==0 else 0 for i in range(1,21)]
print(tri_num)

mems={
    "김철수":35,
    "이영희":20,
    "홍길동":48
}
age={i:j for i,j in mems.items() if j>=30}
print(age)