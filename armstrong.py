n = input('Enter the number')
i = 0 
ln = len(n)
s = 0
while i<ln:
    s += int( n[i])**ln
    i+=1

if int(n)==s:
    print('number is armstrong')
    
else:
    print('not armstrong')
