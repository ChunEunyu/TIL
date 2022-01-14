# say_myself.py

def say_myself (name, old, man=True):
    print("My name is %s."%name)
    print("My age is %d." %old)
    if man:
        print("man.")
    else:
        print("female.")

say_myself("Levi", 31)
say_myself("Levi", 31, True)
say_myself("Mikasa", 19, False)
