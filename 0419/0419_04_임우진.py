'''
    작성일 : 2024년 4월 19일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 숫자 맞추기 게임
            컴퓨터에 1~10 사이의 숫자를 정해두고,
            사용자에게는 5번의 기회를 줍니다.
            사용자는 컴퓨터가 가지고 있는 숫자를 맞추고
            몇 번만에 맞췄는지 알려줍니다.

    [문제분석]
        컴퓨터에 1~10 사이 숫자를 정한다. => 랜덤 수 생성.
        사용자 기회는 총 5번이고, 한번 틀릴 때마다 기회는 감소한다.
        사용자가 1회에 맞추면 게임 종료된다. break 사용.
            =>2, 3, 4, 5회는 없다.
        이 게임은 사용자가 5회 안에 맞추거나
        5회가 넘으면 게임 종료

    [알고리즘]
        1. 1~10 사이 랜덤 숫자를 변수에 저장한다.
        2. 기회는 5번이다.  5번 반복하면서
            2-1. 사용자에게 정수를 입력받는다.
            2-2. 만약 입력받은 정수가 랜덤 숫자와 같다면
                2-2-1. 몇 번만에 맞췄는지 출력한다. (반복 횟수)
                2-2-2. 반복을 종료한다.
            2-3. 아니라면
                2-3-1. 오답 메세지를 출력한다.
        3. 정답을 알려준다.
'''
import random # 랜덤 수 사용하기 위한 함수 불러오기

# 1~10 사이 랜덤 수 발생하기 => 변수에 저장
comNum = random.randint(1, 10)

for count in range(1, 6) :
    userNum = int(input("숫자 입력 : "))
    if userNum == comNum :
        print(f"{count}번 만에 맞췄습니다.")
        break
    else :
        print("오답입니다.")

print(f"정답은 {comNum}입니다.")