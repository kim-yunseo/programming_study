print("sort()와 람다함수")
students  = [("홍길동",60), ("권율", 92), ("이순신", 88), ("유관순", 74)]
stu_list=sorted(students, key=lambda x:x[1])
print("오름차순")
print(stu_list)
for a in stu_list:
    print(a)

stu_list=sorted(students, key=lambda x:x[1],reverse=True)
print("내림차순")
print(stu_list)

print()
print("딕셔너리->리스트의 정렬")
stu=[{"name":"홍길동", "score":70}, {"name":"아이유", "score":88}, {"name":"변우석", "score":95}, {"name":"유재석", "score":52}]
stu_desc=sorted(stu, key=lambda x:x["score"], reverse=True)
print(stu_desc)
for a in stu_desc:
    print(a["name"],a["score"])