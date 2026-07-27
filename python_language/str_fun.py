# s라는 객체를 출력하려고 하면 자동으로 __str__을 호출한다
class SimpleBook:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def __str__(self):
        return f"도서명: {self.title}, 가격: {self.price}원"

s=SimpleBook("파이썬 기초",25000)
print(s)