func numberSum(_ n:Int) -> Int {
    var number = n
    var result = 0
    while number > 0 {
        result += number % 10
        number /= 10
    }
    return result
}

func orderWeight(_ s: String) -> String {
    let numbers: [Int] = s.components(separatedBy: " ").flatMap{ Int($0) }

    let sortedNumbers = numbers.sorted { (ln, rn) -> Bool in
        if (numberSum(ln) < numberSum(rn)) {
            return true
        }
        else if (numberSum(ln) > numberSum(rn)) {
            return false
        }
        else {
            if (String(ln) < String(rn)) {
                return true
            }
            return false
        }
    }

    let result = sortedNumbers.reduce("") { (result: String, number: Int) -> String in
        if (result == "") {
            return String(number)
        }
        else {
            return result + " " + String(number)
        }
    }

    return result
}
