'''
    작성일 : 2024년 6월 4일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 코드 9-1
'''
# 함수 선언
def BigSmall(a, b) :
    if a > b :
        big = a
        small = b
    else :
        big = b
        small = a
    return big, small

# 메인
a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))

x, y = BigSmall(a, b)
print("큰 값 :", x)
print("작은 값 :", y)