package main

func BinarySearch(nums []int, target int) int {
	// Use the standard library...
	// index, found := slices.BinarySearch(nums, target)
	// if !found { index = -1 }
	// return index

	// Optimize small nums case
	if len(nums) == 0 {
		return -1
	}

	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1
}
