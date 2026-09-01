import pandas as pd
# 2차원 구조(DataFrame)

score=pd.DataFrame([[100,30,40,55,77], [50,66,400,78,90], [20,78,99,80,70]], index=["java","python","c"])
print(score)
print("\n")

num=[1,2,3,4,5]
score2= pd.DataFrame(
    {
        "이름":["홍길동","이길동","장길동","오길동","최길동"],
        "자바":[100,30,40,55,77],"파이썬":[50,66,100,78,90],"c":[20,78,99,80,70]
    },index=num
)
print(score2)
print("\n")

print("처음 두 줄")
print(score2.head(2))
print("\n")
print("끝에 두 줄")
print(score2.tail(2))
print("\n")

print("index 기준 내림차순 정렬")
print(score2.sort_index(ascending=False))
print("\n")
print("이름 기준 오름차순 정렬")
print(score2.sort_values(by="이름",ascending=True))
print("\n")

print("자바 기준 내림차순 정렬")
score3=score2.sort_values(by="자바",ascending=False)
print(score3)

score3.to_csv("./score.csv", encoding="utf-8-sig")
