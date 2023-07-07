#include <Python.h>
#include <object.h>
#include <unicodeobject.h>


void print_python_string(PyObject *p)
{
    const char *ptr = NULL;
    Py_ssize_t size = 0;
    wchar_t *ch = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        ptr = "compact ascii";
    else
        ptr = "compact unicode object";

    ch = PyUnicode_AsWideCharString(p, &size);

    printf("  type: %s\n", ptr);
    printf("  length: %ld\n", size);
    printf("  value: %ls\n", ch);
}
