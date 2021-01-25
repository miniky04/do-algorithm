s = input()

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
count = 0

while s != '#':
    for vowel in vowels:
        count += s.count(vowel)
    print(count)
    count = 0
    s = input()
