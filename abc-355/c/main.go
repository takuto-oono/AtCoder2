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
	n, t := inputInt(), inputInt()
	aSl := inputIntSl(t)

	var aMap map[int]int
	for i, a := range aSl {
		aMap[a] = i + 1
	}

	ans := math.MaxInt
	var patterns [][]int

	for i := 1; i < n*n+1; i += n {
		var nums []int
		for j := i; j < n+n+1; j++ {
			nums = append(nums, aMap[j])
		}

		patterns = append(patterns, nums)
	}

	for i := 1; i < n+1; i++ {
		var nums []int
		for j := 0; j < n; j++ {
			nums = append(nums, aMap[i+j*n])
		}

		patterns = append(patterns, nums)
	}

	var nums1 []int
	var nums2 []int
	var nums3 []int
	var nums4 []int

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i == j {
				nums1 = append(nums1, aMap[i*j+1])
			}
			if i == n-j-1 {
				nums2 = append(nums2, aMap[i*j+1])
			}
		}
	}

	if ans == math.MinInt {
		fmt.Println(-1)
	} else {
		fmt.Println(ans)
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
