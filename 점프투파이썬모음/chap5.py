import random

result = []
for i in range(6):
    num = random.randint(1,45) # 난수를 생성하여 num 변수에 저장
    if num not in result: # num 값이 result리스트에 없는 수면
        result.append(num) # result리스트에 num값을 저장
print(result)
