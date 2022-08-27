package main

func lowerBound(sl []int, v int) int {
	l, r := 0, len(sl)-1
	for l <= r {
		m := l + (r-l)/2
		if sl[m] < v {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func upperBound(sl []int, v int) int {
	l, r := 0, len(sl)-1
	for l <= r {
		mid := l + (r-l)/2
		if sl[mid] <= v {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l
}
