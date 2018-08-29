func currentSum(_ array: [Int]) -> Int {
  var result = 0
  for number in array {
    result += number * number
  }
  return result
}

func recursion(_ n: Int, _ array: [Int]) -> [Int] {
  var arCopy = array
  let rest = Double(n*n - currentSum(array))
  if rest <= 0 {
    return array
  }
  let biggestNextElement: Double = rest.squareRoot().rounded()
  if Int(biggestNextElement) >= array.last! || biggestNextElement < 1 {
    return array
  }
  else {
    for i in (1...Int(biggestNextElement)).reversed() {
      arCopy.append(i)
      arCopy = recursion(n, arCopy)
      if currentSum(arCopy) == n*n {
        return arCopy
      }
      arCopy.popLast()
    }
  }
  return array
}

func decompose(_ n: Int) -> [Int] {
  let rest = n*n
  let startValue = n-1
  var result: [Int] = []
  for i in (1...startValue).reversed() {
    result.append(i)
    let array = recursion(n, result)
    if currentSum(array) == rest {
      return array.reversed()
    }
    result.popLast()
  }
  return []
}

decompose(5) == [3, 4]
decompose(50) == [1,3,5,8,49]
decompose(625) == [2,5,8,34,624]
decompose(7654321) == [6, 10, 69, 3912, 7654320]
decompose(2) == []