str = input('Enter the string:')
l = str.split()
m = []
for i in l:
    if(str.count(i) > 1 and (i not in m) or str.count(i) == 1):
        m.append(i)
print(' '.join(m))        
