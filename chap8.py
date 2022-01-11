f = open('sample.txt', 'r')
lines = f.readlines()    # 모든 라인을 읽음
f.close()

total=0
for line in lines:
    score = int(line)
    total += score

avg = total/len(lines)

f=open("result.txt", "w")
f.write(str(avg))
f.close()
