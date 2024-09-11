#include <stdlib.h>
#include <stdio.h>


typedef struct ListNode
{
    int val;
    struct ListNode *next;
} list_node_s;
typedef list_node_s* list_node;

/*
 * Merge two lists and return a new list allocated on the heap.
 * ie. user must free returned list.
*/
list_node merge(list_node list1, list_node list2) {
    unsigned int total_size = 0;
    list_node ptr = list1;
    while(ptr != NULL)
    {
        total_size++;
        ptr = ptr->next;
    }
    ptr = list2;
    while(ptr != NULL)
    {
        total_size++;
        ptr = ptr->next;
    }

    list_node output = malloc(sizeof(list_node_s) * total_size);
    if (!output)
    {
        return NULL;
    }

    for(int i = 0; i < total_size; i++)
    {
        output[i].next = (i == (total_size-1)) ? NULL : &output[i+1];
    }

    unsigned int i = 0;
    while(list1 && list2)
    {
        ptr = &output[i++];
        if(list1->val < list2->val)
        {
            ptr->val = list1->val;
            list1 = list1->next;
        }
        else
        {
            ptr->val = list2->val;
            list2 = list2->next;
        }
        ptr = ptr->next;
    }

    while(list1)
    {
        ptr = &output[i++];
        ptr->val = list1->val;
        list1 = list1->next;
    }
    while(list2)
    {
        ptr = &output[i++];
        ptr->val = list2->val;
        list2 = list2->next;
    }

    return output;
}

list_node merge2(list_node list1, list_node list2) {
    unsigned int total_size = 0;

    list_node before = NULL;
    list_node ptr = NULL;

    while(list1 && list2)
    {
        list_node min = NULL;
        if(list1->val < list2->val)
        {
            min = list1;
            list1 = list1->next;
        }
        else
        {
            ptr->next->val = list2->val;
            list2 = list2->next;
        }

        if(before)
        {
            before->next = ptr;
        }
        before = ptr;
        ptr = ptr->next;
    }

    while(list1)
    {
        ptr = &output[i++];
        ptr->val = list1->val;
        list1 = list1->next;
    }
    while(list2)
    {
        ptr = &output[i++];
        ptr->val = list2->val;
        list2 = list2->next;
    }

    return output;
}

int main(int argc, char **argv)
{
    list_node_s node1;
    list_node_s node2;
    list_node_s node3;
    list_node_s node4;
    list_node_s node5;
    list_node_s node6;
    list_node ptr;

    node1.val = 1;
    node1.next = &node2;
    node2.val = 2;
    node2.next = &node3;
    node3.val = 4;
    node3.next = NULL;

    node4.val = 1;
    node4.next = &node5;
    node5.val = 3;
    node5.next = &node6;
    node6.val = 4;
    node6.next = NULL;

    list_node list1 = &node1;
    list_node list2 = &node4;

    list_node merged = merge(list1, list2);

    const int expected[6] = {1, 1, 2, 3, 4, 4};
    ptr = merged;
    for(int i = 0; i < 6; i++)
    {
        if(!ptr || ptr->val != expected[i])
        {
            printf("TEST FAILED!\n");
            exit(1);
        }
        ptr = ptr->next;
    }
    printf("TEST SUCCEEDED!\n");

    free(ptr);
}
