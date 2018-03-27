def kebabize(string):
    result = ""
    for char in string:
        if (char.isalpha()):
            if (char.isupper()):
                result += "-" + char.lower()
            else:
                result += char
    if (result != '')and(result[0] == "-"):
        result = result[1:]
    return result
    