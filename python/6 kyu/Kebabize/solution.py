def kebabize(string):
    #your code here
    pass

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
