a = input("Introduce yourself.")



vowels = { 
"a" :0,
"e":0,
"o":0,
"i":0,
"u":0,
}

for letter in a:
    if letter in vowels:
        vowels[letter] += 1

print(vowels)