#pragma once

typedef struct tree_s tree;
struct tree_s
{
  tree *left;
  tree *right;
  int val;
};

int max_height(tree *node, int level);

int is_balanced(tree *t);

tree *init_tree(int *nums, int len);
