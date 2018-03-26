func removNb(_ n: Int) -> [(Int,Int)] {
    var result:[(Int, Int)] = []

    let fullSum = n*(n+1)/2
    let minValue = Int(floor(Double(fullSum)/Double(n)))
    let maxValue = Int(floor(sqrt(Double(fullSum))))
    for i in minValue...maxValue {
        var curNumber = Int(round(Double(fullSum-i)/Double(i+1)))
        curNumber = curNumber > n ? n : curNumber
        if (fullSum-i-curNumber) == i*curNumber && curNumber != i{
            result.append((i, curNumber))
            result.append((curNumber,i))
        }
    }

    return result.sorted(by: { (a, b) -> Bool in
        let (a0,_) = a
        let (b0,_) = b
        return a0 < b0
    })
}
