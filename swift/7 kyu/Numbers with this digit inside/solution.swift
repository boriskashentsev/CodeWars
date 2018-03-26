func doesNumber(_ x: Int64, containsNumber d:Int64) -> Bool {
    var xLocal = x
    while xLocal > 0 {
        if(xLocal % 10 == d) {
            return true
        }
        xLocal = xLocal / 10
    }
    return false
}

func numbersWithDigitInside(_ x: Int64, _ d: Int64) -> [Int64] {
    var result: [Int64] = [0,0,0]
    for number in 1...x {
        if doesNumber(number, containsNumber: d) {
            if (result[0] == 0) {
                result = [0, 0, 1]
            }
            result[0] = result [0] + 1
            result[1] = result [1] + number
            result[2] = result [2] * number
        }
    }
    return result
}
