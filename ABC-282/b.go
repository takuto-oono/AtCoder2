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

func judgeSolvingAllProblems(a, b string) bool {
	for i := 0; i < len(a); i++ {
		if !(a[i:i+1] == "o" || b[i:i+1] == "o") {
			return false
		}
	}
	return true
}

func main() {
	n, _ := intInput(), intInput()
	ans := 0
	sSl := []string{}
	for i := 0; i < n; i ++ {
		sSl = append(sSl, stringInput())
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if judgeSolvingAllProblems(sSl[i], sSl[j]) {
				ans += 1
			}
		}
	}
	fmt.Println(ans)
}
