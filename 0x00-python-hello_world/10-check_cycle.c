#include "lists.h"
/**
 * check_cycle - check if singly-linked list contains cycle
 * @list: singly-linked list
 * Return: always int
 * case: 1 true, 0 false
 */
int check_cycle(listint_t *list)
{
	listint_t *check = list, *has = list;
	while (check != NULL && has != NULL && has->next != NULL)
	{
		check = check->next;
		has = has->next->next;
		if (check == has)
			return (1);
	}
return (0);
}
