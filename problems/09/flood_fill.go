package main

type point [2]int
type cache map[point]bool

func FloodFill(img [][]int, row int, col int, color int) [][]int {
	if row < 0 || row >= len(img) || col < 0 || col >= len(img[0]) {
		return nil
	}

	recurse(img, row, col, img[row][col], color, make(cache))
	return img
}

func recurse(img [][]int, row int, col int, initial int, target int, c cache) {
	current := point{row, col}
	if _, found := c[current]; found {
		return
	}
	if row < 0 || row >= len(img) || col < 0 || col >= len(img[0]) {
		return
	}

	c[current] = true
	if img[row][col] != initial {
		return
	}

	img[row][col] = target
	for _, pt := range neighbors(row, col) {
		recurse(img, pt[0], pt[1], initial, target, c)
	}
}

func neighbors(row int, col int) []point {
	return []point{
		{row, col - 1},
		{row, col + 1},
		{row - 1, col},
		{row + 1, col},
	}
}
