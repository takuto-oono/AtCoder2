package main

func gcd(x, y int) int {
	if x > y {
		x, y = y, x
	}

	for x != 0 {
		x, y = y%x, x
	}
	return y
}

func gcdSl(sl []int) int {
	if len(sl) == 0 {
		return 0
	}
	g := sl[0]
	for _, v := range sl {
		g = gcd(g, v)
	}
	return g
}
