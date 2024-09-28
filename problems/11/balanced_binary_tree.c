#include <criterion/criterion.h>
#include <stdio.h>
#include <string.h>

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
  if (node == NULL)
  {
    return level;
  }

  fprintf(stderr, "max_height lh t:%p %p %d\n", node, node->left, node->val);
  int lh = max_height(node->left, level + 1);
  fprintf(stderr, "max_height rh t: %p %p %d\n", node, node->right, node->val);
  int rh = max_height(node->right, level + 1);
  return MAX(lh, rh);
}

int is_balanced(tree *t)
{
  if (t == NULL || (unsigned long long)t == 0x1e1)
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
    const int left = 2 * i + 1;
    const int right = left + 1;
    if (left < len)
    {
      t[i].left = (nums[left] == -1) ? NULL : &t[2 * i + 1];
    }
    if (right < len)
    {
      t[i].right = (nums[right] == -1) ? NULL : &t[2 * i + 2];
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
  tree *t = init_tree(nodes, 9);
  const int result = is_balanced(t);
  cr_expect(result == 0);
  free(t);
}

Test(BalancedTree, NullExample) { cr_expect(is_balanced(NULL) == 1); }
