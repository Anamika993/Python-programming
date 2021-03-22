n = int(input('Enter the number'))
i = 0
while(i<=n):
    if n%5 == 0:
        if n%2 == 0:
            continue
        print(i, end = ' ')
    i+=1
