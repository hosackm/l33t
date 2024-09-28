#include "tree.h"
#include <stdio.h>
#include <stdlib.h>

#define MAX(a, b) ((a > b) ? a : b)

int max_height(tree *node, int level)
{
  if (node == NULL)
  {
    return level;
  }

  int lh = max_height(node->left, level + 1);
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
