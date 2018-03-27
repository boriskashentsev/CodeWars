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

def testing(value1, value2):
    if (value1 == value2):
        print ("You are wizard Harry!")
    else :
        print ("Dudley is behind you")

testing(solve("zodiac"),26)
testing(solve("chruschtschov"),80)
testing(solve("khrushchev"),38)
testing(solve("strength"),57)
testing(solve("catchphrase"),73)
testing(solve("twelfthstreet"),103)
testing(solve("mischtschenkoana"),80)