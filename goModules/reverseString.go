package main

import (

)

func reverseString(s string) string {
	new := ""
	n := len(s)
	for i := 0; i < n; i ++ {
		new += s[n - i - 1:n - i]
	}
	return new
}