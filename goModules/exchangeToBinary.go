package main

import (
	"strconv"
)

func intToString(x int) string {
	return strconv.Itoa(x)
}

func exchangeToBinary(x int) int64 {
	i2, _ := strconv.ParseInt(intToString(x), 2, 0)
	return i2
}