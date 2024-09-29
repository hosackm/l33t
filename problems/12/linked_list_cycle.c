#include <criterion/criterion.h>
#include <l33t.h>

int has_cycle(l33t_list *list)
{
  if (!list)
  {
    return 0;
  }

  l33t_list *slow = list;
  l33t_list *fast = list->next;
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
  l33t_list *ll = l33t_list_init(nums, 4);

  l33t_list *second = ll->next;
  l33t_list *fourth = ll->next->next->next;
  fourth->next = second;

  cr_expect(has_cycle(ll) == 1);

  l33t_list_destroy(ll, 4);
}

Test(LinkedListCycle, LinkedListCycleSecond)
{
  int nums[] = {1, 2};
  l33t_list *ll = l33t_list_init(nums, 2);
  cr_expect(has_cycle(ll) == 0);
  l33t_list_destroy(ll, 2);
}

Test(LinkedListCycle, LinkedListCycleThird)
{
  int nums[] = {1};
  l33t_list *ll = l33t_list_init(nums, 1);
  cr_expect(has_cycle(ll) == 0);
  l33t_list_destroy(ll, 1);
}
