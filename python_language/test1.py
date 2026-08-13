scores = [65, 80, 95, 70, 88, 55]
av=sum(scores)/len(scores)
voav=0
pa=0
unpa=0
print("전체 학생 수: ",len(scores))
print("최고점수: ",max(scores))
print("최저점수: ",min(scores))
print("평균: ",round(av,1))
for i in scores:
    if (i>=av):
        voav+=1
    if (i>=70):
        pa+=1
    else:
        unpa+=1
print("평균 이상 학생 수:",voav)
print("합격자 수:",pa)
print("불합격자 수:",unpa)
print("내림차순 점수:",sorted(scores,reverse=True))