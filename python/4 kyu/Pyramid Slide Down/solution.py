def longest_slide_down(pyramid):
    for depth in range(len(pyramid)-2,-1,-1):
        for width in range(len(pyramid[depth])):
            pyramid[depth][width] += max(pyramid[depth+1][width], pyramid[depth+1][width+1])
    return pyramid[0][0]
