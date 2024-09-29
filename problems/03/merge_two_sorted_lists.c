#include <criterion/criterion.h>
#include <l33t.h>

l33t_list *merge(l33t_list *first, l33t_list *second)
{
  if (!first && !second)
  {
    return NULL;
  }

  l33t_list *result;

  // choose which list to use as head
  if (first && second)
  {
    if (first->val < second->val)
    {
      result = first;
      first = first->next;
    }
    else
    {
      result = second;
      second = second->next;
    }
  }
  else
  {
    if (first)
    {
      result = first;
      first = first->next;
    }
    else
    {
      result = second;
      second = second->next;
    }
  }

  l33t_list *node = result;
  // iterate through lists and set value next
  while (first || second)
  {
    if (!second || first->val < second->val)
    {
      node->next = first;
      first = first->next;
    }
    else if (!first || first->val >= second->val)
    {
      node->next = second;
      second = second->next;
    }
    node = node->next;
  }

  return result;
}

Test(MergeLists, MergeListsTests)
{
  static const int vals[6] = {1, 2, 4, 1, 3, 4};
  l33t_list nodes[6] = {0};

  for (int i = 0; i < 6; i++)
  {
    if (i != 2 && i != 5)
    {
      nodes[i].next = &nodes[i + 1];
    }
    nodes[i].val = vals[i];
  }

  // correctly merge two lists
  l33t_list *merged = merge(&nodes[0], &nodes[3]);

  const int expected[6] = {1, 1, 2, 3, 4, 4};
  for (int i = 0; i < 6; i++)
  {
    cr_expect(merged);
    cr_expect(merged->val == expected[i]);
    merged = merged->next;
  }

  // both empty lists
  l33t_list *null = merge(NULL, NULL);
  cr_expect(!null);

  // one empty list
  l33t_list zero = {.val = 0, .next = NULL};
  l33t_list *zero_n = merge(NULL, &zero);
  cr_expect(&zero == zero_n);
}
