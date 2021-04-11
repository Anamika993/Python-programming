str = input('Enter the string:')
for i in range(len(str)):
    count = 1
    for j in range(i + 1, len(str)):
        if(str[i] == str[j] and str[i] != ''):
            count += 1
            str = str[:j] + '0' + str[j + 1:]
    if(count > 1 and str[i] != '0'):
         print(str[i])
