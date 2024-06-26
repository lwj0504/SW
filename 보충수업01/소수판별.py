'''
정수를 입력받아 그 수가 소수인지 아닌지 판별하시오.

[문제분석]
    소수는 1과 자기자신으로 나누어 떨어지는 수
                        (나머지가 0인 수)
    1을 제외하고 2부터 자기자신까지 나누어 나머지가 0인것을 확인하자.

    반복 조건 : 입력 수까지
    선택 조건 : 나누어 나머지가 0이면

[알고리즘]
    0. count의 초기값을 0으로 설정한다.
    1. 정수를 입력 받는다.
    2. 2부터 입력받은 수까지 반복하면서
        2-1. 입력수를 2부터 나누어 나머지가 0이면
            2-1-1. 개수를 증가시킨다.
    3. 개수가 1이면
        3-1. 00은 소수이다.
    4. 아니면
        4-1. 00은 소수가 아니다.
'''
num1 = int(input("소수인지 알고싶은 수를 입력하시오 : "))

count = 0
for num in range (2, num1+1, 1) :
    if num1 % num == 0 :
        count = count + 1

if count == 1 :
    print(f"{num1}은(는) 소수입니다.")
else :
    print(f"{num1}은(는) 소수가 아닙니다.")