'''
    작성일 : 2024년 3월 28일
    작성자 : 컴퓨터공학부 202495015 임우진
    설명 : 점수를 입력받아 80점 이상이면
            "당신의 점수는 80점 입니다." "좋은 성적입니다."를
            출력하는 프로그램을 작성하시오.

    [문제분석]
        점수를 입력받는다.
        입력 받는 길이를 정수로 변환한다.
        입력받은 점수를 변수에 저장한다.
        점수는 80점 이상이어야 한다.
        입력받은 점수가 80점 이상인가?
        80점 이상이면 메세지를 출력한다.

        필요한 변수 => score

    [알고리즘]
        1. 점수를 입력받는다.
        2. 점수가 80점 이상이면
            2-1. "당신의 점수는 00점 입니다.
                "좋은 성적입니다."
        3. "감사합니다."를 출력한다.
            =>조건과 상관없이 무조건 출력한다.
'''

# 점수를 입력받아 변수에 저장하시오.
score = int(input("점수를 입력하시오 : "))

# 입력받은 점수가 80점 이상이면 아래 문장을 출력하시오.
# 당신의 점수는 00점 입니다.
# 좋은 성적입니다.
# 점수에 상관없이 "감사합니다."를 출력하시오
if score >= 80 :
    print(f"당신의 점수는 {score}점 입니다.")
    print("좋은 성적입니다.")

print("감사합니다.")