package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

var simplePath = []int{}
var seen = []bool{}

func contains(sl []int, x int) bool {
	for _, v := range sl {
		if v == x {
			return true
		}
	}
	return false
}

func initSeen(n int) {
	for i := 0; i < n; i++ {
		seen = append(seen, false)
	}
}

func bfs(branches [][]int, x, y int) bool {
	seen[x] = true
	if contains(branches[x], y) {
		simplePath = append(simplePath, y)
		return true
	}
	for _, next := range branches[x] {
		if seen[next] {
			continue
		}
		if bfs(branches, next, y) {
			simplePath = append(simplePath, next)
			return true
		}
	}
	return false
}

func printIntSlice(sl []int) {
	ans := make([]string, 0)
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v + 1))
	}
	fmt.Println(strings.Join(ans, " "))
}

func main() {
	n, x, y := intInput(), intInput()-1, intInput()-1
	branches := make([][]int, n)

	initSeen(n)
	for i := 0; i < n-1; i++ {
		u, v := intInput()-1, intInput()-1
		branches[u] = append(branches[u], v)
		branches[v] = append(branches[v], u)
	}
	bfs(branches, y, x)
	simplePath = append(simplePath, y)
	printIntSlice(simplePath)

}
