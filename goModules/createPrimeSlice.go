package main

func createPrimeSlice(n int) []bool {
	isPrimeSlice := make([]bool, n+1)
	for i := 0; i < n+1; i++ {
		isPrimeSlice[i] = true
	}
	isPrimeSlice[0], isPrimeSlice[1] = false, false
	for i := 2; i < n+1; i++ {
		if i*i > n {
			break
		}
		if isPrimeSlice[i] {
			for j := 2 * i; j < n+1; j += i {
				isPrimeSlice[j] = false
			}
		}
	}
	return isPrimeSlice
}
