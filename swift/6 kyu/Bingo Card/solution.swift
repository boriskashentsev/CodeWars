import Foundation

func random(between min:Int, and max:Int) -> Int{
    let randomValue = Int(drand48() * Double(max - min + 1))
    return randomValue + min
}

func getColumn(with letter:String, min:Int, max: Int, amount: Int) -> [String] {
    var array:[Int] = []

    while array.count < amount {
        var nextRandom = random(between: min, and: max)

        while array.contains(nextRandom) {
            nextRandom = (nextRandom + 1 > max) ? min : nextRandom + 1
        }
        array.append(nextRandom)
    }

    return array.flatMap({ (number) -> String in
        return letter+String(number)
    })
}

func getCard() -> [String] {

    let bColumn = getColumn(with: "B", min: 1, max: 15, amount: 5)
    let iColumn = getColumn(with: "I", min: 16, max: 30, amount: 5)
    let nColumn = getColumn(with: "N", min: 31, max: 45, amount: 4)
    let gColumn = getColumn(with: "G", min: 46, max: 60, amount: 5)
    let oColumn = getColumn(with: "O", min: 61, max: 75, amount: 5)

    return bColumn + iColumn + nColumn + gColumn + oColumn
}
