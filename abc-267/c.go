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

func createCumulativeSumSl(sl []int) []int {
	res := []int{0}
	sum := 0
	for _, num := range sl {
		sum += num
		res = append(res, sum)
	}
	return res
}

func main() {
	n, m := intInput(), intInput()
	aSl := intSliceInput(n)
	cumulativeSumASl := createCumulativeSumSl(aSl)
	ans, x := 0, 0

	for i := 0; i < n-m+1; i++ {
		if i == 0 {
			for j := 0; j < m; j++ {
				x += (j + 1) * aSl[j]
				ans = x
			}
			continue
		}
		x -= cumulativeSumASl[i+m-1] - cumulativeSumASl[i-1]
		x += m * aSl[i+m-1]
		ans = max(x, ans)
	}
	fmt.Println(ans)
}
