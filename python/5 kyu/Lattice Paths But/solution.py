def lattice_paths(grid):
    rows = len(grid)
    cols = len(grid[0])
    countGrid = [[0]*cols for _ in range(rows)]
    countGrid[-1][-1] = 1
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if (grid[i][j]):
                if (i+1<rows):
                    countGrid[i][j] += countGrid[i+1][j]
                if (j+1<cols):
                    countGrid[i][j] += countGrid[i][j+1]
    return countGrid[0][0]

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ [[True, True, True, True],
    [True, True, True, True],
    [True, True, True, True]],                                         10 ],
         [ [[True, True, True, True],
    [True, False, True, True],
    [True, True, True, True]],                                         4 ],
         ]
  
for pattern, answer in tests:
    testing(lattice_paths(pattern), answer)