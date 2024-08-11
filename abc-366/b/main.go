package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	n := inputIntSl()[0]
	sSl := inputCharSlSl(n)
	maxLenS := 0
	for _, s := range sSl {
		maxLenS = max(maxLenS, len(s))
	}

	tSl := make([][]string, maxLenS)
	for i := 0; i < maxLenS; i++ {
		tSl[i] = make([]string, n)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < len(sSl[i]); j++ {
			tSl[j][i] = sSl[i][j]
		}
	}

	for i := 0; i < maxLenS; i++ {
		isAsterisk := false
		for j := 0; j < n; j++ {
			if tSl[i][j] == "" {
				if isAsterisk {
					tSl[i][j] = "*"
				}
			} else {
				isAsterisk = true
			}
		}
	}

	for _, t := range tSl {
		fmt.Println(reverseString(strings.Join(t, "")))
	}
}

func inputIntSl() []int {
	//sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	inputs := strings.Split(sc.Text(), " ")
	result := make([]int, len(inputs))
	for i, input := range inputs {
		result[i] = stringToInt(input)
	}
	return result
}

func inputStr() string {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	return sc.Text()
}

func inputIntSlSl(n int) [][]int {
	sc := bufio.NewScanner(os.Stdin)
	results := make([][]int, 0)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}
		result := make([]int, 0)
		for _, input := range strings.Split(sc.Text(), " ") {
			result = append(result, stringToInt(input))
		}
		results = append(results, result)
	}

	return results
}

func inputStrSlSl(n int) [][]string {
	sc := bufio.NewScanner(os.Stdin)
	results := make([][]string, 0)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}

		results = append(results, stringToSlice(sc.Text()))
	}

	return results
}

func inputCharSlSl(n int) [][]string {
	//sc := bufio.NewScanner(os.Stdin)
	results := make([][]string, 0)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}
		results = append(results, strings.Split(sc.Text(), ""))
	}

	return results
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxSl(sl []int) int {
	result := math.MinInt
	for _, x := range sl {
		result = max(result, x)
	}
	return result
}

func minSl(sl []int) int {
	result := math.MaxInt
	for _, x := range sl {
		result = min(result, x)
	}
	return result
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func stringToInt(s string) int {
	x, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return x
}

func stringToSlice(s string) []string {
	sl := make([]string, 0)
	for _, r := range s {
		sl = append(sl, string(r))
	}
	return sl
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func intToString(x int) string {
	return strconv.Itoa(x)
}

func binarySearch(sl []int, v int) int {
	l, r := 0, len(sl)-1

	for l < r {
		m := (l + r) / 2
		if sl[m] == v {
			return m
		} else if sl[m] < v {
			l = m + 1
		} else {
			r = m
		}
	}
	return -1
}
