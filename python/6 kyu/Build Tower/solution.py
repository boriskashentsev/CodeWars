def tower_builder(n_floors) :
    result = []
    for i in range(n_floors) :
        line = ' '*(n_floors-1-i) + '*'*(i*2+1) + ' '*(n_floors-1-i)
        result += [line]
    return result
