func race(_ v1: Int, _ v2: Int, _ g: Int) -> [Int]? {
    if (v1 >= v2) {
        return nil
    }

    let seconds = g * 3600 / (v2-v1)

    return [seconds / 3600, (seconds % 3600) / 60, seconds % 60]

}
