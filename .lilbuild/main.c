#include <stdio.h>
#define type_finder(type) \
_Generic((type), char : "%c", int: "%d", float: "%f", char*: "%s")
#define print(value) \
printf(type_finder(value), value)
#define input(value) \
scanf(type_finder(value), &value)
