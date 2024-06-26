'''
    작성일 : 2024년 4월 23일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 사용자로부터 하나의 숫자를 입력받아 1부터 입력받은 숫자 사이의 소수를 구하여 출력하는 프로그램을 작성하시오. 

    [문제분석]
        정수를 입력받는다.
        1은 포함하지 않는다.
        소수 => 1과 자기 자신으로만 나누어 떨어지는 수

        입력받은 수까지 반복한다.
        count 0 초기화.
        나머지가 0이면 카운트 증가.
        break로 반복문 종료.
        카운트가 0인 수들만 해당 수를 출력한다.

    [알고리즘]
        1. 정수를 입력받는다.
        2. num을 2부터 입력받은 수+1까지 반복한다.
            2-1. count를 0으로 초기화 한다.
            2-2. i를 2부터 num까지 반복
                2-2-1. 만약 num을 i로 나눠 나머지가 0이면
                2-2-2. 카운트를 1 증가시킨다.
                2-2-3. 반복문을 종료한다.
            2-3. 만약 카운트가 0이면
                2-3-1. num을 출력한다.
'''
# 정수를 입력받아 변수에 저장
input_num = int(input("소수를 알고싶은 수를 입력하시오. : "))

# num을 2부터 입력받은 수+1까지 반복
# count = 0 초기화
# i를 2부터 num까지 반복
# num을 i로 나눠 나머지가 0이면 count 1 증가 후 반복문 종료
# count가 0이면 num 출력
print(f"1부터 {input_num}사이의 소수는 ",end='')
for num in range(2, input_num+1) :
    count = 0
    for i in range(2, num) :
        if num % i == 0 :
            count = count + 1
            break
    if count == 0 :
        print(num, end=' ')
print("입니다.")