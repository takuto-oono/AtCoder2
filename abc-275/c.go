package main

import (
	"fmt"
	"os"
	"sort"
	"strings"

	"gonum.org/v1/gonum/stat/combin"
)

func calLength(e []int) int {
	return e[0]*e[0] + e[1]*e[1]
}

func sortIntSlice(sl *[]int, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.IntSlice(*sl)))
	} else {
		sort.Sort(sort.IntSlice(*sl))
	}
}

func isSquare(coordinates [][]int) bool {
	a, b, c, d := coordinates[0], coordinates[1], coordinates[2], coordinates[3]
	ab := []int{a[0] - b[0], a[1] - b[1]}
	ac := []int{a[0] - c[0], a[1] - c[1]}
	ad := []int{a[0] - d[0], a[1] - d[1]}
	bc := []int{b[0] - c[0], b[1] - c[1]}
	bd := []int{b[0] - d[0], b[1] - d[1]}
	cd := []int{c[0] - d[0], c[1] - d[1]}

	lengths := []int{}
	lengths = append(lengths, calLength(ab))
	lengths = append(lengths, calLength(ac))
	lengths = append(lengths, calLength(ad))
	lengths = append(lengths, calLength(bc))
	lengths = append(lengths, calLength(bd))
	lengths = append(lengths, calLength(cd))

	sortIntSlice(&lengths, false)

	if lengths[0] != lengths[3] {
		return false
	}

	if lengths[4] != lengths[5] {
		return false
	}

	return lengths[4] == 2*lengths[1]
}

func main() {
	sSl := make([][]string, 9)
	n := 9
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		sSl[i] = strings.Split(s, "")
	}
	pawnCoordinates := [][]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if sSl[i][j] == "#" {
				pawnCoordinates = append(pawnCoordinates, []int{i, j})
			}
		}
	}
	if len(pawnCoordinates) < 4 {
		fmt.Println(0)
		os.Exit(0)
	}

	candidateSquares := combin.Combinations(len(pawnCoordinates), 4)
	ans := 0

	for _, candidateSquare := range candidateSquares {
		coordinates := make([][]int, 4)
		for i := 0; i < 4; i++ {
			coordinates[i] = pawnCoordinates[candidateSquare[i]]
		}

		if isSquare(coordinates) {
			ans += 1
		}
	}
	fmt.Println(ans)
}
