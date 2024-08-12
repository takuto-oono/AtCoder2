package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	n := inputIntSl()[0]
	scSl := inputStrSlSl(n)

	t := 0
	for _, sc := range scSl {
		c := stringToInt(sc[1])
		t += c
	}

	m := mod(t, n)

	sSl := make([]string, n)
	for i, sc := range scSl {
		sSl[i] = sc[0]
	}

	names := sortStrings(sSl)

	fmt.Println(names[m])
}

func inputIntSl() []int {
	sc.Scan()
	inputs := strings.Split(sc.Text(), " ")
	result := make([]int, len(inputs))
	for i, input := range inputs {
		result[i] = stringToInt(input)
	}
	return result
}

func inputStr() string {
	sc.Scan()
	return sc.Text()
}

func inputIntSlSl(n int) [][]int {
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
	results := make([][]string, 0)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}
		results = append(results, strings.Split(sc.Text(), " "))
	}

	return results
}

func inputCharSlSl(n int) [][]string {
	results := make([][]string, 0)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}
		results = append(results, strings.Split(sc.Text(), ""))
	}

	return results
}

func printIntSlice(sl []int) {
	strSl := make([]string, len(sl))
	for i, num := range sl {
		strSl[i] = strconv.Itoa(num)
	}
	fmt.Println(strings.Join(strSl, " "))
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
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

func intToString(x int) string {
	return strconv.Itoa(x)
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func sortStrings(sl []string) []string {
	sortedSl := make([]string, len(sl))
	copy(sortedSl, sl)
	sort.Strings(sortedSl)
	return sortedSl
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
