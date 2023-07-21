def fibonaaci(number):
    if number==0:
        return 0
    if number==1:
        return 1
    return fibonaaci(number-1)+fibonaaci(number-2)
number=int(input())
print(fibonaaci(number))