#include "tree.h"
#include <criterion/criterion.h>
#include <l33t.h>

int lca(l33t_tree *root, l33t_tree *first, l33t_tree *second)
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

TestSuite(TestLCA);

Test(TestLCA, FirstExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  l33t_tree *root = l33t_tree_init(nodes, ARRAY_SIZE(nodes, int));

  int anc = lca(root, root->left, root->right);
  cr_expect(anc == 6);
  l33t_tree_destroy(root);
}

Test(TestLCA, SecondExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  l33t_tree *root = l33t_tree_init(nodes, ARRAY_SIZE(nodes, int));

  int anc = lca(root, root->left, root->left->right);
  cr_expect(anc == 2);
  l33t_tree_destroy(root);
}

Test(TestLCA, ThirdExample)
{
  int nodes[] = {2, 1};
  l33t_tree *root = l33t_tree_init(nodes, ARRAY_SIZE(nodes, int));

  int anc = lca(root, root, root->left);
  cr_expect(anc == 2);
  l33t_tree_destroy(root);
}
