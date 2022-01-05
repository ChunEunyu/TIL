
f1 = open("c:/doit/test.txt", 'w')
f1.write("Life is too short\n")
f1.write("you need java")
f1.close()

f2 = open("c:/doit/test.txt", 'r')
data=f2.read()
data=data.replace("java","python")
f2.close()

f3=open("c:/doit/test.txt", 'w')
f3.write(data)
f3.close()
