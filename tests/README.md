# Pytest - Common Components

## Fixtures

Fixtures are used when we want to run some code before every test method. So instead of repeating the same code in every test we define fixtures.

See `test_fixture_example()` in `test_pytest_reusable_components.py`.

## PytestConfig

Pytest config builtins allow you to provide additional command line arguments to your pytests. A good overview is described here: [Using pytestconfig](https://medium.com/pragmatic-programmers/using-pytestconfig-eaeacedbe29a).

They're also commonly used with fixtures as a way to always provide an additional input to all test cases.

See `pytestconfig_fixture_eg` in `test_pytest_reusable_components.py`.

## Parameterize

<TODO>

---

## Useful Pytest Command Line Args

* `-k`: this is used to only run target tests that match your substring expression. See `pytest_fixture_example` in the `Makefile`.

### Reporting Args

* `--no-header`: disable the header. IMO, this doesn't add any value and should be disabled by default.
* `-q`: this is used to decrease verbosity. I again tend to include this as a default arg.
* `--disable-pytest-warnings`: this is more subjective/but this will disable all pytest warnings. There are occassions when you will want to see these, so I recommend not including these as a default arg.

---

### Useful links

* Summary of command line args: [Exploring pytest command line options](https://qxf2.com/blog/pytest-command-line-options/).
* [Structuring Unit Tests in Python](https://medium.com/python-in-plain-english/unit-testing-in-python-structure-57acd51da923).

---

## Exception types

For a list of exception types, see: [python exception types](https://docs.python.org/3/library/exceptions.html#os-exceptions)

Common exception types:

* KeyError: when a mapping (directionary) key is not found in the set of existing keys
* FileNotFoundError: when a file or directory is requested but doesn’t exist
* TypeError: operation or function is applied to an object of inappropriate type
* ValueError: when an operation or function receives an argument that has the right type but an inappropriate value

## Error types

For a list of python error types, see: [python error types]https://www.tutorialsteacher.com/python/error-types-in-python).

## pytest

In the boilerplate example here, run `pytest tests/test_cases.py`

See: https://medium.com/plusteam/pytest-beginners-guide-9fb9451706bf
