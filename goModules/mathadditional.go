package main

import (
	"math"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func maxSlice(sl []int) int {
	if len(sl) == 0 {
		return 0
	}
	ans := sl[0]
	for _, x := range sl {
		if x > ans {
			ans = x
		}
	}
	return ans
}

func minSlice(sl []int) int {
	if len(sl) == 0 {
		return 0
	}
	ans := sl[0]
	for _, x := range sl {
		if x < ans {
			ans = x
		}
	}
	return ans
}

func pythonMod(x, y int) int {
	m := x % y
	if m < 0 {
		return m + y
	}
	return m
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func gcd(x, y int) int {
	if x > y {
		x, y = y, x
	}

	for x != 0 {
		x, y = y % x, x
	}
	return y
}

func lcm(x, y int) int {
	return x * y / gcd(x, y)
}
