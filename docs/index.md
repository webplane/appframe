# Introduction and Installation

!!! Important
    This documentation is on the initial phase of development, breaking changes are likely to be introduced until the v1.0 release.

Appframe is an open souurce python library that reduces the code and complexity of developing a command line applications by handling most of the logic that is common to a typical application lifecycle.

##  Features

- [x] Automatic composition of the CLI syntax from plain python modulues

Appframe leverages the follwing greate libraries:

- https://pypi.org/project/cleo/
- https://pypi.org/project/simple-plugin-loader/

## Installation

Webplane is avaiable from the official Python Package Index (PIP), you can install it from the terminal:
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

Now test it with:
```sh
python test.py greet Joe
```