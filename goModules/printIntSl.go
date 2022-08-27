package main

import (
	"fmt"
	"strconv"
	"strings"
)

func printIntSlice(sl []int) {
	ans := make([]string, 0)
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ans, " "))
}
