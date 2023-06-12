import sys


while True:
    line = sys.stdin.readline().rstrip('\n')

    if not line :
        break

    l , u , d , s = 0,0,0,0 #각각 소,대,숫자,공백

    for i in line:
        if i.islower():
            l +=1
        elif i.isupper():
            u +=1
        elif i.isdigit():
            d +=1
        elif i.isspace():
            s +=1

    print(l,u,d,s)