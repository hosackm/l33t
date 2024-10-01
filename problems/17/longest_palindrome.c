#include <stdint.h>
#include <string.h>

#include <criterion/criterion.h>

#define STB_DS_IMPLEMENTATION
#include <stb_ds.h>

typedef struct
{
  char key;
  uint16_t value;
} counter_t;

int longest_palindrome(const char *str)
{
  counter_t *hash = NULL;
  for (uint32_t i = 0; i < strlen(str); i++)
  {
    if (hmgeti(hash, str[i]) == -1)
    {
      hmput(hash, str[i], 1);
    }
    else
    {
      const uint16_t count = hmget(hash, str[i]);
      hmput(hash, str[i], count + 1);
    }
  }

  uint16_t sum = 0;
  uint16_t found_odd = 0;
  for (int i = 0; i < hmlen(hash); i++)
  {
    const uint16_t count = hash[i].value;
    found_odd = (count % 2) == 1 ? 1 : found_odd;
    sum += count / 2;
  }

  return sum + found_odd;
}

Test(LongestPalindromTests, LongestPalindromeExamples)
{
  cr_expect(longest_palindrome("abccccdd"));
  cr_expect(longest_palindrome("a") == 1);
}
