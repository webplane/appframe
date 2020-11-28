# Introduction and Installation

!!! Important
    This documentation is on the initial phase of development, breaking changes are likely to be introduced until the v1.0 release.

Appframe is an open souurce python library that reduces the code and complexity of developing a command line applications by handling most of the logic that is common to a typical application lifecycle.

##  Features

- [x] 2 lines of code on your `main` file
- [x] Composition of the CLI syntax from modules in the ***commands/*** directory

Appframe leverages the follwing great libraries:

- https://pypi.org/project/cleo/
- https://pypi.org/project/simple-plugin-loader/

## Installation

Webplane is avaiable from the official Python Package Index (PIP), you can install it from the terminal:
```bash
pip install appframe
```

##  Hello World
_main.py_
```python
import appframe

appframe.main(__name__, __file__)
```

_commands/hello.py_
```python
from appframe import Command


class CreateCommand(Command):
    """
    Greet a person

    greet
        {person? : name of the person to greet}
    """

    def handle(self):
        person = self.argument,get("person") or "Peter"
        print(f"Hello {person}")
```
