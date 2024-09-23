#include <criterion/criterion.h>

int binary_search(int *nums, int len, int target)
{
  int low = 0;
  int high = len - 1;
  while (low <= high)
  {
    int mid = (low + high) / 2;
    if (target < nums[mid])
    {
      high = mid - 1;
    }
    else if (target > nums[mid])
    {
      low = mid + 1;
    }
    else
    {
      return mid;
    }
  }
  return -1;
}

Test(BinarySearch, BinarySearchTests)
{
  {
    int nums[6] = {-1, 0, 3, 5, 9, 12};
    cr_expect(binary_search(nums, 6, 9) == 4);
  }
  {
    int nums[6] = {-1, 0, 3, 5, 9, 12};
    cr_expect(binary_search(nums, 6, 2) == -1);
  }
  {
    int nums[1] = {5};
    cr_expect(binary_search(nums, 1, -5) == -1);
  }
}
