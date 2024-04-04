'''
    작성일 : 2024년 3월 29일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 2개의 정수를 입력받아 두 수가 모두 짝수이면 더한 결과를 출력하고,
            둘 중 하나라도 홀수이면 몇 번쨰 수를 짝수로 입력해야 하는지 알려주시오.

    [문제분석]
        필요한 변수는 무엇? 2개 num1, num2
        입력받는 두 수는 모두 정수로 변환해야 한다.
        짝수는 2로 나눈 나머지가 0이다.
        홀수는 2로 나눈 나머지가 0이 아니다.
        두 수를 2로 나눠 짝수인지 홀수인지 판단한다.
        둘 다 짝수라면 두 수를 더하고 출력한다.
        두 수중 홀수가 있다면 "0 번쨰 수를 짝수로 입력하시오."를 출력한다.
        두 수 모두 홀수라면 "두 수를 짝수로 입력하시오."를 출력한다.

    [알고리즘]
        1. 첫 번째 수를 입력받아 정수로 변환하여 변수에 저장한다.
        2. 두 번째 수를 입력받아 정수로 변환하여 변수에 저장한다.
        3. 만약에 두 수를 2로 나눠 둘 다 짝수라면
            3-1. 두 수를 더한 값을 출력한다.
        4. 아니면 만약에 첫 번쨰 수가 홀수이고 두 번쨰 수가 짝수이면
            4-1. "첫 번쨰 수를 짝수로 입력하시오."를 출력한다.
        5. 아니면 만약에 첫 번쨰 수가 짝수이고 두 번쨰 수가 홀수이면
            5-1. "두 번쨰 수를 짝수로 입력하시오."를 출력한다.
        6. 아니면
            6-1. "두 수 모두 짝수로 입력하시오."를 출력한다.
'''

# 2개의 정수를 입력받아 각각 변수에 저장하시오.
num1 = int(input("첫 번쨰 수를 입력하시오. : "))
num2 = int(input("두 번째 수를 입력하시오. : "))

# 두 수를 2로 나눠 둘 다 나머지가 0이면 값을 더해 출력하시오.
# 두 수를 2로 나눠 첫 번쨰 수의 나머지가 0이 아니고 두 번쨰 수의 나머지가 0이면 "첫 번쨰 수를 짝수로 입력하시오."를 출력하시오.
# 두 수를 2로 나눠 첫 번쨰 수의 나머지가 0이고 두 번쨰 수의 나머지가 0이 아니라면 "두 번쨰 수를 짝수로 입력하시오."를 출력하시오.
# 아니라면 "두 수 모두 짝수로 입력하시오."를 출력하시오.
if num1 % 2 == 0 and num2 % 2 == 0 :
    print(f"두 수의 합은 {num1 + num2}입니다.")
elif num1 % 2 != 0 and num2 % 2 == 0 :
    print("첫 번쨰 수를 짝수로 입력하시오.")
elif num1 % 2 == 0 and num2 % 2 != 0 :
    print("두 번쨰 수를 짝수로 입력하시오.")
else :
    print("두 수 모두 짝수로 입력하시오.")