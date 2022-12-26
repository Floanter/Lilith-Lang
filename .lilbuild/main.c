#include <stdio.h>
#define LIST_INIT_CAPACITY 4
typedef struct List 
{
 void **items;
int capacity;
int lenght;
} List;
void list_init(List* l)
{
 l->capacity = LIST_INIT_CAPACITY;
 l->lenght = 0;
 l->items = malloc(sizeof(void*) * l->capacity);
}
void list_free(List* l)
{
free(l->items);
}
int list_lenght(List* l)
{
return l->lenght;
}
static void list_resize(List* l, int capacity)
{
void* items = realloc(l->items, sizeof(void*) * capacity);
if (items)
{
 l->items = items;
 l->capacity = capacity;
}
}
void list_push(List* l, void* item)
{
if (l->capacity == l->lenght)
{
list_resize(l, l->capacity * 2);
}
 l->items[l->lenght++] = item;
}
