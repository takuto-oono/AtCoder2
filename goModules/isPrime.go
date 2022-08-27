package main

func isPrime(n int) bool {
	for i := 2; i < n+1; i++ {
		if i*i > n {
			break
		}
		if n%i == 0 {
			return false
		}
	}
	return true
}
