package main

import "math"

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func createBinarySearchSlice(n int) [][]int {
	binarySearchSl := make([][]int, pow(n, 2))
	for bits := 0; bits < (1 << uint64(n)); bits++ {
		sl := make([]int, n)
		for i := 0; i < n; i++ {
			if (bits>>uint64(i))&1 == 1 {
				sl[i] = 1
			}
		}
		binarySearchSl[bits] = sl
	}
	return binarySearchSl
}
