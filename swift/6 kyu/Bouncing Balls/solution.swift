func bouncingBall(_ h: Double, _ bounce: Double, _ window: Double) -> Int {
    if (h <= 0) || (window >= h) || (bounce >= 1) || (bounce <= 0) {
        return -1
    }
    var curHeight: Double = h
    var result: Int = 1
    while true {
        curHeight = curHeight * bounce
        if curHeight > window {
            result = result + 2
        }
        else {
            break
        }
    }
    return result
}
