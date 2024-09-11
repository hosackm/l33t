package main

import (
	"testing"
)

func TestIsBalanced(t *testing.T) {
	type Input struct {
		tree     *TreeNode
		balanced bool
		height   int
	}

	trees := []Input{
		{&TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 9,
			},
			Right: &TreeNode{
				Val: 20,
				Left: &TreeNode{
					Val: 15,
				},
				Right: &TreeNode{
					Val: 7,
				},
			},
		}, true, 3},
		{&TreeNode{
			Val: 1,
			Left: &TreeNode{
				Val: 2,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			Right: &TreeNode{
				Val: 2,
			},
		}, false, 4},
		{tree: nil, balanced: true, height: 0},
	}

	for _, input := range trees {
		balanced, height := IsBalanced(input.tree)
		if balanced != input.balanced || input.height != height {
			t.Fail()
		}
	}
}
