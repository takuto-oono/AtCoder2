package main

import "fmt"

func insertIntSlice(sl []int, x, index int) []int {
	l := len(sl)
	if index == l-1 {
		sl = append(sl, x)
	} else if index == 0 {
		sl = append(sl, sl[l-1])
		tmp := x
		for i := 0; i < l; i++ {
			sl[i], tmp = tmp, sl[i]
		}
	} else {
		sl = append(sl, sl[l-1])
		tmp := x
		for i := 0; i < l; i++ {
			if i < index {
				continue
			}
			sl[i], tmp = tmp, sl[i]
		}
	}
	return sl
}

func main() {
	slice := []int{}
	for i := 0; i < 10; i++ {
		slice = append(slice, i)
	}
	fmt.Println(slice)
	slice = insertIntSlice(slice, 11, 0)
	fmt.Println(slice)
	slice = insertIntSlice(slice, 4, 2)
	fmt.Println(slice)
	slice = insertIntSlice(slice, 60, 5)
	fmt.Println(slice)

}
