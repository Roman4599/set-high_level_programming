#include <Python.h>
#include <string.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t size, limit, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	s = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %.*s\n", (int)size, s);
	limit = size + 1;
	if (limit > 10)
		limit = 10;
	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)s[i]);
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, allocated, i;
	const char *type;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	allocated = ((PyListObject *)(p))->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)(p))->ob_item[i];
		type = ((PyObject *)(item))->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}