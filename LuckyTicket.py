n = int(input())
n1 = int((n % 1000000)100000)
n2 = int((n % 100000)10000)
n3 = int((n % 10000)1000)
n4 = int((n % 1000)100)
n5 = int((n % 100)10)
n6 = int(n % 10)
if n1+n2+n3 == n4+n5+n6
    print(Счастливый)
else
    print(Обычный)