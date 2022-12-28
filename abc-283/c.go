package main

import (
	"fmt"
)


func main() {
	var s []byte
	fmt.Scan(&s)
	ans := len(s)
	isBeforeZero := false
	for _, c := range s {
		if c == '0' {
			if isBeforeZero {
				ans -= 1
			}
			isBeforeZero = !isBeforeZero
		} else {
			isBeforeZero = false
		}
	}
	fmt.Println(ans)
}