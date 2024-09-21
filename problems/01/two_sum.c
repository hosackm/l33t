#include <criterion/criterion.h>

#define STB_DS_IMPLEMENTATION
#include <stb_ds.h> // hashmap

typedef struct
{
  int first;
  int second;
} answer;

answer two_sum(int *nums, int len, int target)
{
  answer a = {0};
  struct
  {
    int key;
    int value;
  } *hash = NULL;

  for (int i = 0; i < len; i++)
  {
    int compliment = target - nums[i];
    if (hmgeti(hash, compliment) != -1)
    {
      a.first = hmget(hash, compliment);
      a.second = i;
      return a;
    }
    else
    {
      hmput(hash, nums[i], i);
    }
  }
  return a;
}

Test(TwoSum, TwoSumTests)
{
  typedef struct test
  {
    int inputs[4];
    int len;
    int target;
    answer answer;
  } test_s;

  test_s tests[3] = {
      {{2, 7, 11, 5}, 4, 9, {0, 1}},
      {{3, 2, 4}, 3, 6, {1, 2}},
      {{3, 3}, 2, 6, {0, 1}},
  };

  for (int i = 0; i < 3; i++)
  {
    test_s test = tests[i];
    answer a = two_sum(test.inputs, test.len, test.target);
    cr_expect(a.first == test.answer.first);
  }
}
