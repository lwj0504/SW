'''
    작성일 : 2024년 6월 4일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 코드 9-2          
'''
# 함수 선언
def morning1(name) :
    print(name,"씨 굿모닝입니다.")

def morning2(name) :
    s = name+"씨 굿모닝입니다."
    return s

def morning3(name) :
    s1 = "오늘 날씨가 쾌청합니다."
    s2 = name+"씨 굿모닝입니다."
    return s1, s2

# 메인
morning1("임우진")
s = morning2("임우진")
print(s)

s1, s2 = morning3("임우진")
print(s1, s2)