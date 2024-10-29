package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func area(h []int, l int, r int) int {
	return min(h[l], h[r]) * (r - l)
}

func MaxArea(height []int) int {
	left := 0
	right := len(height) - 1
	max := 0
	for left < right {
		a := area(height, left, right)
		if a > max {
			max = a
		}

		if height[left] < height[right] {
			left += 1
		} else {
			right -= 1
		}
	}

	return max
}
