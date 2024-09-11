package main

type Answer = [2]int

func TwoSum(nums []int, target int) Answer {
	table := map[int]int{}
	for i, num := range nums {
		compliment := target - num
		if index, exists := table[compliment]; exists {
			return Answer{index, i}
		}
		table[num] = i
	}
	return Answer{0, 0}
}
