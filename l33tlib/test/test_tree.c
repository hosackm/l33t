#include "tree.h"
#include <criterion/criterion.h>

TestSuite(TreeTests);
Test(TreeTests, InitTreeNode)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  tree *root = init_tree(nodes, sizeof(nodes) / sizeof(int));

  cr_expect(root->val == 6);
  cr_expect(root->left->val == 2);
  cr_expect(root->right->val == 8);
  cr_expect(root->left->left->val == 0);
  cr_expect(root->left->left->left == NULL);

  free(root);
}
