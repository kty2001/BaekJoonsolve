# 10872 - 팩토리얼

n = int(input())
a = 1
for i in range(2, n+1):
    a *= i
print(a)