'''
[문제분석]
    초미세먼지 농도에 따른 문자 메세지 발송
    초미세먼지 농도는 좋음입니다. : 15미만
    초미세먼지 농도는 보통입니다. : 15 ~ 35
    초미세먼지 농도는 나쁨입니다. : 35초과

[알고리즘]
    1. 초미세먼지 농도를 측정한다.(입력받는다.)
    2. 만약 초미세먼지 농도가 15미만이면
        2-1. 좋음
    3. 만약 초미세먼지 농도가 15 ~ 35 이면
        3-1. 보통
    4. 만약 초미세먼지 농도가 35 초과이면
        4-1. 나쁨
'''
dust = int(input("초미세먼지 농도를 입력하십시오 : "))

if dust < 15 :
    print("초미세먼지 농도는 좋음입니다.")
elif 15 <= dust <= 35 :
    print("초미세먼지 농도는 보통입니다.")
else :
    print("초미세먼지 농도는 나쁨입니다.")

if dust < 15 :
    print("초미세먼지 농도는 좋음입니다.")
if 15 <= dust <= 35 :
    print("초미세먼지 농도는 보통입니다.")
if dust > 35 : 
    print("초미세먼지 농도는 나쁨입니다.")
    
if dust < 15 :
    print("초미세먼지 농도는 좋음입니다.")
elif dust <= 35 :
    print("초미세먼지 농도는 보통입니다.")
else :
    print("초미세먼지 농도는 나쁨입니다.")

if dust < 15 :
    print("초미세먼지 농도는 좋음입니다.")
elif dust > 35 :
    print("초미세먼지 농도는 나쁨입니다.")
else :
    print("초미세먼지 농도는 보통입니다.")  