#include <criterion/criterion.h>

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

Test(ValidParens, ValidParensTests)
{
  static const char *inputs[5] = {
      "()", "[]", "{}", "([{}])", "{([])}",
  };
  for (int i = 0; i < 5; i++)
  {
    cr_expect(valid_parentheses(inputs[i]) == 1);
  }
}
