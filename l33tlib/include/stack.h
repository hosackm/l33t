#pragma once

#include <l33t.h>

typedef struct stack_s l33t_stack;
struct stack_s
{
  int *array;
};

l33t_stack *l33t_stack_init();

void l33t_stack_destroy(l33t_stack *st);

l33t_error_code l33t_stack_push(l33t_stack *st, int value);
l33t_error_code l33t_stack_pop(l33t_stack *st, int *value);
l33t_error_code l33t_stack_peek(l33t_stack *st, int *value);
int l33t_stack_is_empty(l33t_stack *st);
