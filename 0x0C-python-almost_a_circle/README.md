# 0x0C. Python - Almost a Circle

This project focuses on various concepts and techniques in Python programming. It involves working with object-oriented programming (OOP) principles, implementing unit tests, serialization, deserialization, reading/writing JSON files, handling named arguments, and more.

## Project Overview

The project consists of the following tasks:

1. Implement unit tests for all files, classes, and methods.
2. Create the `Base` class with the following features:
   - Private class attribute `__nb_objects = 0`.
   - Class constructor `__init__(self, id=None)`.
3. Implement the `Rectangle` class, which inherits from `Base`:
   - Private instance attributes: `__width`, `__height`, `__x`, `__y`.
   - Class constructor `__init__(self, width, height, x=0, y=0, id=None)`.
4. Validate attributes in the `Rectangle` class:
   - Implement validation for width, height, x, and y attributes.
5. Implement the `area` method in the `Rectangle` class.
6. Implement the `display` method in the `Rectangle` class.
7. Override the `__str__` method in the `Rectangle` class.
8. Enhance the `display` method in the `Rectangle` class.
9. Implement the `Square` class, which inherits from `Rectangle`:
   - Class constructor `__init__(self, size, x=0, y=0, id=None)`.
10. Add getter and setter methods for the `size` attribute in the `Square` class.
11. Implement the `update` method in the `Square` class.
12. Implement the `to_dictionary` method in the `Rectangle` class.
13. Implement the `to_dictionary` method in the `Square` class.
14. Add the `to_json_string` static method in the `Base` class.
15. Implement the `save_to_file` class method in the `Base` class.
16. Implement the `from_json_string` static method in the `Base` class.
17. Implement the `create` class method in the `Base` class.
18. Implement the `load_from_file` class method in the `Base` class.

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*
- All files must be executable.
- All modules, classes, and functions must be documented.
- Code must pass the PEP 8 style guide.

## Usage

1. Clone the repository:


2. Navigate to the project directory:


3. Run the unit tests:


4. Execute specific test files:


## File Structure

The project has the following file structure:

models/
init.py
base.py
rectangle.py
square.py
tests/
init.py
test_models/
init.py
test_base.py
test_rectangle.py
test_square.py
