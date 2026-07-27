age =5
if age <=0:
    raise ValueError("나이가 0보다 작거나 같으면 안됨")
print("나이:",age)

try:
    age=int(input("나이를 입력하세요 "))
    if age <=0:
        raise ValueError("나이가 0보다 작거나 같으면 안됨")
except ValueError as e:
    print("오류발생")
else:
    print("나이는:",age)
finally:
    print("끝")