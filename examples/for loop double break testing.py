no = False

def forlooping(x,y):
    global no
    for n in range(x):
        print('x =',n)
        if no:
            print('changed')
            break
        for m in range(y):
            print('y=',m)
            if m > n:
                no = True
                print(n)
                break



forlooping(3,6)
print(no)



###########################################################

def forlooping(x,y):
    for n in range(x):
        print('x =',n)
        for m in range(y):
            print('y=',m)
            if m > n:
                break
        else:
            continue

        break


forlooping(3,6)



