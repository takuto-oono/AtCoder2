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

func process1(aSl []int, k, x int) []int {
	aSl[k-1] = x
	return aSl
}

func process2(aSl []int, k int) {
	fmt.Println(aSl[k-1])
}

func main() {
	n := intInput()
	aSl := intSliceInput(n)
	q := intInput()
	for i := 0; i < q; i++ {
		if intInput() == 1 {
			k, x := intInput(), intInput()
			process1(aSl, k, x)
		} else {
			k := intInput()
			process2(aSl, k)
		}
	}
}
