#include "error.h"
#include "list.h"
#include <criterion/criterion.h>
#include <l33t.h>

l33t_list *reverse(l33t_list *list)
{
  l33t_list *node = list;
  l33t_list *prev = NULL;

  while (node)
  {
    l33t_list *tmp = node->next;
    node->next = prev ? prev : NULL;
    prev = node;
    node = tmp;
  }

  return prev;
}

Test(ReverseListTests, LeetcodeExamples)
{
  int nums[5] = {1, 2, 3, 4, 5};
  l33t_list *list = l33t_list_init(nums, 5);
  list = reverse(list);

  cr_expect(list->val == 5);
  cr_expect(list->next->val == 4);
  cr_expect(list->next->next->val == 3);
  cr_expect(list->next->next->next->val == 2);
  cr_expect(list->next->next->next->next->val == 1);

  l33t_list_destroy(list, 5);
}
