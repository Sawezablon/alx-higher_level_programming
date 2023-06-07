#include "lists.h"
#include <stdlib.h>

/**
* insert_node - insert node to sorted list
* @head: pointer to a pointer listint_t
* @number: number to be inserted
*
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *previous;

	current = *head;
	previous = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	return (NULL);

	new->n = number;
	new->next = NULL;

	while (current != NULL && current->n < number)
	{
	previous = current;
	current = current->next;
	}
	if (previous == NULL)
	{
	new->next = *head;
	*head = new;
	}
	else
	{
	previous->next = new;
	new->next = current;
	}

	return (new);
}
