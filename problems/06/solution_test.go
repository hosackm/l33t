package main

import (
	"testing"
)

func TestInvertTree(t *testing.T) {
	root := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val:   2,
			Left:  &TreeNode{Val: 1},
			Right: &TreeNode{Val: 3},
		},
		Right: &TreeNode{
			Val:   7,
			Left:  &TreeNode{Val: 6},
			Right: &TreeNode{Val: 9},
		},
	}
	InvertTree(root)
	if root.Val != 4 {
		t.Fail()
	}
	if root.Left.Val != 7 || root.Right.Val != 2 {
		t.Fail()
	}
	if root.Left.Left.Val != 9 || root.Left.Right.Val != 6 {
		t.Fail()
	}
	if root.Right.Left.Val != 3 || root.Right.Right.Val != 1 {
		t.Fail()
	}

	if InvertTree(nil) != nil {
		t.Fail()
	}
}
