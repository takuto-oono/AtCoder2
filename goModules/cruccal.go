package main

import (
	"sort"
)

type UnionFind struct {
	parSlice  []int
	sizeSlice []int
}

func (uni *UnionFind) createStruct(n int) {
	for i := 0; i < n; i++ {
		uni.parSlice = append(uni.parSlice, -1)
		uni.sizeSlice = append(uni.sizeSlice, 1)
	}
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

type Edge struct {
	weight int
	pair   []int
}

func sortEdgeByWeight(edges []Edge) []Edge {
	sort.Slice(edges, func(i, j int) bool {
		return edges[i].weight > edges[j].weight
	})
	return edges
}

func cruccal(edges []Edge, n int) int {
	uf := new(UnionFind)
	uf.createStruct(n)
	ans := 0
	for _, edge := range edges {
		w := edge.weight
		u := edge.pair[0]
		v := edge.pair[1]
		if (uf.isSame(u, v)) {
			continue
		}
		ans += w
		uf.unite(u, v)
	}
	return ans
}
