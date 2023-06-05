#include "lists.h"

/**
  * check_cycle - function in C that checks if a singly linked list
  * @list: a ponter to structure
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *ch;
	listint_t *str;

	ch = list;
	str = list;
	while (list && ch && ch->next)
	{
		list = list->next;
		ch = ch->next->next;

		if (list == ch)
		{
			list = str;
			str =  ch;
			while (1)
			{
				ch = str;
				while (ch->next != list && ch->next != str)
				{
					ch = ch->next;
				}
				if (ch->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
