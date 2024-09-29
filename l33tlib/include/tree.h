#pragma once

typedef struct tree_s l33t_tree;
struct tree_s
{
  l33t_tree *left;
  l33t_tree *right;
  int val;
};

/*
 * Initialize a tree containing nodes that
 * have values corresponding to nums. -1 is
 * used to represent NULL tree nodes.
 */
l33t_tree *l33t_tree_init(int *nums, int len);

/*
 * Deallocate all memory used by the list.
 * Must provide len to avoid following cycles
 * and freeing already freed nodes.
 */
void l33t_tree_destroy(l33t_tree *ll);
