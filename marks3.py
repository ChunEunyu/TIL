#marks3.py

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] <60:
        continue
    else:
        print("%d번 학생 축하합니다. 합격입니다."%(number+1))
