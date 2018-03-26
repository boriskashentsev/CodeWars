extension Array where Element == Int {
    static func *(left:[Int], right:[Int]) -> Int {
        var result = 0

        for i in 0...(left.count-1) {
            result += left[i] * right[i]
        }

        return result
    }
}

func goodWorth(_ numbers:[Int]) -> Int {
    let unitWorth = [1, 2, 3, 3, 4, 10]
    return numbers * unitWorth
}

func evilWorth(_ numbers:[Int]) -> Int {
    let unitWorth = [1, 2, 2, 2, 3, 5, 10]
    return numbers * unitWorth
}

func evaluate(good: String, vsEvil evil: String) -> String {
    let goodArmy = good.components(separatedBy: " ").flatMap{ Int( $0 ) }
    let evilArmy = evil.components(separatedBy: " ").flatMap{ Int( $0 ) }
    if goodWorth(goodArmy) > evilWorth(evilArmy) {
        return "Battle Result: Good triumphs over Evil"
    }
    else if goodWorth(goodArmy) < evilWorth(evilArmy) {
        return "Battle Result: Evil eradicates all trace of Good"
    }
    else {
        return "Battle Result: No victor on this battle field"
    }
}
