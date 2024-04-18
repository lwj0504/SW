'''
사용자로부터 정수를 입력받아 그 정수의 약수를 찾아주시오.

[문제분석]
    약수는 나누어 떨어지는 수(나머지가 0인 수)
    1부터 입력받은 수까지 나누었을 때 나머지가 0인 수들을 출력한다.

[알고리즘]
    1. 정수를 입력받는다.
    2. 1부터 입력받은 수까지 반복한다.
        2-1. 입력받은 수를 1부터 나누어 나머지가 0이면
            2-2. 수를 출력한다.
'''
num1 = int(input("약수를 알고싶은 수를 입력하시오 : "))

print("== for ==")
print(f"{num1}의 약수는 ", end='')
for num in range(1, num1+1, 1) :
    if num1 % num == 0 :
        print(num, end=" ")

print()

print("== while ==")
print(f"{num1}의 약수는 ", end='')
num = 1
while num <= num1 :
    if num1 % num == 0 :
        print(num, end=" ")
    num = num + 1