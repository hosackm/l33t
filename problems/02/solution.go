package main

// map of closing rune to its matching opening rune
var table map[rune]rune

func init() {
	table = map[rune]rune{
		'}': '{',
		')': '(',
		']': '[',
	}
}

func LongEnough(stackSize int, charsLeft int) bool {
	return stackSize <= charsLeft
}

func ValidParentheses(s string) bool {
	// if it's not an even number of parentheses then
	// they can't be matched evenly.
	numChars := len(s)
	if numChars%2 != 0 {
		return false
	}

	pos := -1
	stack := make([]rune, numChars)
	for i, ch := range s {
		// If the number of chars left is ever shorter than
		// the stack, then we know we have an invalid string
		// there aren't enough character to match with their
		// open parenthesis
		if !LongEnough(pos+1, numChars-i) {
			return false
		}

		switch ch {
		case '{', '(', '[':
			pos++
			stack[pos] = ch
		case '}', ')', ']':
			match, ok := table[ch]
			if !ok || pos < 0 || stack[pos] != match {
				return false
			}
			pos--
		default:
			// invalid character
			return false
		}
	}

	return true
}
