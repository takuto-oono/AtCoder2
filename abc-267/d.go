package main

import (
	"bufio"
	"fmt"
	"math"
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

type ABC267D struct {
	n       int
	m       int
	numbers []int
}

func createStruct() *ABC267D {
	n, m := intInput(), intInput()
	return &ABC267D{n: n, m: m, numbers: intSliceInput(n)}
}

func (abc267d *ABC267D) dp() int {
	dpSl := initSlSl(abc267d.n+1, abc267d.n+1)
	for i := 0; i < len(dpSl); i++ {
		for j := 0; j < len(dpSl[i]); j++ {
			dpSl[i][j] = math.MinInt
		}
	}
	dpSl[0][0] = 0

	for i := 1; i < abc267d.n+1; i++ {
		for j := 0; j < i+1; j++ {
			if j == 0 {
				dpSl[i][j] = 0
			} else {
				dpSl[i][j] = max(dpSl[i-1][j], dpSl[i-1][j-1]+abc267d.numbers[i-1]*j)
			}
		}
	}
	return dpSl[abc267d.n][abc267d.m]
}

func main() {
	abc267d := createStruct()
	fmt.Println(abc267d.dp())
}
