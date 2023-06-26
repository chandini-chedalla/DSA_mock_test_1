s = input()

char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1

for i, char in enumerate(s):
    if char_count[char] == 1:
        print(i)
        break
else:
    print("-1")
