#include <criterion/criterion.h>
#include <stdint.h>

int valid_palindrome(const char *s, size_t len)
{
  const char *end = s + len - 1;
  while (s < end)
  {
    if (*s != *end)
    {
      return 0;
    }
    s++;
    end--;
  }

  return 1;
}

Test(ValidPalindrome, ValidPalindromeTests)
{
  cr_expect(valid_palindrome("racecar", 7) == 1);
  cr_expect(valid_palindrome("panama", 6) == 0);
  cr_expect(valid_palindrome("amanaplanacanalpanama", 21) == 1);
}
