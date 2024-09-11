package main

type Pair [2]int

const LAND byte = '1'
const WATER byte = '0'

func NumIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}

	numRows := len(grid)
	numCols := len(grid[0])
	visited := map[Pair]bool{}
	islands := 0

	for r := 0; r < numRows; r++ {
		for c := 0; c < numCols; c++ {
			p := Pair{r, c}
			if _, exists := visited[p]; exists || grid[r][c] == WATER {
				continue
			}
			islands++
			bfs(grid, r, c, &visited)
		}
	}
	return islands
}

func bfs(grid [][]byte, r int, c int, visited *map[Pair]bool) {
	queue := []Pair{{r, c}}
	for len(queue) > 0 {
		p := queue[0]
		queue = queue[1:]
		if _, exists := (*visited)[p]; exists {
			continue
		}

		row, col := p[0], p[1]
		if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[0]) {
			continue
		}

		(*visited)[p] = true
		if grid[row][col] == WATER {
			continue
		}

		queue = append(
			queue,
			Pair{row - 1, col},
			Pair{row + 1, col},
			Pair{row, col - 1},
			Pair{row, col + 1},
		)
	}
}
