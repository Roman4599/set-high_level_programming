#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 * Uses Floyd's tortoise and hare: the slow pointer moves one node at a
 * time while the fast one moves two, so a cycle is detected in linear
 * time and constant space, without touching the list.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
