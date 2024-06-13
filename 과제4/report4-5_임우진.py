'''
    작성일 : 2024년 6월 4일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 실습예제 9-3     
'''
# 함수 선언
def dNumber(num, dnum_list) :
    for i in range(1, num+1) :
        if num % i == 0 :
            dnum_list.append(i)

# 메인
num = int(input("자연수를 입력하세요 : "))
dnum = []

if num > 0 :
    dNumber(num, dnum)
    print(num, "의 약수는 :", dnum)

else :
    print(num, "은 자연수가 아닙니다.")