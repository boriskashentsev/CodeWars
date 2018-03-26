func separate (_ n:Int) -> [Int] {
    var result:[Int] = []
    var number = n
    while number > 0 {
        result.insert(number % 10, at: 0)
        number /= 10
    }
    return result
}

func specialMin (_ arr:[Int]) -> (value:Int, index:Int) {
    let reverseArr = arr.reversed() as [Int]
    guard let minElement = arr.min(),
        let itsIndex = reverseArr.index(of: minElement) else {
            print ("HOW?")
            fatalError()
    }

    var newIndex = itsIndex
    while (newIndex < arr.count - 2) && (reverseArr[itsIndex] == reverseArr[newIndex + 1])  {
        newIndex += 1
    }

    return (minElement, arr.count-1-newIndex)
}

func specialMax(_ arr:[Int]) -> (value:Int, index:Int) {
    for i in 1...(arr.count-1) {
        if arr[0]<arr[i] {
            var newIndex = i-1

            return (arr[0], newIndex)
        }
    }
    return (arr[0], arr.count-1)
}

func insertDigits(_ numbers:[Int],_ ind1: Int,_ ind2: Int) -> [Int] {
    var result:[Int] = numbers

    let number = numbers[ind2]

    result.remove(at: ind2)
    result.insert(number, at: ind1)

    return result
}

func calculate(_ numbers:[Int]) -> Int {
    var result = 0
    for number in numbers {
        result = result * 10 + number
    }
    return result
}

func smallest(_ n: Int) -> (Int, Int, Int) {
    let arr = separate(n)
    print(n)
    var result: (Int, Int, Int) = (n, 0, 0)
    for i in 0...(arr.count-2) {
        let smallerArray = [] + arr[i...(arr.count-1)]
        let (_, indMin) = specialMin(smallerArray)
        let (_, indMax) = specialMax(smallerArray)

        if result.0 >= calculate(insertDigits(arr, indMax+i, i)) {
            result.0 = calculate(insertDigits(arr, indMax+i, i))
            result.1 = i
            result.2 = indMax + i
        }

        if result.0 > calculate(insertDigits(arr, i, indMin + i)) {
            result.0 = calculate(insertDigits(arr, i, indMin + i))
            result.1 = indMin + i
            result.2 = i
        }
    }

    if (result.0 == n) {
        return (n, 0, 0)
    }

    return result
}
