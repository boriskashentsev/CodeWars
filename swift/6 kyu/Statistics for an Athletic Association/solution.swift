extension Array where Element == SimpleTime {

    var total:Element {
        return reduce(SimpleTime(0), { (x: Element, y: Element) -> SimpleTime in
            SimpleTime(x.seconds() + y.seconds())
        })
    }

    var average:Element {
        return SimpleTime(total.seconds() / count)
    }

    var range:Element {
        return SimpleTime(last!.seconds()-first!.seconds())
    }

    var median:Element {
        if count % 2 == 0 {

            return [self[count / 2 - 1], self[count / 2]].average
        }
        else {
            return self[count / 2]
        }
    }
}

struct SimpleTime {
    let h:Int
    let m:Int
    let s:Int

    init (_ str: String) {
        let timeComponents = str.components(separatedBy: "|")
        guard let h = Int(timeComponents[0]),
            let m = Int(timeComponents[1]),
            let s = Int(timeComponents[2]) else {
                print("init String is not correct")
                fatalError()
        }
        self.h = h
        self.m = m
        self.s = s
    }

    init (_ seconds: Int) {
        self.h = seconds / 3600
        self.m = (seconds % 3600) / 60
        self.s = seconds % 60
    }

    func seconds() -> Int {
        return (h * 60 + m) * 60 + s
    }

    func printTime() -> String {
        let strH:String = String(format: "%02d", h)
        let strM:String = String(format: "%02d", m)
        let strS:String = String(format: "%02d", s)

        return strH + "|" + strM + "|" + strS
    }
}

func stat(_ strg: String) -> String {
    if strg == "" {
        return ""
    }

    let array = strg.components(separatedBy:",").flatMap{ SimpleTime($0) }

    let sortedArray = array.sorted { (lh, rh) -> Bool in
        return lh.seconds() < rh.seconds()
    }

    let range = sortedArray.range

    let average = sortedArray.average

    let median = sortedArray.median

    return "Range: " + range.printTime() + " Average: " + average.printTime() + " Median: " + median.printTime()
}
