'''
    작성일 : 2024년 6월 4일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 실습예제 9-2      
'''
# 함수 선언
def findPrime(x, y) :
    print(x, "부터", y, "사이의 소수 :", end=' ')
    count = 0

    for i in range(x, y+1) :
        for j in range(2, y+1) :
            if i % j == 0 :
                break
        if i == j :
            print(i, end=' ')
            count = count + 1
    print()
    return count

# 메인
num1 = int(input("첫 번째 숫자 입력(작은 수) : "))
num2 = int(input("두 번째 숫자 입력(큰 수) : "))

count = findPrime(num1, num2)
print("소수는 모두", count, "개 입니다.")