func maxBall(_ v0: Int) -> Int {
    let v:Double = Double(v0)
    let g:Double = 9.81

    return Int((10.0*v/(g*3.6)).rounded())
}
