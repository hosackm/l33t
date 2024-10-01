#include <l33t.h>
#include <stdlib.h> // calloc, free

l33t_list *l33t_list_init(int *nums, int len)
{
  l33t_list *head = NULL;
  l33t_list *prev = NULL;
  for (int i = 0; i < len; i++)
  {
    l33t_list *node = calloc(1, sizeof(l33t_list));
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

void l33t_list_destroy(l33t_list *ll, int len)
{
  for (int i = 0; i < len; i++)
  {
    l33t_list *next = ll->next;
    free(ll);
    ll = next;
  }
}
