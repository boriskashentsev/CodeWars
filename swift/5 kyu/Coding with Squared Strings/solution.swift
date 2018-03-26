func appendString(_ s: String) -> (newString:String, n:Int) {
    var result = s
    let length = s.characters.count
    var n = 0
    if Int(sqrt(Double(length))) * Int(sqrt(Double(length))) != length {
        n = Int(sqrt(Double(length))) + 1
    } else {
        n = Int(sqrt(Double(length)))
    }

    var i = (n*n-length)

    while i > 0 {
        result.append("\u{F7}")
        i -= 1
    }

    return (result, n)
}

func codingString2square(_ str:String, _ n:Int) -> [String] {
    var result:[String] = []
    for i in 0..<n {
        let lowerBound = str.index(str.startIndex, offsetBy: i*n)
        let upperBound = str.index(str.startIndex, offsetBy: (i+1)*n)
        result.append( String(str[lowerBound..<upperBound]) )
    }
    return result
}

func code(_ s: String) -> String {
    let (str, n) = appendString(s)
    let square = codingString2square(str, n)
    var result = ""
    for i in 0..<n {
        var line = ""
        for j in 0..<n {
            line += String(square[n-1-j][ square[n-1-j].index(square[n-1-j].startIndex, offsetBy: i)])
        }
        result += (i != (n-1)) ? (line + "\n") : line
    }
    return result
}

func decodingString2square(_ str:String) -> ([String], Int) {
    let result: [String] = str.components(separatedBy: "\n")
    return (result, result[0].characters.count)
}

func decode(_ s: String) -> String {
    let (square, n) = decodingString2square(s)
    var result = ""
    for i in 0..<n {
        var line = ""
        for j in 0..<n {
            line += String(square[j][ square[j].index(square[j].startIndex, offsetBy: n-1-i)])
        }
        result += line
    }
    return result.components(separatedBy: "\u{F7}").first!
}
