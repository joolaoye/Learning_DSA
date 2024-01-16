#include <stdio.h>
#include <stdlib.h>

#define None NULL

typedef struct node{
    int val;
    struct node* next;
}node;

int main(){
    node* list = None;

    node* n = malloc(sizeof(node));
    if (n == None){
        return 1;
    }

    n->val = 1;
    n->next = None;

    list = n;

    n = malloc(sizeof(node));
    if (n == None){
        return 1;
    }

    n->val = 2;
    n->next = None;

    list->next = n;

    n = malloc(sizeof(node));

    n->val = 3;
    n->next = None;

    list->next->next = n;

    node* tail = list;

    while (tail != None){
        printf("%i\n", tail->val);

        tail = tail->next;
    }
}