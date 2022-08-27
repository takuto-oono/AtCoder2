package main

func maxSl(sl []int) int {
	if len(sl) == 0 {
		return -1
	}
	ma := sl[0]
	for _, v := range sl {
		if v > ma {
			ma = v
		}
	}
	return ma
}
