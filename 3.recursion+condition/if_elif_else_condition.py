# 조건문 : 특정 조건을 만족할때 명령어를 수행하는 것
# if , if- elif -else

#시험점수에 따른 과락을 분류

score = int(input('점수를 입력하세요'))
if score>= 70:
    result = '통과'

elif score>= 60:
    result = '재시험'

else:
    result = '과락'

print (result)

# if elif else 구문의 구조

# if 조건문:
#     실행할 코드1
#     실행할 코드2
#     >>>
# elif 조건문:
#     실행할 코드3
#     실행할 코드4
#     실행할 코드5
# else 조건문
#     실행할 코드6
#     실행할 코드7