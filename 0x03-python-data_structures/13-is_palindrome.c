#include "lists.h"

/**
* is_palindrome - function that checks if a list is a palindrome.
* @head: a pointer to pointer
* Return: 1 or 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *new = *head;
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (current != NULL && current->next != NULL)
	{
		current = current->next->next;
		next = new->next;
		new->next = prev;
		prev = new;
		new = next;
	}

	if (current != NULL)
	{
		new = new->next;
	}

	while (prev != NULL && new != NULL)
	{
		if (prev->n != new->n)
		{
			return (0);
		}
		prev = prev->next;
		new = new->next;
	}

	return (1);
}
