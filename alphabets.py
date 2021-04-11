str1 = input('Enter the string:')
str2 = ''
vaild = 'abcdefghijklmnopqrstuvwxyz'
for i in str1:
    if i in vaild:
       str2 += i
print(str2)                                          
