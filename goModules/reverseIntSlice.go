package main

func reverseIntSlice(sl []int) []int {
	l := len(sl)
	revSl := make([]int, l)
	for i, v := range sl {
		revSl[l-i-1] = v
	}
	return revSl
}
