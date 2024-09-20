#include <glib.h>
#include <stdio.h>
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

void test_valid_anagram()
{
  g_assert_cmpint(1, ==, valid_anagram("anagram", "nagaram"));
  g_assert_cmpint(0, ==, valid_anagram("rat", "tag"));
}

int main(int argc, char **argv)
{
  g_test_init(&argc, &argv, NULL);
  g_test_add_func("/valid_anagram", test_valid_anagram);
  return g_test_run();
}
