#include <criterion/criterion.h>

#define MAX(a, b) ((a > b) ? a : b)

typedef struct tree_s tree;
struct tree_s
{
  tree *left;
  tree *right;
  int val;
};

int max_height(tree *node, int level)
{
  if (!node)
  {
    return level;
  }

  return MAX(max_height(node->left, level + 1),
             max_height(node->right, level + 1));
}

int is_balanced(tree *t)
{
  if (!t)
  {
    return 1;
  }

  const int lh = max_height(t->left, 0);
  const int rh = max_height(t->right, 0);
  return (lh - rh) <= 1;
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
  tree *t = init_tree(nodes, sizeof(nodes) / sizeof(int));
  int result = is_balanced(t);
  cr_expect(result == 0);
  free(t);
}

Test(BalancedTree, NullExample) { cr_expect(is_balanced(NULL) == 1); }
