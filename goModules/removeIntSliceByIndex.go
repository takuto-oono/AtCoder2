package main


func removeSliceByIndex(sl []int, index int) []int {
	return sl[:index+copy(sl[index:], sl[index+1:])]
}