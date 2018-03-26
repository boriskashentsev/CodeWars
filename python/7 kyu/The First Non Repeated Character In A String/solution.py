def first_non_repeated(s):
    lst = list (s)
    while len(lst) > 0:
        char = lst[0]
        matches = [i for i,x in enumerate(lst[1:]) if x == char]
        if len(matches) == 0 :
            return char
        for elements in reversed(matches):
            lst.pop(elements+1)
        lst.pop(0)
    # shouldn't get here
    return None
