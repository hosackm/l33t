package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func IsBalanced(t *TreeNode) (bool, int) {
	if t == nil {
		return true, 0
	}

	lbal, lheight := IsBalanced(t.Left)
	rbal, rheight := IsBalanced(t.Right)
	height := max(lheight, rheight) + 1
	balanced := lbal && rbal && abs(lheight-rheight) <= 1
	return balanced, height
}
