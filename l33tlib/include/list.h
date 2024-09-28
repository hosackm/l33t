#pragma once

typedef struct list_node_s lnode;
struct list_node_s
{
  int val;
  lnode *next;
};

lnode *init_list_node(int *nums, int len);
void destroy_list_node(lnode *ll, int len);
