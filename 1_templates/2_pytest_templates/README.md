# PyTest Templates

Example pytest scripts.

## Contents

* Common Components
* Useful PyTest Command Line Args
* Resources

---

## Common Components

### Fixtures

Fixtures are used when we want to run some code before every test method. So instead of repeating the same code in every test we define fixtures.

See `test_fixture_example()` in `test_pytest_reusable_components.py`.

### PyTestConfig

PyTestConfig builtins allow you to provide additional command line arguments to your pytests. A good overview is described here: [Using pytestconfig](https://medium.com/pragmatic-programmers/using-pytestconfig-eaeacedbe29a).

They're also commonly used with fixtures as a way to always provide an additional input to all test cases.

See `pytestconfig_fixture_eg` in `test_pytest_reusable_components.py`.

### Parameterize

# TODO

---

## Useful PyTest Command Line Args

* `-k`: this is used to only run target tests that match your substring expression. See `pytest_fixture_example` in the `Makefile`.

### Reporting Args

* `--no-header`: disable the header. IMO, this doesn't add any value and should be disabled by default.
* `-q`: this is used to decrease verbosity. I again tend to include this as a default arg.
* `--disable-pytest-warnings`: this is more subjective/but this will disable all pytest warnings. There are occassions when you will want to see these, so I recommend not including these as a default arg.

---

* Summary of command line args: [Exploring pytest command line options](https://qxf2.com/blog/pytest-command-line-options/).
* [Structuring Unit Tests in Python](https://medium.com/python-in-plain-english/unit-testing-in-python-structure-57acd51da923).
