# 조건문 : 특정 조건을 만족할때 명령어를 수행하는 것
# if , if- elif -else

#시험점수에 따른 과락을 분류

score = int(input('점수를 입력하세요'))
if score>= 70:
    result = '통과'
else:
    result = '과락'

print (result)

#if 문의 구조
#if 조건문:
#  실행할 코드 1
#  실행할 코드 2
