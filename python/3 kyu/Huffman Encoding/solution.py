# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    hist = {} # histogram
    for char in s:
        if char not in hist:
            hist[char] = 1
        else :
            hist[char] += 1
    if len(hist.keys()) < 1 :
        return []
    # convert to list which will be pro manipulated
    freqs = []
    for key in hist.keys() :
        freqs.append((key, hist[key]))
    return freqs

def buildATree(freqs) :
    if freqs == None:
        return
    tree = []
    for element in freqs:
        tree.append([element[0], element[1]])
    tree = sorted(tree, key = lambda pair: pair[1], reverse = True) # sort by number of appearances
    if len(tree) > 1 :
        while len(tree) > 2 :
            newNode = [[tree[-2][0], tree[-1][0]], tree[-2][1] + tree[-1][1]]
            tree.pop()
            tree.pop()
            locs = [loc for loc, val in enumerate(tree) if val[1] >= newNode[1]]
            index = max(locs) if len(locs) > 0 else -1
            tree.insert(index + 1, newNode)
        tree = [tree[0][0], tree[1][0]]
        return tree
    else :
        return

def goDeep(node, prefix, dictionary):
    if len(node) > 1 :
        goDeep(node[0], prefix + "0", dictionary)
        goDeep(node[1], prefix + "1", dictionary)
    else :
        dictionary[node] = prefix

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    result = ""
    tree = buildATree(freqs)
    if tree == None:
        return
    charDict = {}
    goDeep(tree[0], "0", charDict)
    goDeep(tree[1], "1", charDict)
    for char in s :
        result += charDict[char]
    return result
  
# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs,bits):
    result = ""
    tree = buildATree(freqs)
    if tree == None:
        return
    ind = 0
    while ind < len(bits) :
        node = tree[int(bits[ind])]
        while len(node) > 1:
            ind += 1
            node = node[int(bits[ind])]
        result += node
        ind += 1
    return result

print "Test 1"
s = "aaaabcc"
fr = frequencies(s)
encoded = encode(fr, s)
print encoded
decoded = decode(fr, encoded)
print decoded
print decoded == s


print "Test 2"
s = "aaaabaaacbbbbccgdfgertebhsfsdvsnfjskdhgfsudhfjwekhbfjvsgvhkjshdjfklshjufgshjdfbhsjkdf"
fr = frequencies(s)
encoded = encode(fr, s)
print encoded
decoded = decode(fr, encoded)
print decoded
print decoded == s