package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var rdr = bufio.NewReaderSize(os.Stdin, 1000000)

func stringInput() string {
	sc.Scan()
	return sc.Text()
}

func intInput() int {
	sc.Scan()
	x, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return x
}

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func initSlSl(y, x int) [][]int {
	sl := make([][]int, y)
	if x == -1 {
		for i := 0; i < y; i++ {
			sl[i] = []int{}
		}
		return sl
	}
	for i := 0; i < y; i++ {
		sl[i] = make([]int, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

func main() {
	n := intInput()
	var s string
	fmt.Scan(&s)
	cntDoubleQuotation := 0
	var ansSl []byte
	for i := 0; i < n; i++ {
		if s[i:i+1] == "," {
			if cntDoubleQuotation%2 == 0 {
				ansSl = append(ansSl, '.')
			} else {
				ansSl = append(ansSl, ',')
			}
		} else if s[i:i+1] == "\"" {
			cntDoubleQuotation++
			ansSl = append(ansSl, '"')
		} else {
			ansSl = append(ansSl, s[i])
		}
	}
	fmt.Println(string(ansSl))
}
