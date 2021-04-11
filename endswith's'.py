def endingwith(str, suff):
    c = 0
    wrd = str.split(' ')
    for i in wrd:
        if i.endswith(suff):
            c += 1
    return c
str = input('Enter the string:')
suff = 's'
print(endingwith(str, suff))
