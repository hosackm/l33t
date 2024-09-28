#include "list.h"
#include <stdlib.h>

lnode *init_list_node(int *nums, int len)
{
  lnode *head = NULL;
  lnode *prev = NULL;
  for (int i = 0; i < len; i++)
  {
    lnode *node = malloc(sizeof(lnode));
    node->next = NULL;
    node->val = nums[i];

    if (!head)
    {
      head = node;
    }

    if (prev)
    {
      prev->next = node;
    }
    prev = node;
  }

  return head;
}

void destroy_list_node(lnode *ll, int len)
{
  for (int i = 0; i < len; i++)
  {
    lnode *next = ll->next;
    free(ll);
    ll = next;
  }
}
