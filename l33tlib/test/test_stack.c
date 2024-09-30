#include "error.h"
#include <criterion/criterion.h>
#include <l33t.h>

TestSuite(StackTests);
Test(StackTests, InitializesCorrectly)
{
  l33t_error_code err = L33T_ERR_OK;

  l33t_stack *st = l33t_stack_init();
  cr_expect(l33t_stack_is_empty(st));

  err = l33t_stack_push(st, 1);
  cr_expect(err == L33T_ERR_OK);

  err = l33t_stack_push(st, 2);
  cr_expect(err == L33T_ERR_OK);

  err = l33t_stack_push(st, 3);
  cr_expect(err == L33T_ERR_OK);

  cr_expect(!l33t_stack_is_empty(st));

  int value;
  err = l33t_stack_pop(st, &value);
  cr_expect(err == L33T_ERR_OK);
  cr_expect(value == 3);

  err = l33t_stack_pop(st, &value);
  cr_expect(err == L33T_ERR_OK);
  cr_expect(value == 2);

  err = l33t_stack_pop(st, &value);
  cr_expect(err == L33T_ERR_OK);
  cr_expect(value == 1);

  cr_expect(l33t_stack_is_empty(st));

  err = l33t_stack_pop(st, &value);
  cr_expect(err == L33T_ERR_EMPTY_CONTAINER);

  l33t_stack_destroy(st);
}
