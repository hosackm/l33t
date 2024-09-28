#include "list.h"
#include <criterion/criterion.h>

TestSuite(LinkedList);
Test(LinkedList, LinkedListInit)
{
  int nums[] = {1, 2, 3, 4};
  lnode *ll = init_list_node(nums, 4);
  lnode *node = ll;
  for (int i = 0; i < 4; i++)
  {
    cr_expect(node->val == (i + 1));
    node = node->next;
  }

  destroy_list_node(ll, 4);
}
