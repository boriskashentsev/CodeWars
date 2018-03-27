def kebabize(string):
    result = ""
    for char in string:
        if (char.isalpha()):
            if (char.isupper()):
                result += "-" + char.lower()
            else:
                result += char
    #print result
    if (result != '')and(result[0] == "-"):
        result = result[1:]
    return result

def testing(value1, value2): 
    if (value1 == value2):
        print "Yep"
    else:
        print "Nope"

testing(kebabize('myCamelCasedString'), 'my-camel-cased-string')
testing(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
testing(kebabize('SOS'), 's-o-s')
testing(kebabize('42'), '')
testing(kebabize('CodeWars'), 'code-wars')
