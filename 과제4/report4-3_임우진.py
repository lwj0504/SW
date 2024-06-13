'''
    작성일 : 2024년 6월 4일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 실습예제 9-2
'''
# 함수 선언
def findmax(a, b, c) :
    if a > b :
        biggest = a
    else :
        biggest = b
    
    if biggest < c :
        biggest = c

    return biggest

# 메인
a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))
c = int(input("세 번째 숫자 입력 : "))

biggest = findmax(a, b, c)
print("가장 큰 수는 :", biggest)