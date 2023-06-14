#include <listobject.h>
#include <bytesobject.h>
#include <Python.h>
#include <object.h>

/**
* print_python_bytes - python bytes
*
* @p: a pointer parameter
* Return: Nothing
*/
void print_python_bytes(PyObject *p)
{
	long int len;
	int zab = 0;
	char *ch = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("	[ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &ch, &len);

	printf("	size: %li\n", len);
	printf("	trying string: %s\n", ch);
	if (len < 10)
		printf("	first %li bytes:", len + 1);
	else
		printf("	first 10 bytes:");
	while (zab <= len && zab < 10)
	{
		printf(" %02hhx", ch[zab]);
	    zab++;
	}
	printf("\n");
}

/**
* print_python_list - Python lists
*
* @p: a pointer parameter
* Return: Nothing
*/
void print_python_list(PyObject *p)
{
	PyListObject *list;
	const char *type;
	long int len;
	int zab = 0;

	len = PyList_Size(p);
	list = (PyListObject *)p
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", list->allocated);
	while (zab < len)
	{
		type = (list->ob_item[zab])->ob_type->tp_name;
		printf("Element %zab: %s\n", zab, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[zab]);
	    zab++;
	}
}
