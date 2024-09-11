package main

// The difference between uppercase and lowercase ascii characters
var Difference = byte('a') - byte('A')

// IsAlnum returns true if the input byte is alphanumeric
// when converted to an ascii character.
func IsAlpha(ch byte) bool {
	return ch >= byte('A') && ch <= byte('z')
}

func IsNum(ch byte) bool {
	return ch >= byte('0') && ch <= byte('9')
}

// IsAlnum returns true if the input byte is alphanumeric
// when converted to an ascii character.
func IsAlnum(ch byte) bool {
	return IsAlpha(ch) || IsNum(ch)
}

// Returns true if the input bytes represent the same
// character (case insensitive).
func BytesEqual(one byte, other byte) bool {
	if IsNum(one) || IsNum(other) {
		return one == other
	}

	switch one - other {
	case 0, Difference, -Difference:
		// check if they're both alphabetical
		return true
	default:
		return false
	}
}

// ValidPalindrome returns true if the input string
// is a palindrome. Ignores all non-alphanumeric characters
// in the string.  An empty string is considered a palindrome.
func ValidPalindrome(s string) bool {
	if len(s) < 2 {
		return true
	}

	left := 0
	right := len(s) - 1
	for left < right {
		for left < len(s) && !IsAlnum(s[left]) {
			left++
		}
		for right > 0 && !IsAlnum(s[right]) {
			right--
		}

		if left > right {
			return true
		}

		if !BytesEqual(s[left], s[right]) {
			return false
		}

		left++
		right--
	}

	return true
}
