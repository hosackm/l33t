#pragma once

/**
 * @brief A structure to represent a linked list.
 */
typedef struct list_node_s l33t_list;

struct list_node_s
{
  int val;         /**< The value stored within this node. */
  l33t_list *next; /**< The next node in the list. */
};

/**
 * @brief Initialize a linked list.
 *
 * Allocates memory and assigns nodes according to values in nums.
 *
 * @param[in] nums An arrray of integers to be inserted as nodes.
 * @param[in] len The length of nums.
 * @return The linked list.
 */
l33t_list *l33t_list_init(int *nums, int len);

/*
 * Deallocate all memory used by the list.
 * Must provide len to avoid following cycles
 * and freeing already freed nodes.
 */
/**
 * @brief Deallocate a list.
 *
 * Deallocate (up to len nodes) nodes within a list.
 *
 * @param[in] ll The linked list.
 * @param[in] len The number of nodes to deallocate.
 */
void l33t_list_destroy(l33t_list *ll, int len);
