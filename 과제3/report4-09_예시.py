num = int(input("숫자 입력 : ")) # 정수 입력 받기

for i in range(2, num+1) :      # i를 2부터 입력받은 수까지 반복
    count = 0                   # 매번마다 초기값 설정
    
    for j in range(1, i + 1) :  # j를 1부터 i까지 반복      # j는 나누는 수이다.
        if i % j == 0 :         # 만약 i를 j로 나눈 나머지가 0이면
            count += 1          # count 1 증가
            
    if count == 2 :             # 만약 count가 2이면        # 소수는 약수가 1과 자기 자신 뿐인 수라서 2 고정
        print(i)                # 출력
        
#################################################

for i in range(2, num + 1) :    # i를 2부터 입력받은 수까지 반복
    
    for j in range(2, i + 1) :  # j를 2부터 i까지 반복
        if i % j == 0 :         # 만약 i를 j로 나눈 나머지가 0이면
            break               # 반복문 종료
        
    if i == j :                 # 만약 i와 j가 같다면       # 자기 자신인지 확인
        print(i, end=' ')       # 출력