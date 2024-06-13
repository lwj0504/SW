'''
    학번을 입력받아 어느 학과 학생인지 알려주세요.
    학번은 학과 코드 영문자와 숫자로 구성되어 있습니다.

    예) C202095001
    [학과 코드]
    C : 컴퓨터공학과  A : 인공지능공학과   F : 식품영양학과

    입력받는 학과코드는 대소문자를 구분하지 않습니다.
    학과를 알려주는 부분은 함수로 작성하세요.

    [출력 결과]
        [학과 코드]
         C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과
        학번을 입력하세요 : c202095001 
        c202095001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : A202045001
        A202045001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : s202036001
        해당 학과는 없습니다.
'''
# 함수 선언
def dept(id_num) :
    if "C" in id_num or "c" in id_num :
        print(f"{id_num}학생은 컴퓨터공학과 소속입니다.")
    elif "A" in id_num or "a" in id_num :
        print(f"{id_num}학생은 인공지능공학과 소속입니다.")
    elif "F" in id_num or "f" in id_num :
        print(f"{id_num}학생은 식품영양학과 소속입니다.")
    else :
        print("해당 학과는 없습니다.")

# 메인
print("[학과 코드]")
print("C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과")

print()
id_num = input("학번을 입력하세요 : ")
dept(id_num)

print("=======================================")
# 함수
# 시작하는 글자가 c이면
# startswitch(시작하는 문자)
# endswitch(끝나는 문자)
def dept(id_num) :
    if id_num.startswith("c") == True or id_num.startswith("C") == True :
        print(f"{id_num}학생은 컴퓨터공학과 소속입니다.")
    elif id_num.startswith("a") == True or id_num.startswith("A") == True :
        print(f"{id_num}학생은 인공지능공학과 소속입니다.")
    elif id_num.startswith("f") == True or id_num.startswith("F") == True :
        print(f"{id_num}학생은 식품영양학과 소속입니다.")
    else :
        print("해당 학과는 없습니다.")

# 메인
print("[학과 코드]")
print("C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과")

print()
id_num = input("학번을 입력하세요 : ")
dept(id_num)