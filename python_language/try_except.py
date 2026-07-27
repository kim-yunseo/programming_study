try:
    num=int(input("숫자를 입력하세요 "))
    res=100/num
except ValueError:
    print("오류 숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except Exception as e:
    print("오류메시지",e)
else:
    print("결과는",res)
finally:
    print("프로그램 종료")