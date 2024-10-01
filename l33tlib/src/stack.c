#include "stack.h"
#include <l33t.h>
#include <string.h> // memset

#define STB_DS_IMPLEMENTATION
#include <stb_ds.h>

l33t_stack *l33t_stack_init()
{
  l33t_stack *st = malloc(sizeof(l33t_stack));
  memset(st, 0, sizeof(l33t_stack));
  return st;
}

void l33t_stack_destroy(l33t_stack *st)
{
  free(st);
}

l33t_error_code l33t_stack_push(l33t_stack *st, int value)
{
  arrpush(st->array, value);
  return L33T_ERR_OK;
}

l33t_error_code l33t_stack_pop(l33t_stack *st, int *value)
{
  if (!st || !value)
  {
    return L33T_ERR_NULL_POINTER;
  }

  const int length = arrlen(st->array);
  if (length == 0)
  {
    return L33T_ERR_EMPTY_CONTAINER;
  }

  *value = st->array[length - 1];
  arrsetlen(st->array, length - 1);

  return L33T_ERR_OK;
}

l33t_error_code l33t_stack_peek(l33t_stack *st, int *value)
{
  if (!st || !value)
  {
    return L33T_ERR_NULL_POINTER;
  }

  const int length = arrlen(st->array);
  if (length == 0)
  {
    return L33T_ERR_EMPTY_CONTAINER;
  }

  *value = st->array[length - 1];
  return L33T_ERR_OK;
}

int l33t_stack_is_empty(l33t_stack *st)
{
  return arrlen(st->array) == 0;
}
