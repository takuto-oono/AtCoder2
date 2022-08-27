package main

func createSlMapValue(m map[int]int) []int {
	sl := make([]int, 0)
	for _, v := range m {
		sl = append(sl, v)
	}
	return sl
}
