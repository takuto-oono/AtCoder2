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

type UnionFind struct {
	parSl  []int
	sizeSl []int
}

func createStruct(n int) *UnionFind {
	uni := new(UnionFind)
	for i := 0; i < n; i++ {
		uni.parSl = append(uni.parSl, -1)
		uni.sizeSl = append(uni.sizeSl, 1)
	}
	return uni
}

func (uni *UnionFind) root(x int) int {
	if uni.parSl[x] == -1 {
		return x
	} else {
		uni.parSl[x] = uni.root(uni.parSl[x])
		return uni.parSl[x]
	}
}

func (uni *UnionFind) isSame(x, y int) bool {
	return uni.root(x) == uni.root(y)
}

func (uni *UnionFind) unite(x, y int) bool {
	x, y = uni.root(x), uni.root(y)
	if x == y {
		return false
	}
	if uni.sizeSl[x] < uni.sizeSl[y] {
		x, y = y, x
	}
	uni.parSl[y] = x
	uni.sizeSl[x] += uni.sizeSl[y]
	return true
}

func (uni *UnionFind) size(x int) int {
	return uni.sizeSl[uni.root(x)]
}

func main() {
	n := intInput()
	abSl := initSlSl(n, 2)
	CandidateMap := map[int]int{1: 0}
	cntCandidates := 1

	for i := 0; i < n; i++ {
		abSl[i][0], abSl[i][1] = intInput(), intInput()
		if _, ok := CandidateMap[abSl[i][0]]; !ok {
			CandidateMap[abSl[i][0]] = cntCandidates
			cntCandidates += 1
		}
		if _, ok := CandidateMap[abSl[i][1]]; !ok {
			CandidateMap[abSl[i][1]] = cntCandidates
			cntCandidates += 1
		}
	}

	uni := createStruct(cntCandidates)
	for i := 0; i < n; i++ {
		uni.unite(CandidateMap[abSl[i][0]], CandidateMap[abSl[i][1]])
	}
	ans := 1
	for k, v := range CandidateMap {
		if uni.isSame(CandidateMap[1], v) {
			ans = max(k, ans)
		}
	}
	fmt.Println(ans)
}
