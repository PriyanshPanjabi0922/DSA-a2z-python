# simple program:
count = 0

def verify():
    global count 

    if count == 4:
        return

    print(count)
    count+=1
    verify()

verify()