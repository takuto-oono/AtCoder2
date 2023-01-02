package main

import (
	"fmt"
	"math"
)

func calTimeReachGround(a, b, g float64) float64 {
	return (g-1)*b + a/math.Sqrt(g)
}

func min(x, y float64) float64 {
	if x < y {
		return x
	}
	return y
}

func main() {
	var a float64
	var b float64
	fmt.Scan(&a, &b)
	g := float64(int(math.Pow(a/(2*b), 2.0/3.0)))
	fmt.Println(min(calTimeReachGround(a, b, g), calTimeReachGround(a, b, g+1)))
}
