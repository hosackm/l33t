package main

func FindBad(latest int, isBad func(int) bool) int {
	left := 1
	right := latest
	bad := latest
	for left <= right {
		var mid int = (left + right) / 2
		if isBad(mid) {
			bad = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return bad
}
