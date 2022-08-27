package main

func minSl(sl []int) int {
	if len(sl) == 0 {
		return -1
	}
	mi := sl[0]
	for _, v := range sl {
		if v < mi {
			mi = v
		}
	}
	return mi
}
