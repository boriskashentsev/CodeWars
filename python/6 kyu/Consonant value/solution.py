def solve(s):
    vowels = "aeiou"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for vowel in vowels:
        s = s.replace(vowel, ' ')
    parts = s.split(' ')
    result = 0
    for part in parts:
        currentValue = 0
        for letter in part:
            currentValue += alphabet.find(letter) + 1
        if (currentValue > result):
            result = currentValue
    return result