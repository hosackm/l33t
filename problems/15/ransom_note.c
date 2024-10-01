#include <criterion/criterion.h>
#include <string.h>

#define STB_DS_IMPLEMENTATION
#include <stb_ds.h>

typedef struct
{
  char key;
  int value;
} counter_t;

counter_t *count_letters(const char *s)
{
  counter_t *hash = NULL;
  for (unsigned long i = 0; i < strlen(s); i++)
  {
    if (hmgeti(hash, s[i]) != -1)
    {
      const int count = hmget(hash, s[i]);
      hmput(hash, s[i], count + 1);
    }
    else
    {
      hmput(hash, s[i], 1);
    }
  }
  return hash;
}

int can_construct(const char *note, const char *magazine)
{
  counter_t *note_count = count_letters(note);
  counter_t *mag_count = count_letters(magazine);

  for (int i = 0; i < hmlen(note_count); i++)
  {
    const char ch = note_count[i].key;
    const int count = note_count[i].key;
    if (hmgeti(mag_count, ch) == -1 || hmget(mag_count, ch) < count)
    {
      return 0;
    }
  }

  return 1;
}

TestSuite(RansomNote);
Test(RansomNote, RansomNoteTests)
{
  cr_expect(!can_construct("a", "b"));
  cr_expect(!can_construct("aa", "ab"));
  cr_expect(!can_construct("aa", "aab"));
}
