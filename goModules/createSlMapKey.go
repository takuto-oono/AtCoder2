package main

func createSlMapKey(m map[int]int) []int {
	sl := make([]int, 0)
	for k, _ := range m {
		sl = append(sl, k)
	}
	return sl
}
