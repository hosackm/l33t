#include <criterion/criterion.h>
#include <l33t.h>
#include <stdio.h>

int max_height(l33t_tree *node, int level)
{
  if (node == NULL)
  {
    return level;
  }

  int lh = max_height(node->left, level + 1);
  int rh = max_height(node->right, level + 1);
  return MAX(lh, rh);
}

int is_balanced(l33t_tree *t)
{
  if (t == NULL || (unsigned long long)t == 0x1e1)
  {
    return 1;
  }

  const int lh = max_height(t->left, 0);
  const int rh = max_height(t->right, 0);
  return (lh - rh) <= 1;
}

TestSuite(BalancedTree);
Test(BalancedTree, FirstExample)
{
  int nodes[] = {3, 9, 20, -1, -1, 15, 7};
  l33t_tree *t = l33t_tree_init(nodes, sizeof(nodes) / sizeof(int));
  int result = is_balanced(t);
  cr_expect(result == 1);
  l33t_tree_destroy(t);
}

Test(BalancedTree, SecondExample)
{
  int nodes[] = {1, 2, 2, 3, 3, -1, -1, 4, 4};
  l33t_tree *t = l33t_tree_init(nodes, 9);
  const int result = is_balanced(t);
  cr_expect(result == 0);
  l33t_tree_destroy(t);
}

Test(BalancedTree, NullExample) { cr_expect(is_balanced(NULL) == 1); }
