
func getGeneration(_ cells: [[Int]], generations: Int) -> [[Int]] {
  let dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  let dy = [0, 1, 1, 1, 0, -1, -1, -1]
  var gen = 0
  var curGen:[[Int]] = cells
  while gen < generations {
    var newGen = Array(repeating:Array(repeating: 0, count: curGen.first!.count+2), count: curGen.count+2)
    for i in 0..<newGen.count {
      for j in 0..<newGen.first!.count {
        var cell = 0
        if (i > 0 && i <= (curGen.count)) && (j > 0  && j <= (curGen.first!.count)) {
          cell = curGen[i-1][j-1]
        }
        var neighbours = 0
        for d in 0..<dx.count {
          if ((i + dx[d]) > 0 && (i + dx[d]) <= (curGen.count)) && ((j + dy[d]) > 0  && (j + dy[d]) <= (curGen.first!.count)) {
            neighbours += curGen[i-1+dx[d]][j-1+dy[d]]
          }
        }
        if cell == 0 && neighbours == 3 {
          newGen[i][j] = 1
        }
        else if cell == 1 {
          if neighbours < 2 || neighbours > 3 {
            newGen[i][j] = 0
          }
          else {
            newGen[i][j] = 1
          }
        }
      }
    }

    // Cut out frame if not needed
    // Lines from the top
    var isEmptyLine = true
    var numOfEmptyLinesTop = 0
    while isEmptyLine {
      if numOfEmptyLinesTop == newGen.count {
        return [[]]
      }
      for i in 0..<newGen[numOfEmptyLinesTop].count {
        if newGen[numOfEmptyLinesTop][i] == 1 {
          isEmptyLine = false
          numOfEmptyLinesTop -= 1 // Just to have correct number
          break;
        }
      }
      numOfEmptyLinesTop += 1
    }
    // Lines from the bottom
    isEmptyLine = true
    var numOfEmptyLinesBottom = 0
    while isEmptyLine {
      for i in 0..<newGen[newGen.count - 1 - numOfEmptyLinesBottom].count {
        if newGen[newGen.count - 1 - numOfEmptyLinesBottom][i] == 1 {
          isEmptyLine = false
          numOfEmptyLinesBottom -= 1
          break;
        }
      }
      numOfEmptyLinesBottom += 1
    }
    newGen.removeFirst(numOfEmptyLinesTop)
    newGen.removeLast(numOfEmptyLinesBottom)
    print (numOfEmptyLinesTop, numOfEmptyLinesBottom)
    // Rows from the left
    var isEmptyRow = true
    var numOfEmptyRowsLeft = 0
    while isEmptyRow {
      for i in 0..<newGen.count {
        if newGen[i][numOfEmptyRowsLeft] == 1 {
          isEmptyRow = false
          numOfEmptyRowsLeft -= 1
          break;
        }
      }
      numOfEmptyRowsLeft += 1
    }
    // Rows from the right
    isEmptyRow = true
    var numOfEmptyRowsRight = 0
    while isEmptyRow {
      for i in 0..<newGen.count {
        if newGen[i][newGen[i].count - 1 - numOfEmptyRowsRight] == 1 {
          isEmptyRow = false
          numOfEmptyRowsRight -= 1
          break;
        }
      }
      numOfEmptyRowsRight += 1
    }
    for i in 0..<newGen.count {
      newGen[i].removeFirst(numOfEmptyRowsLeft)
      newGen[i].removeLast(numOfEmptyRowsRight)
    }
    curGen = newGen
    gen += 1
  }
  return curGen
}

let cells = [[1,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]]
let cells = [[1,1],[1,1]]
let cells = [[1,0,0],[0,1,1],[1,1,0]]
let cells = [[1,1,1,0,0,0,1,0],[1,0,0,0,0,0,0,1],[0,1,0,0,0,1,1,1]]
getGeneration(cells, generations: 16)
