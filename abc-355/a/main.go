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

var (
	sc           = bufio.NewScanner(os.Stdin)
	bufferSize   = 1000000000
	maxTokenSize = 1000000000
)

func init() {
	sc.Buffer(make([]byte, bufferSize), maxTokenSize)
	sc.Split(bufio.ScanWords)
}

func main() {
	a, b := inputInt(), inputInt()
	if a == b {
		fmt.Println(-1)
		os.Exit(0)
	}
	candidates := []int{1, 2, 3}
	for _, c := range candidates {
		if a == c || b == c {
			continue
		}
		fmt.Println(c)
	}
}

func inputIntSl(l int) []int {
	result := make([]int, l)
	for i := 0; i < l; i++ {
		sc.Scan()
		result[i] = stringToInt(sc.Text())
	}
	return result
}

func inputStr() string {
	sc.Scan()
	return sc.Text()
}

func inputInt() int {
	sc.Scan()
	return stringToInt(sc.Text())
}

func inputIntSlSl(y, x int) [][]int {
	results := make([][]int, y)

	for i := 0; i < y; i++ {
		results[i] = make([]int, x)
		for j := 0; j < x; j++ {
			if !sc.Scan() {
				break
			}
			results[i][j] = stringToInt(sc.Text())
		}
	}

	return results
}

func inputStrSl(n int) []string {
	results := make([]string, n)

	for i := 0; i < n; i++ {
		if !sc.Scan() {
			break
		}
		results[i] = sc.Text()
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
