#include <criterion/criterion.h>
#include <sys/resource.h>

#define SZ(arr, x) (sizeof(arr) / sizeof(x))

typedef struct tree_node_s node;
struct tree_node_s
{
  int val;
  node *left;
  node *right;
};

int lca(node *root, node *first, node *second)
{
  if (!root)
  {
    return -1;
  }

  // 3 posibilites
  // 1. both nodes are larger than the current node. Go right.
  // 2. both nodes are smaller than current node. Go left.
  // 3. one is equal OR one is larger / one smaller. Found ancestor.
  if (first->val > root->val && second->val > root->val)
  {
    return lca(root->right, first, second);
  }
  else if (first->val < root->val && second->val < root->val)
  {
    return lca(root->left, first, second);
  }
  else
  {
    return root->val;
  }
}

node *init_tree(int *nums, int len)
{
  node *tree = malloc(sizeof(node) * len);
  for (int i = 0; i < len; i++)
  {
    if ((2 * i + 1) < 11)
    {
      tree[i].left = (nums[2 * i + 1] == -1) ? NULL : &tree[2 * i + 1];
    }
    if ((2 * i + 2) < 11)
    {
      tree[i].right = (nums[2 * i + 2] == -1) ? NULL : &tree[2 * i + 2];
    }
    tree[i].val = nums[i];
  }
  return tree;
}

TestSuite(TestLCA);

Test(TestLCA, InitTreeNode)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  node *root = init_tree(nodes, SZ(nodes, int));

  cr_expect(root->val == 6);
  cr_expect(root->left->val == 2);
  cr_expect(root->right->val == 8);
  cr_expect(root->left->left->val == 0);
  cr_expect(root->left->left->left == NULL);

  free(root);
}

Test(TestLCA, FirstExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  node *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root->left, root->right);
  cr_expect(anc == 6);
  free(root);
}

Test(TestLCA, SecondExample)
{
  int nodes[] = {6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5};
  node *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root->left, root->left->right);
  cr_expect(anc == 2);
  free(root);
}

Test(TestLCA, ThirdExample)
{
  int nodes[] = {2, 1};
  node *root = init_tree(nodes, SZ(nodes, int));

  int anc = lca(root, root, root->left);
  cr_expect(anc == 2);
  free(root);
}
