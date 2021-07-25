for i in range(1,11):
    if(i%2== 0):
         print(i,"은/는 짝수입니다.")
    else  :
        print(i,"은/는 홀수입니다.")

# #for문의 구조
# for i in 범위
# 반복할 명령어1
# 반복할 명령어2

#for문 with list
mylist = ['해달이','사스미','메기']
 
for i in mylist:
    print(i)
print("반복 끝")

# for 문 with range 
#print list range
print(list(range(1,11))) 
print(list(range(10))) #시작점은 0부터 시작됨
print(list(range(1,20,3)))
print(list(list(range(20,0,-3))))

#for문 with Range
for i in range(1,11):
    print(i,end=" ")
print('반복끝')