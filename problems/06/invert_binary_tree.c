#include <criterion/criterion.h>
#include <l33t.h>

void invert(l33t_tree *root)
{
  if (root)
  {
    l33t_tree *tmp = root->left;
    root->left = root->right;
    root->right = tmp;

    invert(root->left);
    invert(root->right);
  }
}

Test(InvertBtree, InvertBtreeTests)
{
  l33t_tree node7 = {NULL, NULL, 9};
  l33t_tree node6 = {NULL, NULL, 6};
  l33t_tree node5 = {NULL, NULL, 3};
  l33t_tree node4 = {NULL, NULL, 1};
  l33t_tree node3 = {&node6, &node7, 7};
  l33t_tree node2 = {&node4, &node5, 2};
  l33t_tree node1 = {&node2, &node3, 4};

  invert(&node1);

  cr_expect(node1.val == 4);
  cr_expect(node1.left->val == 7);
  cr_expect(node1.right->val == 2);
  cr_expect(node1.left->left->val == 9);
  cr_expect(node1.left->right->val == 6);
  cr_expect(node1.right->val == 2);
  cr_expect(node1.right->left->val == 3);
  cr_expect(node1.right->right->val == 1);
}

Test(InvertBtree, InvertBtreeTests2)
{
  l33t_tree node3 = {NULL, NULL, 3};
  l33t_tree node2 = {NULL, NULL, 1};
  l33t_tree node1 = {&node2, &node3, 2};

  invert(&node1);

  cr_expect(node1.val == 2);
  cr_expect(node1.left->val == 3);
  cr_expect(node1.right->val == 1);
}
