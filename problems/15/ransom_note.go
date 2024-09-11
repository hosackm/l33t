package main

type LetterCount [26]int

func CanConstruct(letter string, magazine string) bool {
	var letterCount LetterCount
	var magazineCount LetterCount

	for _, ch := range letter {
		index := int(byte(ch) - 'a')
		letterCount[index]++
	}

	for _, ch := range magazine {
		index := int(byte(ch) - 'a')
		magazineCount[index]++
	}

	for ch, cnt := range letterCount {
		if cnt > magazineCount[ch] {
			return false
		}
	}

	return true
}
