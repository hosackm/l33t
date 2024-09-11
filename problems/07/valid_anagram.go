package main

type Counter map[rune]int

func countChars(s string) Counter {
	table := make(Counter)
	for _, ch := range s {
		num, exists := table[ch]
		if exists {
			table[ch] = num + 1
		} else {
			table[ch] = 1
		}
	}
	return table
}

func countsEqual(first Counter, second Counter) bool {
	if len(first) != len(second) {
		return false
	}

	for ch := range first {
		num, exists := second[ch]
		if !exists || num != first[ch] {
			return false
		}
	}

	return true
}

// IsAnagram returns true if the first string is an anagram of the second
// and vice versa.
func IsAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sCount := countChars(s)
	tCount := countChars(t)

	return countsEqual(sCount, tCount)
}
