package main

func LongestPalindrome(s string) int {
	counts := make(map[rune]int)
	for _, ch := range s {
		counts[ch]++
	}

	total := 0
	middle := 0
	for _, count := range counts {
		total += (count / 2) * 2
		if count%2 == 1 {
			middle = 1
		}
	}

	return total + middle
}
