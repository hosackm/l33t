#include "list.h"
#include <criterion/criterion.h>

TestSuite(LinkedList);
Test(LinkedList, LinkedListInit)
{
  int nums[] = {1, 2, 3, 4};
  l33t_list *ll = l33t_list_init(nums, 4);
  l33t_list *node = ll;
  for (int i = 0; i < 4; i++)
  {
    cr_expect(node->val == (i + 1));
    node = node->next;
  }

  l33t_list_destroy(ll, 4);
}
