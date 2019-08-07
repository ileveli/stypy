def squsum(*args):
    sum = 0
    for i in args:
        sum += i * i
    print(sum)

squsum(1,2,3,4,5,6,7,8,9,10)