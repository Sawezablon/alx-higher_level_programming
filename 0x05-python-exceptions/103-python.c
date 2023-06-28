#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>
#include <Python.h>
#include <object.h>

void print_python_float(PyObject *p)
{
    char *ptr = NULL;
    PyFloatObject *zab = (PyFloatObject *)p;
    double z = zab->ob_fval;

    printf("[.] float object info\n");
    if (!PyFloat_Check(zab))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    
    ptr = PyOS_double_to_string(z, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", ptr);
}

void print_python_bytes(PyObject *p)
{
    long unsigned int len;
    unsigned int z;
    char *ptr = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    len = ((PyVarObject *)p)->ob_size;
    ptr = ((PyBytesObject *)p)->ob_sval;
    printf("  len: %lu\n", len);
    printf("  trying string: %s\n", ptr);
    if (len < 10)
        printf("  first %lu bytes:", len + 1);
    else
        printf("  first 10 bytes:");
    for (z = 0; z <= len && z < 10; z++)
        printf(" %02hhx", ptr[z]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    long unsigned int len;
    unsigned int z;
    PyListObject *list = (PyListObject *)p;
    const char *ptr;

    printf("[*] Python list info\n");
    if (!PyList_Check(list))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    len = ((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %lu\n", len);
    printf("[*] Allocated = %lu\n", list->allocated);
    for (z = 0; z < len; z++)
    {
        ptr = (list->ob_item[z])->ob_type->tp_name;
        printf("Element %z: %s\n", z, ptr);
        if (!strcmp(ptr, "bytes"))
            print_python_bytes(list->ob_item[z]);
        if (!strcmp(ptr, "float"))
            print_python_float(list->ob_item[z]);
    }
}
