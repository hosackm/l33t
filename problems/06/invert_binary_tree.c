#include <criterion/criterion.h>

typedef struct tree_node_t treenode;
struct tree_node_t
{
  int val;
  treenode *left;
  treenode *right;
};

void invert(treenode *root)
{
  if (root)
  {
    treenode *tmp = root->left;
    root->left = root->right;
    root->right = tmp;

    invert(root->left);
    invert(root->right);
  }
}

Test(InvertBtree, InvertBtreeTests)
{
  struct tree_node_t node7 = {9, NULL, NULL};
  struct tree_node_t node6 = {6, NULL, NULL};
  struct tree_node_t node5 = {3, NULL, NULL};
  struct tree_node_t node4 = {1, NULL, NULL};
  struct tree_node_t node3 = {7, &node6, &node7};
  struct tree_node_t node2 = {2, &node4, &node5};
  struct tree_node_t node1 = {4, &node2, &node3};

  invert(&node1);

  cr_expect(node1.val == 4);
  cr_expect(node1.left->val == 7);
  cr_expect(node1.right->val == 2);
  cr_expect(node1.left->left->val == 9);
  cr_expect(node1.left->right->val == 6);
  cr_expect(node1.right->val == 2);
  cr_expect(node1.right->left->val == 3);
  cr_expect(node1.right->right->val == 1);
}
