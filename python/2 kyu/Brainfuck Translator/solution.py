def char_to_c(char, repetition, numberOfSpaces):
    if char == "+":
        return ((" " * numberOfSpaces) + "*p += " + str(repetition) +";\n", numberOfSpaces)
    if char == "-":
        return ((" " * numberOfSpaces) + "*p -= " + str(repetition) +";\n", numberOfSpaces)
    if char == ">":
        return ((" " * numberOfSpaces) + "p += " + str(repetition) +";\n", numberOfSpaces)
    if char == "<":
        return ((" " * numberOfSpaces) + "p -= " + str(repetition) +";\n", numberOfSpaces)
    if char == ".":
        return ((" " * numberOfSpaces) + "putchar(*p);\n", numberOfSpaces)
    if char == ",":
        return ((" " * numberOfSpaces) + "*p = getchar();\n", numberOfSpaces)
    if char == "[":
        return ((" " * numberOfSpaces) + "if (*p) do {\n", numberOfSpaces+2)
    if char == "]":
        return ((" " * (numberOfSpaces-2)) + "} while (*p);\n", numberOfSpaces-2)

def clean_brainfuck_to_c(cleanSource) :
    numberOfSpaces = 0
    index = 0
    result = ""
    while index < len(cleanSource):
        char = cleanSource[index]
        if char in "+-<>" :
            repetition = 1
            index += 1
            while index < len(cleanSource) and cleanSource[index] == char:
                repetition += 1
                index += 1
            (translation, numberOfSpaces) = char_to_c (char, repetition, numberOfSpaces)
            result += translation
        else:
            (translation, numberOfSpaces) = char_to_c (char, 0, numberOfSpaces)
            result += translation
            index += 1
    return result

def brainfuck_to_c(source_code):
    indexResult = -1
    result = [""]
    index = 0
    numOfSqrBrackets = 0
    while  index < len(source_code) :
        char = source_code[index]
        if char in "+-<>,.[]" :
            if indexResult >= 0:
                charInResult = result[indexResult]
                if char == "[" :
                    numOfSqrBrackets += 1
                elif char == "]" :
                    numOfSqrBrackets -= 1
                    if numOfSqrBrackets < 0:
                        return "Error!"

                if ((char == "+" and charInResult =="-") or (char == "-" and charInResult == "+") or
                    (char == "<" and charInResult ==">") or (char == ">" and charInResult == "<") or
                    (char == "]" and charInResult == "[") ) :
                    indexResult -= 1
        else :
            if indexResult + 1 < len(result) :
                result[indexResult + 1] = char
                    else :
                        result.append(char)
                indexResult += 1
        else :
            if char == "[" :
                numOfSqrBrackets += 1
                elif char == "]" :
                    numOfSqrBrackets -= 1
                    if numOfSqrBrackets < 0:
                        return "Error!"
            indexResult = 0
                result[indexResult] = char
index += 1

    if numOfSqrBrackets > 0 :
        return "Error!"
elif indexResult < 0 :
    return ""
    else :
        return clean_brainfuck_to_c(result[:indexResult+1])
