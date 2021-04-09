n = input('Enter the string:')
vowels = 0
consonants = 0
whitespace = 0
digit = 0
n = n.lower()
for i in range (len(n)):
    if(n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u'):
        vowels += 1
    elif((n[i] >= 'a' and n[i] <= 'z')):
        consonants += 1
    elif(' '):
        whitespace += 1
    else:
        digit += 1
       
print('Vowels',vowels)
print('Consonants',consonants)
print('Whitespace',whitespace)
print('Digits',digit)
