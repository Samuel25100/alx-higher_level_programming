#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *nex = *head;
	int buf[100], count, x;

	if (*head == NULL)
	{
	return (1);
	}

	for (count = 0; nex; count++)
	{
	buf[count] = nex->n;
	nex = nex->next;
	}
	count = count - 1;
	for (x = 0; x <= count; x++)
	{
	printf("count = %d", count);
	if (buf[x] != buf[count])
		return (0);
	count--;
	}
	return (1);
}
