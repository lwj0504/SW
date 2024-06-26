'''
    작성일 : 2024년 4월 20일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 10개의 정수를 입력받아 합을 구하는 프로그램을 for문을 사용하여 작성하시오. 단, 짝수 번째에 입력되는 숫자는 양수를 음수로, 음수를 양수로 바꾸어 합을 구하시오.

    [문제분석]
        짝수 = 2로 나누었을때 나머지가 0이 아닌것
        
        sum = 0 초기값 지정

        10번 반복한다.
        수를 입력받는다.
        만약 짝수 번째에 수를 입력받으면 -1을 곱하여 부호를 바꾼 후 합계에 더한다.
        아니라면 바로 합계에 더한다.

        합계를 출력한다.

    [알고리즘]
        1. sum = 0
        2. 10번 반복
            2-1. 정수를 입력받는다.
            2-2. 만약 num을 2로 나눴을때 나머지가 0이라면
                2-2-1. input_num * -1
                2-2-2. 합계를 계산
            2-3. 아니라면
                2-3-1. 합계를 계산
        3. 합계를 출력
'''
# sum 초기값 지정
sum = 0

# 10번 반복
# 만약 짝수 번째에 입력받으면 -1을 곱해 부호를 바꾸고, 아니라면 그대로 합계에 더하기
for num in range(1, 11) :
    input_num = int(input(f"{num}번째 정수를 입력하시오 : "))
    if num % 2 == 0 :
        input_num = input_num * -1
        sum = sum + input_num
    else :
        sum = sum + input_num

# 합계를 출력
print(f"입력된 수 10개중 짝수 번째에 입력된 수만 부호를 바꾼 총합은 {sum}입니다.")
    