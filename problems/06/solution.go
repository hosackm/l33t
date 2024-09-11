package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func InvertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	InvertTree(root.Left)
	InvertTree(root.Right)
	root.Left, root.Right = root.Right, root.Left

	return root
}
