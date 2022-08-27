package main

import (
	"sort"
)

func sortStringSlice(sl *[]string, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.StringSlice(*sl)))
	} else {
		sort.Strings(*sl)
	}
}