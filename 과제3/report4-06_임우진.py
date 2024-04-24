'''
    작성일 : 2024년 4월 20일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 10개의 수를 입력받아 0보다 큰 수에 대해서만 전체 합과 평균을 출력하는 프로그램을 while 반복문을 이용하여 작성하시오.

    [문제분석]
        sum = 0 초기값 지정
        num = 1 초기값 지정

        num <= 10까지 반복한다.
        수를 입력받는다.
        만약 수가 0보다 크다면 합계에 더하고 count를 1 올린다.  # sum = sum + input_num

        평균을 구한다.
        평균 = sum / count
        
        합계와 평균을 출력한다.

    [알고리즘]
        1. sum = 0
        2. num = 1
        3. count = 0
        4. num <= 10까지 반복
            4-1. 정수를 입력받아 변수에 저장
            4-2. 만약 정수가 0보다 크다면
                4-2-1. 합계를 계산
                4-2-2. count 1 증가
            4-3. num = num + 1
        5. 평균을 계산  # average = sum / count
        6. 합계와 평균을 출력
        
'''
# sum과 num과 count의 초기값 지정
sum = 0
num = 1
count = 0
# 10번 반복
# 정수를 입력받아 변수에 저장
# 정수가 0보다 크다면 합계에 더하고 count + 1
while num <= 10 :
    input_num = int(input(f"{num}번째 정수를 입력하시오 : "))
    if input_num > 0 :
        sum = sum + input_num
        count = count + 1
    num = num + 1

# 평균을 변수에 저장
average = sum / count
# 합계와 평균을 출력
# 소수는 2자리까지 출력
print(f"입력된 수 10개중 0보다 큰 수의 합은 {sum}이고, 평균은 {average:.2f}입니다.")