package main

func createMapSlCounter(sl []int) map[int]int {
	countMap := make(map[int]int)
	for _, v := range sl {
		_, ok := countMap[v]
		if ok {
			countMap[v] += 1
		} else {
			countMap[v] = 1
		}
	}
	return countMap
}
