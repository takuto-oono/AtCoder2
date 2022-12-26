package main

import (
	"fmt"
)

func main() {
	s := "abc"
	for _, c := range s {
		if c == 'a' {
			fmt.Println("this is a", c)
		} else {
			fmt.Println("this is not a", c)
		}
	}
}