package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	sl := inputIntSl()
	n, t, a := sl[0], sl[1], sl[2]
	r := n - t - a

	if min(t, a)+r < max(t, a) {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}

func inputIntSl() []int {
	sc := bufio.NewScanner(os.Stdin)
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

func inputIntSlSl() [][]int {
	sc := bufio.NewScanner(os.Stdin)
	results := make([][]int, 0)

	for sc.Scan() {
		result := make([]int, 0)
		for _, input := range strings.Split(sc.Text(), " ") {
			result = append(result, stringToInt(input))
		}
		results = append(results, result)
	}

	return results
}

func inputStrSlSl() [][]string {
	sc := bufio.NewScanner(os.Stdin)
	results := make([][]string, 0)

	for sc.Scan() {
		results = append(results, strings.Split(sc.Text(), " "))
	}

	return results
}

func inputCharSlSl() [][]string {
	sc := bufio.NewScanner(os.Stdin)
	results := make([][]string, 0)

	for sc.Scan() {
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
