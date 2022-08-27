package main

import (
	"math"
)

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}
func sqrt(n, m int) int {
	ans := 1
	for i := 1; i < n+1; i++ {
		if pow(i+1, m) > n {
			break
		}
		ans = i
	}
	return ans
}
