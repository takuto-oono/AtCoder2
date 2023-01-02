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
	parSlice  []int
	sizeSlice []int
}

func createStruct(n int) *UnionFind {
	uni := new(UnionFind)
	for i := 0; i < n; i++ {
		uni.parSlice = append(uni.parSlice, -1)
		uni.sizeSlice = append(uni.sizeSlice, 1)
	}
	return uni
}

func (uni *UnionFind) root(x int) int {
	if uni.parSlice[x] == -1 {
		return x
	} else {
		uni.parSlice[x] = uni.root(uni.parSlice[x])
		return uni.parSlice[x]
	}
}

func (uni *UnionFind) isSame(x, y int) bool {
	return uni.root(x) == uni.root(y)
}

func (uni *UnionFind) unite(x, y int) bool {
	x = uni.root(x)
	y = uni.root(y)
	if x == y {
		return false
	}
	if uni.sizeSlice[x] < uni.sizeSlice[y] {
		x, y = y, x
	}
	uni.parSlice[y] = x
	uni.sizeSlice[x] += uni.sizeSlice[y]
	return true
}

func (uni *UnionFind) size(x int) int {
	return uni.sizeSlice[uni.root(x)]
}

func (uni *UnionFind) getParCnt() int {
	cnt := 0
	for _, par := range uni.parSlice {
		if par == -1 {
			cnt += 1
		}
	}
	return cnt
}

func isNext(a, b int) bool {
	ax, ay, bx, by := coordinates[a][0], coordinates[a][1], coordinates[b][0], coordinates[b][1]
	candidates := [][]int{
		{ax, ay - 1},
		{ax, ay + 1},
		{ax - 1, ay - 1},
		{ax - 1, ay},
		{ax + 1, ax + 1},
		{ax + 1, ay},
	}
	for i := 0; i < 6; i++ {
		if candidates[i][0] == bx && candidates[i][1] == by {
			return true
		}
	}
	return false
}

var n int
var coordinates [][]int

func main() {
	n = intInput()
	for i := 0; i < n; i++ {
		coordinates = append(coordinates, intSliceInput(2))
	}
	uni := createStruct(n)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if isNext(i, j) {
				uni.unite(i, j)
			}
		}
	}
	fmt.Println(uni.getParCnt())
}
