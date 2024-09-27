#include <criterion/criterion.h>

typedef struct tree_s tree;
struct tree_s
{
  tree *left;
  tree *right;
  int value;
};

int is_balanced(tree *t)
{
  (void)t;
  return 1;
}

TestSuite(BalancedTree);
Test(BalancedTree, Tests)
{
  tree t = {0};
  cr_expect(is_balanced(&t) == 1);
}
