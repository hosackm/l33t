#include <stdint.h>

#include <criterion/criterion.h>

uint16_t climb(uint16_t n)
{
  if (n < 3)
  {
    return n;
  }

  // start from the second step.
  uint16_t step = 2;
  uint16_t last = 2;
  uint16_t down_two = 1;
  while (step < n)
  {
    uint16_t tmp = last;
    last += down_two;
    down_two = tmp;
    step++;
  }
  return last;
}

Test(ClimbingStairsTests, LeetcodeExamples)
{
  cr_expect(climb(2) == 2);
  cr_expect(climb(3) == 3);
  cr_expect(climb(4) == 5);
  cr_expect(climb(5) == 8);
  cr_expect(climb(6) == 13);
}
