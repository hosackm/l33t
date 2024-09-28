#include "list.h"
#include <criterion/criterion.h>

int has_cycle(lnode *list)
{
  if (!list)
  {
    return 0;
  }

  lnode *slow = list;
  lnode *fast = list->next;
  while (1)
  {
    if (!slow || !fast)
    {
      return 0;
    }
    if (slow == fast)
    {
      return 1;
    }

    if (!fast->next || !fast->next->next)
    {
      return 0;
    }

    slow = slow->next;
    fast = fast->next->next;
  }
}

TestSuite(LinkedListCycle);

Test(LinkedListCycle, LinkedListCycleFirst)
{
  int nums[] = {3, 2, 0, -4};
  lnode *ll = init_list_node(nums, 4);

  lnode *second = ll->next;
  lnode *fourth = ll->next->next->next;
  fourth->next = second;

  cr_expect(has_cycle(ll) == 1);

  destroy_list_node(ll, 4);
}

Test(LinkedListCycle, LinkedListCycleSecond)
{
  int nums[] = {1, 2};
  lnode *ll = init_list_node(nums, 2);
  cr_expect(has_cycle(ll) == 0);
  destroy_list_node(ll, 2);
}

Test(LinkedListCycle, LinkedListCycleThird)
{
  int nums[] = {1};
  lnode *ll = init_list_node(nums, 1);
  cr_expect(has_cycle(ll) == 0);
  destroy_list_node(ll, 1);
}
