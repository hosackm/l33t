package main

// MaxProfit returns the maximum profit attainable from
// a list of prices provided as an int slice.
// If no profit can be obtained then 0 is returned.
func MaxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}

	max := 0
	for left, right := 0, 1; right < len(prices); right++ {
		profit := prices[right] - prices[left]
		if profit > max {
			max = profit
		}

		if prices[right] < prices[left] {
			left = right
		}
	}

	return max
}
