import random #random 모듈은 무작위로 숫자 생성 관련 모듈
a1 ="오늘도 행복해"
a2 ="폭설 주의하세요"
a3 ="오늘은 로또를 사세요"
a4 ="당신은 천재에요"
a5 ="영화 무료 쿠폰을 보내드립니다"

print(':::오늘의 운세:::')
input('엔터를 누르면 시작됩니다')
c = random.randint(1,5)
if c==1:
    print(a1)
elif c==2:
    print(a2)
elif c==3:
    print(a3)
elif c==4:
    print(a4)
elif c==5:
    print(a5)
