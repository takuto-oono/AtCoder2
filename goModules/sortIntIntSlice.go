package main

import (
	"sort"
)

func sortIntIntSlice(sl [][]int, index int, rev bool) {
	if rev {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] > sl[j][index] })
	} else {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] < sl[j][index] })
	}
}

