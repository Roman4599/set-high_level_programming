#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *current, *second;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	prev = NULL;

	/* find middle while reversing the first half */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		current = slow;
		slow = slow->next;
		current->next = prev;
		prev = current;
	}

	/* odd number of nodes: skip the middle node */
	if (fast != NULL)
		slow = slow->next;

	second = slow;

	while (prev != NULL && second != NULL)
	{
		if (prev->n != second->n)
			return (0);
		prev = prev->next;
		second = second->next;
	}

	return (1);
}