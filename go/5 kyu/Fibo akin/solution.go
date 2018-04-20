package main

import "fmt"

func calculateUNth(n int, array []int) int {
	return array[n-array[n-1]]+array[n-array[n-2]]
}
func calculateU(n int) []int {
	array := make([]int, n)
	array[0] = 1
	array[1] = 1

	for i:=2; i<n; i++ {
		array[i] = calculateUNth(i, array)
	}

	return array
}

func LengthSupUk(n, k int) int {
	result:=0
	array := calculateU(n)
	for i:=0; i<n; i++ {
		if array[i] >= k {
			result ++;
		}
	}
	return result
}

func Comp(n int) int {
  result := 0
  array := calculateU(n)
  for i:=1; i<n; i++ {
	  if array[i-1] > array[i] {
		  result ++;
	  }
  }

  return result
}

func main() {
	array := calculateU(900)
	fmt.Println(array[len(array)-1] == 455)
	array = calculateU(90000)
	fmt.Println(array[len(array)-1] == 44337)
	fmt.Println(LengthSupUk(23, 12) == 4)
	fmt.Println(LengthSupUk(50, 10) == 35)
	fmt.Println(LengthSupUk(500, 100) == 304)

	fmt.Println(Comp(23) == 1)
	fmt.Println(Comp(100) == 22)
	fmt.Println(Comp(200) == 63)
}