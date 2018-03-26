def find_uniq(arr):
    dict = {}
    for i in range(len(arr)) :
        if arr[i] not in dict :
            dict[arr[i]] = 1
        else :
            dict[arr[i]] += 1
    for key in dict.keys() :
        if dict[key] == 1:
            return key
