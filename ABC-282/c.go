package main

import (
	"fmt"
)

func main() {
	var n int
	var s []byte
	fmt.Scan(&n)
	fmt.Scan(&s)
	flag := true
	for i := 0; i < n; i ++ {
		if s[i] == '"' {
			flag = !flag
		}
		if s[i] == ',' && flag {
			s[i] = '.'
		}
	}
	fmt.Println(string(s))
}
