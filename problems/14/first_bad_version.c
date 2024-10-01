#include <criterion/criterion.h>
#include <stdint.h> // uint32_t

/*
 * Using uint32_t because leetcode specifically tests the case where
 * versions go up to (2^32) - 1.
 */

// callback function to be used inside solution function
typedef int (*bad_version_func)(uint32_t);

uint32_t first_bad_version(uint32_t num_versions, bad_version_func is_bad)
{
  uint32_t low = 1;
  uint32_t high = num_versions;
  uint32_t bad = high;
  while (low <= high)
  {
    const uint32_t mid = (low + high) / 2;
    if (is_bad(mid))
    {
      bad = mid;
      high = mid - 1;
    }
    else
    {
      low = mid + 1;
    }
  }

  return bad;
}

TestSuite(FirstBadVersion);

int is_bad_test_1(uint32_t version)
{
  return version >= 4;
}

int is_bad_test_2(uint32_t version)
{
  return version >= 1;
}

Test(FirstBadVersion, LeetcodeExamples)
{
  uint32_t bad_version = first_bad_version(5, is_bad_test_1);
  cr_expect(bad_version == 4);

  bad_version = first_bad_version(1, is_bad_test_2);
  cr_expect(bad_version == 1);
}
