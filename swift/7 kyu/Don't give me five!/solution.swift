func dontGiveMeFive(_ start: Int, _ end: Int) -> Int {
    var result = 0
    for i in start...end {
        if (String(i).range(of: "5") == nil) {
            result += 1
        }
    }
    return result
}
