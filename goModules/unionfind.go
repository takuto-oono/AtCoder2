package main

import "fmt"

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

func main() {
	uni := createStruct(8)
	uni.unite(1, 2)
	uni.unite(3, 4)
	uni.unite(5, 6)
	uni.unite(2, 3)
	fmt.Println(uni.isSame(1, 2))
	fmt.Println(uni.isSame(1, 4))
	fmt.Println(uni.isSame(4, 5))
	fmt.Println(uni.isSame(1, 7))
	fmt.Println(uni.parSlice)
	fmt.Println(uni.sizeSlice)
}
