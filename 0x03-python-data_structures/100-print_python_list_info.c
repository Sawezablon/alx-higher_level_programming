#include <Python.h>

/**
 * print_python_list_info - Prints Python lists.
 * @p: pointer list.
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int new;
	int len;
	PyObject *o;
	int zab = 0;

	len = Py_SIZE(p);
	new = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", new);

	while (zab < len)
	{
		printf("Element %d: ", zab);

		o = PyList_GetItem(p, zab);
		printf("%s\n", Py_TYPE(o)->tp_name);

		zab++;
	}

}
