#include <glib.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode
{
  int val;
  struct ListNode *next;
} list_node_s;
typedef list_node_s *list_node;
typedef list_node ln;

ln merge(ln first, ln second)
{
  if (!first && !second)
  {
    return NULL;
  }

  ln result;

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

  ln node = result;
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

void test_merge()
{
  static const int vals[6] = {1, 2, 4, 1, 3, 4};
  list_node_s nodes[6] = {0};

  for (int i = 0; i < 6; i++)
  {
    if (i != 2 && i != 5)
    {
      nodes[i].next = &nodes[i + 1];
    }
    nodes[i].val = vals[i];
  }

  // correctly merge two lists
  list_node merged = merge(&nodes[0], &nodes[3]);

  const int expected[6] = {1, 1, 2, 3, 4, 4};
  for (int i = 0; i < 6; i++)
  {
    g_assert(merged);
    g_assert_cmpint(merged->val, ==, expected[i]);
    merged = merged->next;
  }

  // both empty lists
  ln null = merge(NULL, NULL);
  g_assert(!null);

  // one empty list
  list_node_s zero = {.val = 0, .next = NULL};
  ln zero_n = merge(NULL, &zero);
  g_assert(&zero == zero_n);
}

int main(int argc, char **argv)
{
  g_test_init(&argc, &argv, NULL);
  g_test_add_func("/merge_two_sorted_lists", test_merge);
  g_test_run();
}
