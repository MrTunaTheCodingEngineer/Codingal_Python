def palind(r):
    e = len(r)-1
    s = 0
    while s<e:
        if r[s]!=r[e]:
            return False
        
        e -= 1
        s += 1
    return True

r = (2,4,1,5,7,3)

if (palind(r)):
    print("The Tuple is a flip flop")
else:
    print("The Tuple is not a flip flop")


