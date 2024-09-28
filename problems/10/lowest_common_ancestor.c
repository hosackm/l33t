#include "tree.h"
#include <criterion/criterion.h>

#define SZ(arr, x) (sizeof(arr) / sizeof(x))

int lca(tree *root, tree *first, tree *second)
{
  if (!root)
  {
    return -1;
  }

  // 3 posibilites
  // 1. both nodes are larger than the current node. Go right.
  // 2. both nodes are smaller than current node. Go left.
  // 3. one is equal OR one is larger / one smaller. Found ancestor.
  if (first->val > root->val && second->val > root->val)
  {
    return lca(root->right, first, second);
  }
  else if (first->val < root->val && second->val < root->val)
  {
    return lca(root->left, first, second);
  }
  else
  {
    return root->val;
  }
}

tree *init_tree(int *nums, int len)
{
  tree *t = malloc(sizeof(tree) * len);
  for (int i = 0; i < len; i++)
  {
    if ((2 * i + 1) < 11)
    {
      t[i].left = (nums[2 * i + 1] == -1) ? NULL : &t[2 * i + 1];
    }
    if ((2 * i + 2) < 11)
    {
      t[i].right = (nums[2 * i + 2] == -1) ? NULL : &t[2 * i + 2];
    }
    t[i].val = nums[i];
  }
  return t;
}

TestSuite(TestLCA);

Test(TestLCA, FirstExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  tree *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root->left, root->right);
  cr_expect(anc == 6);
  free(root);
}

Test(TestLCA, SecondExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  tree *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root->left, root->left->right);
  cr_expect(anc == 2);
  free(root);
}

Test(TestLCA, ThirdExample)
{
  int nodes[] = {2, 1};
  tree *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root, root->left);
  cr_expect(anc == 2);
  free(root);
}
