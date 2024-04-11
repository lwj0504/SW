'''
    작성일 : 2024년 4월 11일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 반복문 while
'''
# 1~10까지 출력하기
print("==== 반복문 while로 1부터 10까지 출력하기 1 ====")
# print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

num1 = 1    # 초기값. 숫자는 1부터
while num1 <= 10 :      # 조건식. 숫자를 10까지
    print(num1, end=', ')     # 반복하면서 할 일.
    num1 = num1 + 1     # 증감식. 숫자를 1씩 증가하면서
    # 증감식은 항상 반복문의 제일 마지막에 작성

print()     # 한 줄 바꿈

print("==== 반복문 while로 1부터 10까지 출력하기 2 ====")
num1 = 1    # 초기 값
num2 = 10   # 종료 값
while num1 <= num2 :    # 조건식
    print(num1, end=', ')     # 반복하면서 할 일.
    num1 = num1 + 1     # 증감식. 숫자를 1씩 증가하면서
    # 증감식은 항상 반복문의 제일 마지막에 작성

print()     # 한 줄 바꿈

print("반복문으로 자기 이름 10개 출력하기")
# 1. 임우진   2. 임우진   3.임우진
i = 1
while i <= 10 :
    print(i, end='. ')
    print("임우진")
    i = i + 1

j = 1
while j <= 10 :
    print(f"{j}. 임우진")
    j = j + 1