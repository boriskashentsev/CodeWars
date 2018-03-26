func get_differences(_ sequence:[Int]) -> [Int] {
    var result:[Int] = []
    for i in 1..<sequence.count {
        result.append(sequence[i]-sequence[i-1])
    }

    return result
}

func get_dictionary_of_differences(_ diff:[Int]) -> [Int: Int] {
    var result: [Int:Int] = [:]
    for element in diff {
        if result[element] == nil {
            result[element] = 1
        }
        else {
            result[element]! += 1
        }
    }
    return result
}

func find_missing(l sequence:[Int]) -> Int {
    var result:Int = 0
    let diff:[Int] = get_differences(sequence)

    let dict:[Int:Int] = get_dictionary_of_differences(diff)
    let ordered_keys = dict.keys.sorted{ return abs($0) < abs($1) }

    let index:Int = diff.index(of: ordered_keys.last!)!

    result = sequence[index] + ordered_keys.first!

    return result
}
