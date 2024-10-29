#include <criterion/criterion.h>
#include <l33t.h>

int max_area(int *heights, int num)
{
  if (heights == NULL || num <= 0)
  {
    return 0;
  }

  int max = 0;
  int left = 0;
  int right = num - 1;
  while (left < right)
  {
    const int area = MIN(heights[left], heights[right]) * (right - left);
    max = area > max ? area : max;
    heights[left] < heights[right] ? left++ : right--;
  }

  return max;
}

TestSuite(WaterContainerTests);
Test(WaterContainerTests, LeetcodeExamples)
{
  typedef struct
  {
    int heights[9];
    int num;
    int expected;
  } input;
  input inputs[5] = {
      {.heights = {1, 8, 6, 2, 5, 4, 8, 3, 7}, .num = 9, .expected = 49},
      {.heights = {1, 1}, .num = 2, .expected = 1},
      {.heights = {1, 2, 4, 3}, .num = 4, .expected = 4},
      {.heights = {2, 3, 4, 5, 18, 17, 6}, .num = 7, .expected = 17},
      {.heights = {1, 0, 0, 0, 0, 0, 0, 2, 2}, .num = 9, .expected = 8},
  };
  for (int i = 0; i < (int)ARRAY_SIZE(inputs, input); i++)
  {
    input in = inputs[i];
    const int area = max_area(in.heights, in.num);
    cr_expect(area == in.expected);
  }
}
