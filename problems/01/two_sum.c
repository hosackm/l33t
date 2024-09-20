#include <glib.h> // testing

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

void test_two_sum()
{
  static const int num_tests = 3;
  typedef struct test
  {
    int inputs[4];
    int len;
    int target;
    answer answer;
  } test_s;

  test_s tests[num_tests] = {
      {{2, 7, 11, 5}, 4, 9, {0, 1}},
      {{3, 2, 4}, 3, 6, {1, 2}},
      {{3, 3}, 2, 6, {0, 1}},
  };

  for (int i = 0; i < num_tests; i++)
  {
    test_s test = tests[i];
    answer a = two_sum(test.inputs, test.len, test.target);
    g_assert_cmpint(a.first, ==, test.answer.first);
  }
}

int main(int argc, char *argv[])
{
  g_test_init(&argc, &argv, NULL);
  g_test_add_func("/two_sum", test_two_sum);
  return g_test_run();
}
