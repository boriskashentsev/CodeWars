func countTargets(_ n: Int, _ sequence: [Int]) -> Int {
    var result:Int = 0
    var index: Int = 0
    while index < (sequence.count - n) {
        result = (sequence[index] == sequence[index + n]) ? result + 1 : result
        index = index + 1
    }

    return result
}
