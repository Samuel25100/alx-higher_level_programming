#include "lists.h"
/**
 * check_cycle - check whether the list contain a cycle
 * @list: linked list to be checked
 * Return: 1 if there is a cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}

	return (0);
}
