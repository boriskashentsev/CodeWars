package main

import (
	"math"
	"fmt"
)

func abs(x int) int{
	return int(math.Abs(float64(x)))
}

func gcd(x,y int) int {
	if (y == 0 || x == y) {
		return x
	}
	return gcd(y, x % y)
}

func Gcdi(x, y int) int {
    return gcd(Maxi(abs(x), abs(y)), Mini(abs(x), abs(y)))
}
func Som(x, y int) int {
    return x + y
}
func Maxi(x, y int) int {
    if x >= y {
		return x
	}
	return y
}
func Mini(x, y int) int {
    if x <= y {
		return x
	}
	return y
}
func Lcmu(x, y int) int {
	return (abs(x) * abs(y)) / Gcdi(x,y)
}

type FParam func(int, int) int
func OperArray(f FParam, arr []int, init int) []int {
	result := make([]int, len(arr)+1)
	result[0] = init

	for i:=1; i<=len(arr); i++ {
		result[i] = f(result[i-1], arr[i-1])
	}

	return result[1:len(result)]
}

func dotest(f FParam, arr []int, init int, exp []int) {
	var ans = OperArray(f, arr, init)
	fmt.Println(ans)
	fmt.Println(exp)
	
}

func main() {
	var dta = []int{ 18, 69, -90, -78, 65, 40 }
	var sol = []int{18, 3, 3, 3, 1, 1}
	dotest(Gcdi, dta, dta[0], sol);

	dta = []int{357, 112, 28, -52, 644, 119}
	sol = []int{357, 469, 497, 445, 1089, 1208}
	dotest(Som, dta, 0, sol)

	dta = []int{10, -32, 190, 300, -42, -38, 50, 405, -46, 225, -31}
	sol = []int{10, 10, 190, 300, 300, 300, 300, 405, 405, 405, 405}
	dotest(Maxi, dta, dta[0], sol)

	dta = []int{6, -72, -62, -22, -23, 80}
	sol = []int{6, 72, 2232, 24552, 564696, 5646960}
	dotest(Lcmu, dta, dta[0], sol)

	dta = []int{64, -67, -43, 12, -15, 108, 12, 104, -36}
	sol = []int{64, -67, -67, -67, -67, -67, -67, -67, -67}
	dotest(Mini, dta, dta[0], sol)
}