#정수형
a = 154
print(type(a))
a = 0
print(type(a))
a=-20
print(type(a))

# 실수형
b= 181.34   
print(type(b))
b= -22.34   
print(type(b))

# 복소수형

c = 1+4j
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c)) 

#사칙연산
a= 5
b=3.14
c= 3+4j
print(10*a+3*b+c)