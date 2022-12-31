package main

import (
	"fmt"
)

var ansMap = make(map[int]int)

func f(x int) int {
	if x == 0 {
		return 1
	}
	if v, ok := ansMap[x]; ok {
		return v
	}
	ans := f(x / 2) + f(x / 3)
	ansMap[x] = ans
	for {
		if (x % 2 == 0 || x % 3 == 0) {
			break
		}
		ansMap[x] = ans
		x += 1
	}
	return ans
}

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(f(n))
	
	
}