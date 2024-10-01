#include <l33t.h>
#include <stdlib.h> // malloc, ree
#include <string.h> // memset

l33t_tree *l33t_tree_init(int *nums, int len)
{
  l33t_tree *t = malloc(sizeof(l33t_tree) * len);
  memset(t, 0, sizeof(l33t_tree));

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

void l33t_tree_destroy(l33t_tree *tree)
{
  free(tree);
}
