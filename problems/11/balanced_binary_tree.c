#include "tree.h"
#include <criterion/criterion.h>
#include <stdio.h>

TestSuite(BalancedTree);
Test(BalancedTree, FirstExample)
{
  int nodes[] = {3, 9, 20, -1, -1, 15, 7};
  tree *t = init_tree(nodes, sizeof(nodes) / sizeof(int));
  int result = is_balanced(t);
  cr_expect(result == 1);
  free(t);
}

Test(BalancedTree, SecondExample)
{
  int nodes[] = {1, 2, 2, 3, 3, -1, -1, 4, 4};
  tree *t = init_tree(nodes, 9);
  const int result = is_balanced(t);
  cr_expect(result == 0);
  free(t);
}

Test(BalancedTree, NullExample) { cr_expect(is_balanced(NULL) == 1); }
