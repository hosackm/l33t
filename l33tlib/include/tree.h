#pragma once

typedef struct tree_s l33t_tree;
struct tree_s
{
  l33t_tree *left;
  l33t_tree *right;
  int val;
};

/**
 * @brief Initialize a tree.
 *
 * Allocates memory and assigns nodes according to values in nums.
 * Use -1 to create a NULL node.
 *
 * @param[in] nums An arrray of integers to be inserted as nodes.
 * @param[in] len The length of nums.
 * @return The tree.
 */
l33t_tree *l33t_tree_init(int *nums, int len);

/**
 * @brief Deallocate the memory used by a tree.
 *
 * @param[in] tree The tree.
 */
void l33t_tree_destroy(l33t_tree *tree);
