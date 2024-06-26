'''
    작성일 : 2024년 4월 19일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 패밀리 레스토랑에서 저녁 식사 후 음식 요금이 56000원 나왔다. 10%의 부가세를 포함한다면 지불해야 할 식사 금액이 얼마인지를 구하는 프로그램을 작성하시오.

    [문제분석]
        음식 요금 = 56000
        부가세 = 10%    # 1 / 10

        지불 식사 금액 = 음식 요금 + (음식 요금 * 부가세)

    [알고리즘]
        1. 음식 요금을 변수에 지정한다.
        2. 부가세를 변수에 지정한다.
        3. 지불 식사 금액을 계산한다.
        4. 지불 식사 금액을 출력한다.
'''
# 음식 요금 56000을 변수에 지정
basic_price = 56000
# 부가세(1/10)를 변수에 지정
tax = 1 / 10

# 지불 식사 금액을 계산
total_price = int(basic_price + (basic_price * tax))
# 지불 식사 금액을 출력
print(f"총 지불해야할 식사 금액은 {total_price}원 입니다.")