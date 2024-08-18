package main

import (
	"bufio"
	"container/list"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

var (
	sc           = bufio.NewScanner(os.Stdin)
	bufferSize   = 2 * pow(10, 9)
	maxTokenSize = 2 * pow(10, 9)
)

func init() {
	sc.Buffer(make([]byte, bufferSize), maxTokenSize)
}

func main() {
	li := inputIntSl()
	n, k := li[0], li[1]
	pSl := inputIntSl()

	pMap := make(map[int]int, n)
	for i, p := range pSl {
		pMap[p] = i
	}

	sort.Ints(pSl)

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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
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

func equalIntSl(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i, x := range a {
		if x != b[i] {
			return false
		}
	}
	return true
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

type Deque struct {
	data *list.List
}

func NewDeque() *Deque {
	return &Deque{data: list.New()}
}

func (d *Deque) PushFront(value interface{}) {
	d.data.PushFront(value)
}

func (d *Deque) PushBack(value interface{}) {
	d.data.PushBack(value)
}

func (d *Deque) PopFront() interface{} {
	if d.data.Len() == 0 {
		return nil
	}
	front := d.data.Front()
	return d.data.Remove(front)
}

func (d *Deque) PopBack() interface{} {
	if d.data.Len() == 0 {
		return nil
	}
	back := d.data.Back()
	return d.data.Remove(back)
}

func (d *Deque) Len() int {
	return d.data.Len()
}
