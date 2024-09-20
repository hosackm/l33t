#include <glib.h>

#define STB_DS_IMPLEMENTATION
#include <stb_ds.h>

int valid_parentheses(const char *s)
{
  char *stack = NULL;
  for (int i = 0; s[i] != '\0'; i++)
  {
    switch (s[i])
    {
    case '(':
    case '[':
    case '{':
      arrpush(stack, s[i]);
      break;
    case ')':
      if (arrpop(stack) != '(')
      {
        return 0;
      }
      break;
    case ']':
      if (arrpop(stack) != '[')
      {
        return 0;
      }
      break;
    case '}':
      if (arrpop(stack) != '{')
      {
        return 0;
      }
      break;
    }
  }

  return arrlen(stack) == 0;
}

void test_parens()
{
  static const char *inputs[5] = {
      "()", "[]", "{}", "([{}])", "{([])}",
  };
  for (int i = 0; i < 5; i++)
  {
    g_assert_cmpint(1, ==, valid_parentheses(inputs[i]));
  }
}

int main(int argc, char *argv[])
{
  g_test_init(&argc, &argv, NULL);
  g_test_add_func("/valid_parentheses", test_parens);
  return g_test_run();
}
