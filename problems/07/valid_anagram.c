#include <criterion/criterion.h>
#include <string.h>

int valid_anagram(const char *s, const char *t)
{
  int counts[26] = {0};

  if (strlen(s) != strlen(t))
  {
    return 0;
  }

  for (int i = 0; s[i] != '\0'; i++)
  {
    counts[s[i] - 'a']++;
    counts[t[i] - 'a']--;
  }

  // all values should be 0
  for (int i = 0; i < 26; i++)
  {
    if (counts[i])
    {
      return 0;
    }
  }

  return 1;
}

Test(ValidAnagram, LeetcodeExamples)
{
  cr_expect(valid_anagram("anagram", "nagaram") == 1);
  cr_expect(valid_anagram("rat", "tag") == 0);
}
