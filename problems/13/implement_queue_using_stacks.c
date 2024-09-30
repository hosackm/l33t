#include "error.h"
#include "stack.h"
#include <criterion/criterion.h>
#include <l33t.h>

typedef struct queue_s queue;
struct queue_s
{
  l33t_stack *stack;
  l33t_stack *auxiliary;
};

queue *queue_init()
{
  queue *q = malloc(sizeof(queue));
  q->stack = l33t_stack_init();
  q->auxiliary = l33t_stack_init();
  return q;
}

void queue_destroy(queue *q)
{
  if (q)
  {
    free(q->stack);
    free(q->auxiliary);
    free(q);
  }
}

l33t_error_code queue_push(queue *q, int val)
{
  return l33t_stack_push(q->stack, val);
}

int queue_pop(queue *q)
{
  int ret = 0;
  while (!l33t_stack_is_empty(q->stack))
  {
    int value = 0;
    l33t_stack_pop(q->stack, &value);

    if (l33t_stack_is_empty(q->stack))
    {
      ret = value;
      break;
    }

    l33t_stack_push(q->auxiliary, value);
  }

  while (!l33t_stack_is_empty(q->auxiliary))
  {
    int value = 0;
    l33t_stack_pop(q->auxiliary, &value);
    l33t_stack_push(q->stack, value);
  }

  return ret;
}

int queue_peek(queue *q)
{
  int ret = 0;
  while (!l33t_stack_is_empty(q->stack))
  {
    l33t_stack_pop(q->stack, &ret);
    l33t_stack_push(q->auxiliary, ret);
  }

  while (!l33t_stack_is_empty(q->auxiliary))
  {
    int value = 0;
    l33t_stack_pop(q->auxiliary, &value);
    l33t_stack_push(q->stack, value);
  }

  return ret;
}

int queue_is_empty(queue *q)
{
  return l33t_stack_is_empty(q->stack);
}

TestSuite(QueueFromStacks);

Test(QueueFromStacks, InitAndPushOne)
{
  l33t_error_code err = L33T_ERR_OK;
  queue *q = queue_init();

  cr_expect(queue_is_empty(q));

  err = queue_push(q, 1);
  cr_expect(err == L33T_ERR_OK);

  cr_expect(!queue_is_empty(q));

  int value = queue_pop(q);
  cr_expect(value == 1);

  queue_destroy(q);
}

Test(QueueFromStacks, PushMultiplePopMultiple)
{
  l33t_error_code err = L33T_ERR_OK;
  queue *q = queue_init();

  for (int i = 0; i < 3; i++)
  {
    err = queue_push(q, i);
    cr_expect(err == L33T_ERR_OK);
  }

  for (int i = 0; i < 3; i++)
  {
    int value = queue_pop(q);
    cr_expect(value == i);
  }

  cr_expect(queue_is_empty(q));

  queue_destroy(q);
}

Test(QueueFromStacks, PushMultiPeekMulti)
{
  l33t_error_code err = L33T_ERR_OK;
  const int num_pushes = 20;
  queue *q = queue_init();

  for (int i = 0; i < num_pushes; i++)
  {
    err = queue_push(q, i);
    cr_expect(err == L33T_ERR_OK);
  }

  for (int i = 0; i < num_pushes; i++)
  {
    cr_expect(queue_peek(q) == i);
    cr_expect(queue_pop(q) == i);
  }

  cr_expect(queue_is_empty(q));

  queue_destroy(q);
}
