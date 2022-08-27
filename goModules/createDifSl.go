package main

func createDifSl(sl []int) []int {
	if len(sl) <= 1 {
		return []int{-1}
	}
	difSl := make([]int, len(sl)-1)
	for i := 0; i < len(sl)-1; i++ {
		difSl[i] = sl[i+1] - sl[i]
	}
	return difSl
}
