#include <criterion/criterion.h>

int buy_sell(int *nums, int len)
{
  int profit = 0;

  for (int left = 0, right = 1; left < len && right < len; right++)
  {
    int current = nums[right] - nums[left];
    if (current > profit)
    {
      profit = current;
    }
    else if (current < 0)
    {
      left = right;
    }
  }

  return profit;
}

Test(BuySell, BuySellTests)
{
  int t1[6] = {7, 1, 5, 3, 6, 4};
  cr_expect(5 == buy_sell(t1, 6));

  int t2[5] = {7, 6, 4, 3, 1};
  cr_expect(0 == buy_sell(t2, 5));

  cr_expect(0 == buy_sell(NULL, 0));

  int t3[1] = {1};
  cr_expect(0 == buy_sell(t3, 1));

  int t4[2] = {1, 0};
  cr_expect(0 == buy_sell(t4, 2));
}
