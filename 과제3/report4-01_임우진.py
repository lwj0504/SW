'''
    작성일 : 2024년 4월 19일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 30분에 2100자를 입력할 수 있는 사람이 45분 동안 몇 자를 입력할 수 있는지를 구하는 프로그램을 작성

    [문제분석]
        45분 = 30분 * 1.5
        45분에 입력할 수 있는 글자 수 = 2100자 * 1.5

    [알고리즘]
        1. 30분에 입력할 수 있는 글자 수를 지정한다.
        2. 글자 수에 1.5를 곱하여 45분에 입력할 수 있는 글자 수를 계산하여 변수에 저장한다.
        3. 결과를 출력한다.
'''
# 30분에 입력할 수 있는 글자 수 2100을 변수에 지정
typing1 = 2100

# 45분에 입력할 수 있는 글자 수 = 30분에 입력할 수 있는 글자 수 * 1.5
typing2 = int(typing1 * 1.5)
# 45분에 입력할 수 있는 글자 수를 출력
print(f"45분에 입력할 수 있는 글자 수는 {typing2}자 입니다.")