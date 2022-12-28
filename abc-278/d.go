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
	aSl := intSliceInput(n)
	q := intInput()
	aMap := map[int]int{}
	for i, a := range aSl {
		aMap[i] = a
	}
	var initNum int
	for j := 0; j < q; j++ {
		num := intInput()
		if num == 1 {
			initNum = intInput()
			aMap = map[int]int{}
		}
		if num == 2 {
			i, x := intInput() - 1, intInput()
			if _, ok := aMap[i]; ok {
				aMap[i] += x
			} else {
				aMap[i] = initNum + x
			}
		}
		if num == 3 {
			if v, ok := aMap[intInput() - 1]; ok {
				fmt.Println(v)
			} else {
				fmt.Println(initNum)
			}
		}
	}
}
