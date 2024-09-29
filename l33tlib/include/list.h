#pragma once

typedef struct list_node_s l33t_list;
struct list_node_s
{
  int val;
  l33t_list *next;
};

/*
 * Initialize a linked list containing nodes that
 * have values corresponding to nums.
 */
l33t_list *l33t_list_init(int *nums, int len);

/*
 * Deallocate all memory used by the list.
 * Must provide len to avoid following cycles
 * and freeing already freed nodes.
 */
void l33t_list_destroy(l33t_list *ll, int len);
