#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: the Python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i, size;

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(list);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
		printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}