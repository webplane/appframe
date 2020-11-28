# Introduction and Installation

Appframe is an open source python library that reduces the code and complexity of developing command line applications. It handles most of the low level logic while enforcing a modular architecture.

##  Features

- [x] 2 lines of code for the `main` function
- [x] Composition of the CLI commands from a *commands/* directory


Appframe leverages the follwing greate libraries:

- https://pypi.org/project/cleo/
- https://pypi.org/project/simple-plugin-loader/

## Installation

Appframe is avaiable from the official Python Package Index (PIP), you can install it from the terminal:
```bash
pip install appframe
```

##  Hello World
main.py
```python
import appframe


appframe.main(__name__, __file__, "test-app", "0.1")
```

_commands/hello.py_
```python
from appframe import Command, verbose


class CreateCommand(Command):
    """
    Greet a person

    greet
        {person? : name of the person to greet}
    """

    def handle(self):
        person = self.argument("person") or "Peter"
        verbose(1, "Greeting person")
        print(f"Hello {person}")
```

Test the app:
```sh
python test.py greet Joe
```
