 /**
  *   3____1
  *   |    |
  *   |    |
  *   0____2
  */
class Rectangle {
    constructor(coords) {
        this.x0 = coords[0]
        this.y0 = coords[1]
        this.x1 = coords[2]
        this.y1 = coords[3]
    }

    get p0() {
        return [this.x0, this.y0]
    }
    get p1() {
        return [this.x1, this.y1]
    }
    get p2() {
        return [this.x1, this.y0]
    }
    get p3() {
        return [this.x0, this.y1]
    }

    get points() {
        return [this.p0, this.p1, this.p2, this.p3]
    }

    get area() {
        return (this.x1-this.x0)*(this.y1-this.y0)
    }

    static areIntersecting(r1, r2) {
        return r1.p0[0] < r2.p1[0] && r1.p1[0] > r2.p0[0] && r1.p0[1] < r2.p1[1] && r1.p1[1] > r2.p0[1]
    }

    static intersectionRect(r1,r2) {
        const x1 = Math.max(r1.p0[0], r2.p0[0])
        const y1 = Math.max(r1.p0[1], r2.p0[1])
        const x2 = Math.min(r1.p1[0], r2.p1[0])
        const y2 = Math.min(r1.p1[1], r2.p1[1])
        return new Rectangle([x1,y1,x2,y2])
    }

    sameCorners(rect) {
        var number = [0, 0, 0, 0]
        for (var i = 0; i < 4; i++) {
            if (this.points[i][0] == rect.points[i][0] && this.points[i][1] == rect.points[i][1]) {
                number[i] = 1
            }
        }
        return number
    }

}

function getSum(total, num) {
    return total + num
}
/**
 *   .3.
 *   0 2
 *   .1.
 */
function cuttingEdge(corners, rect) {
    if (corners[0]==1 && corners[3]==1) {
        return [0, rect.p1[0]]
    } else if (corners[0]==1 && corners[2]==1) {
        return [1, rect.p1[1]]
    } else if (corners[1]==1 && corners[2]==1) {
        return [2, rect.p0[0]]
    }else if (corners[1]==1 && corners[3]==1) {
        return [3, rect.p0[1]]
    }
}

function cuttingCorner(corners, rect2cut, rect2leave) {
    var coords1 = []
    var coords2 = []
    if (corners[0]==1) {
        coords1 = [rect2cut.p0[0],rect2leave.p1[1],rect2leave.p1[0],rect2cut.p1[1]]
        coords2 = [rect2leave.p1[0],rect2cut.p0[1],rect2cut.p1[0],rect2cut.p1[1]]
    } else if (corners[1]==1) {
        coords1 = [rect2cut.p0[0],rect2cut.p0[1],rect2leave.p0[0],rect2cut.p1[1]]
        coords2 = [rect2leave.p0[0],rect2cut.p0[1],rect2cut.p1[0],rect2leave.p0[1]]
    } else if (corners[2]==1) {
        coords1 = [rect2cut.p0[0],rect2cut.p0[1],rect2leave.p0[0],rect2cut.p1[1]]
        coords2 = [rect2leave.p0[0],rect2leave.p1[1],rect2cut.p1[0],rect2cut.p1[1]]
    } else if (corners[3]==1) {
        coords1 = [rect2cut.p0[0],rect2cut.p0[1],rect2leave.p1[0],rect2leave.p0[1]]
        coords2 = [rect2leave.p1[0],rect2cut.p0[1],rect2cut.p1[0],rect2cut.p1[1]]
    }
    const newRects = [new Rectangle(coords1), new Rectangle(coords2)]
    return newRects
}

function cuttingThrough(rect2cut, rect2leave) {
    var coords1 = []
    var coords2 = []
    if (rect2cut.p0[0] > rect2leave.p0[0] && rect2cut.p1[0] < rect2leave.p1[0]) {
        coords1 = [rect2cut.p0[0], rect2cut.p0[1], rect2cut.p1[0], rect2leave.p0[1]]
        coords2 = [rect2cut.p0[0], rect2leave.p1[1], rect2cut.p1[0], rect2cut.p1[1]]
    }
    else if (rect2cut.p0[1] > rect2leave.p0[1] && rect2cut.p1[1] < rect2leave.p1[1]) {
        coords1 = [rect2cut.p0[0], rect2cut.p0[1], rect2leave.p0[0], rect2cut.p1[1]]
        coords2 = [rect2leave.p1[0], rect2cut.p0[1], rect2cut.p1[0], rect2cut.p1[1]]
    }
    else {
        console.log('---> NO WAY WE ARE HERE.')
    }
    const newRects = [new Rectangle(coords1), new Rectangle(coords2)]
    return newRects
}

function addNewRectangle(rects, rect) {
    var rect1 = rect
    var usedRect = false
    var j = 0
    while (j < rects.length) {
        if (Rectangle.areIntersecting(rects[j], rect1)) {
            var rect0 = rects[j]
            const overlap = Rectangle.intersectionRect(rect0, rect1)
            const r0Corners = rect0.sameCorners(overlap)
            const r1Corners = rect1.sameCorners(overlap)
            if (r1Corners.reduce(getSum) == 4) {
                usedRect = true
            }
            else if (r0Corners.reduce(getSum) == 4) {
                rects.splice(j,1)
                j--
            }
            else if (r1Corners.reduce(getSum) == 2) {
                var coords = rect1.p0.concat(rect1.p1)
                const edgeCutResult = cuttingEdge(r1Corners, rect0)
                coords[edgeCutResult[0]] = edgeCutResult[1]
                rect1 = new Rectangle(coords)
            }
            else if (r0Corners.reduce(getSum) == 2) {
                var coords = rect0.p0.concat(rect0.p1)
                const edgeCutResult = cuttingEdge(r0Corners, rect1)
                coords[edgeCutResult[0]] = edgeCutResult[1]
                rect0 = new Rectangle(coords)
                rects[j]=rect0
            }
            else if (r0Corners.reduce(getSum) == 1) {
                const cornerCutResult = cuttingCorner(r0Corners, rect0, rect1)
                rects = rects.slice(0,j).concat(cornerCutResult.concat(rects.slice(j+1, rects.length)))
                j++
            }
            else if (r0Corners.reduce(getSum) == 0 && r1Corners.reduce(getSum) == 0) {
                const throughCutResult = cuttingThrough(rect0, rect1)
                rects = rects.slice(0,j).concat(throughCutResult.concat(rects.slice(j+1, rects.length)))
                j++
            }
            else
            {
                console.log('---> HOW DID WE GET HERE??')
            }
        }
        j++
    }
    if (!usedRect) {
        rects.push(rect1)
    }
    return rects
}

function calculate(recs){
    var Rects = []
    for (var i=0; i<recs.length; i++) {
        Rects.push(new Rectangle(recs[i]))
    }
    Rects.sort(function(left,right){return left.area > right.area})

    var newRects = []
    for (var i=0; i<Rects.length; i++) {
        newRects = addNewRectangle(newRects, Rects[i])
    }

    var area = 0
    for (var i=0; i<newRects.length; i++) {
        area += newRects[i].area
    }
    return area
}

const {performance} = require('perf_hooks');
const t0 = performance.now();
result = calculate([ [ 1, 1, 2, 2 ],
    [ 1, 4, 2, 7 ],
    [ 1, 4, 2, 6 ],
    [ 1, 4, 4, 5 ],
    [ 2, 5, 6, 7 ],
    [ 4, 3, 7, 6 ] ])
console.log(result)
console.log(result == 21)
const t1 = performance.now();
console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")