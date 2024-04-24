count = 0
sum = 0

while True :
    num = int(input(str(count + 1) + "번째 정수 입력 : "))
    
    if num > 0 :
        sum += num
        count += 1
        
    if count >= 10 :
        break
    
avg = sum / count
print("합계 : ", sum)
print("평균 : ", avg)